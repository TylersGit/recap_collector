import os
import pywhatkit

phone_number = os.environ["PHONE_NUMBER"]


def message_results(game_states, playing_teams):
        message = ""
        
        for game in game_states:
            teams = game["game"].split(",")[0:2]
            message += (f"{teams} - {game["status"]}")
            for team in teams:
                try:
                    message += f"{team}: {playing_teams[team]}"
                except:
                    continue

            message += "\n"
            pywhatkit.sendwhatmsg_instantly(phone_number, message=message)