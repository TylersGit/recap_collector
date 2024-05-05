import os
import time 
import datetime

import statsapi

from dotenv import load_dotenv
from espn_api.baseball import League
from teams_dict import TEAMS
from data_getter import playing_teams_getter, relevant_games_getter, game_status_getter
from whatsapp_sender import message_results
from youtube_scraper import get_video_urls, process_urls

load_dotenv()

LEAGUE_ID = os.environ["LEAGUE_ID"]
YEAR = int(os.environ["YEAR"])
SWID = os.environ["SWID"]
ESPN_S2 = os.environ["ESPN_S2"]
TEAM_ID = int(os.environ["TEAM_ID"])

# Make sure that everything works on US time to prevent finicky game times.
# It'll be easier to get the games if they start and end on the same day, rather
# than start at 23:00 and end on 01:00 the next day.  
# Use Chicago as reference point.
# Go Cubs. 
us_timezone = datetime.timezone(datetime.timedelta(hours=-5))
today = datetime.datetime.today().astimezone(tz=us_timezone).strftime("%m/%d/%Y")


def main():
    # MLB Schedule should be collected once a day.
    # Collect the game schedule data from the MLB stats API when the
    # function starts, because we want to always have schedule data available. 
    try:
        schedule = statsapi.schedule(start_date=today, end_date=today)
    except:
        print("Was not able to collect initial schedule data from the API.")
    
    try:
        league = League(league_id=LEAGUE_ID, year=YEAR, espn_s2=ESPN_S2, swid=SWID)
        my_team = league.get_team_data(team_id=TEAM_ID)
        roster_players = my_team.roster
    except:
        print("Was not able to get League or Team data from the ESPN API. ")

    while True:
        print(datetime.datetime.now().astimezone(tz=us_timezone))

        playing_teams = playing_teams_getter(roster_players)
        relevant_games = relevant_games_getter(schedule, playing_teams)
        
        game_states = game_status_getter(relevant_games, schedule)
        if all(game["status"] == "Final" for game in game_states):
            print("all games done")

        urls = get_video_urls()
        relevant_urls = process_urls(urls, relevant_games)

        # message_results(game_states, playing_teams)
        
        # NOTE: Use 60 seconds when testing. 
        # Increase to 30 minutes or so when finished.
        print("Going to sleep for 60.")
        time.sleep(60)


if __name__ == "__main__":
    main()
