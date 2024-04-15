import os
import datetime

import statsapi
from espn_api.baseball import League

from teams_dict import TEAMS
from data_getter import playing_teams_getter, relevant_games_getter

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

league = League(league_id=LEAGUE_ID, year=YEAR, espn_s2=ESPN_S2, swid=SWID)
schedule = statsapi.schedule(start_date=today, end_date=today)


my_team = league.get_team_data(team_id=TEAM_ID)
roster_players = my_team.roster

playing_teams = playing_teams_getter(roster_players)
relevant_games = relevant_games_getter(schedule, playing_teams)
