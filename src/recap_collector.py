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

# Create a list of non injured/benched players. Save their name and the team they're in.
# Additionally, note the teams that are playing. Each team should be listed only once. 
playing_players = []
playing_teams = set()

for player in roster_players:
    if player.lineupSlot != "BE" and player.lineupSlot != "IL":
        playing_teams.add(player.proTeam)
        playing_players.append({
            "name": player.name,
            "team": player.proTeam,
        })

