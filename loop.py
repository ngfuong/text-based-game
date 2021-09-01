from data.Parser import Parser
from build.build_demo_game import build_game


def game_loop():
    game = build_game()
    parser = Parser(game)
    game.describe()

    while True:
        command = input(">").lower()
        if command == "quit":
            return
        else:
            end_game = parser.parse_command(command)
            if end_game:
                print('THANKS FOR PLAYING')
                return
