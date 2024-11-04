from teams_dict import TEAMS

def game_status_getter(games_set: list[str], schedule):
    game_IDs = []
    for game in games_set:
        game_id = int(game.split("game_ID: ")[1])
        game_IDs.append({
            "game":game, 
            "status": schedule[game_id]["status"]
            })

    return game_IDs