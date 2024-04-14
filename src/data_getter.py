from teams_dict import TEAMS

def playing_teams_getter(roster_players):
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

    return playing_teams

def relevant_games_getter(schedule, playing_teams):
    relevant_games = set()

    for team in playing_teams.keys():
        for game_ID, game in enumerate(schedule):
            if TEAMS[team] in (game["home_name"], game["away_name"]):
                relevant_games.add(f"{game["home_name"]}, {game["away_name"]}, game_ID: {game_ID}")

    return relevant_games