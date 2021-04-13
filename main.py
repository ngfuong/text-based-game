from data import *


def game_loop():
    game = build_game()
    parser = Parser(game)
    game.describe()

    command = ""
    while not command.lower() == "quit" and not command.lower == "q":
        command = input(">")
        end_game = parser.parse_command(command)
        if end_game:
            return


game_loop()
print('THE GAME HAS ENDED')
