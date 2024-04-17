from teams_dict import TEAMS

def playing_teams_getter(roster_players):
# Create a dictionary that lists the playing teams.
# Each key represents a team, and the value represents the players in the team. 
# Only lists players that are not benched/injured
    playing_teams = {}

    for player in roster_players:
        if player.lineupSlot != "BE" and player.lineupSlot != "IL":
            try:
                if playing_teams[f"{TEAMS[player.proTeam]}"] != None: 
                    playing_teams[f"{TEAMS[player.proTeam]}"].append(player.name)
            except KeyError:
                playing_teams[f"{TEAMS[player.proTeam]}"] = [player.name]

    return playing_teams

def relevant_games_getter(schedule, playing_teams):
    relevant_games = set()

    for team in playing_teams.keys():
        for game_ID, game in enumerate(schedule):
            if team in (game["home_name"], game["away_name"]):
                relevant_games.add(f"{game["home_name"]},{game["away_name"]}, game_ID: {game_ID}")

    return relevant_games

def game_status_getter(games_set: list[str], schedule):
    game_IDs = []
    for game in games_set:
        game_id = int(game.split("game_ID: ")[1])
        game_IDs.append({
            "game":game, 
            "status": schedule[game_id]["status"]
            })

    return game_IDs