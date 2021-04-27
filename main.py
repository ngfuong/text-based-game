from data import Parser
from data.build_game import build_game
from data.Parser import Parser


def game_loop():
    game = build_game()
    parser = Parser(game)
    game.describe()

    while True:
        command = input(">").lower()
        if not (command == "quit" or command == "q"):
            end_game = parser.parse_command(command)
            if end_game:
                return
        else:
            return


game_loop()
print('THANKS FOR PLAYING.')
