import os
from espn_api.baseball import League

LEAGUE_ID = os.environ["LEAGUE_ID"]
YEAR = int(os.environ["YEAR"])
SWID = os.environ["SWID"]
ESPN_S2 = os.environ["ESPN_S2"]
TEAM_ID = int(os.environ["TEAM_ID"])


league = League(league_id=LEAGUE_ID, year=YEAR, espn_s2=ESPN_S2, swid=SWID)
team = league.get_team_data(team_id=TEAM_ID)
roster_players = team.roster

# Create a dictionary that lists the playing teams.
# Each key represents a team, and the value represents the players in the team. 
# Only lists players that are not benched/injured
playing_teams = {}

for player in roster_players:
    if player.lineupSlot != "BE" and player.lineupSlot != "IL":
        try:
            if playing_teams[f"{player.proTeam}"] != None: 
                playing_teams[f"{player.proTeam}"].append(player.name)
        except KeyError:
            playing_teams[f"{player.proTeam}"] = [player.name]

