import os
import time 
import datetime

import statsapi

from dotenv import load_dotenv
from teams_dict import TEAMS
from data_getter import playing_teams_getter, relevant_games_getter, game_status_getter

load_dotenv()

YEAR = int(os.environ["YEAR"])
TEAM = os.environ["team"]

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
    

    while True:
        print(datetime.datetime.now().astimezone(tz=us_timezone))

        # There will usually be only one game, but we will need 
        # to account for double-headers.
        relevant_games = relevant_games_getter(schedule, TEAM)
        
        game_states = game_status_getter(relevant_games, schedule)
        if all(game["status"] == "Final" for game in game_states):
            print("all games done")
        
        # NOTE: Use 60 seconds when testing. 
        # Increase to 30 minutes or so when finished.
        print("Going to sleep for 60.")
        time.sleep(60)


if __name__ == "__main__":
    main()
