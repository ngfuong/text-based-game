from flask import Flask
from data.Parser import Parser
from data.build_game import build_game

app = Flask(__name__)

# @app.route("/")
# def index():
#     return "Congratulations, it's a web app!"


@app.route("/")
def affer_page():
    return  """
        <html>
            <body>
                <p>Player's input:</p>
                <form>
                    <p><input name="user_input" /></p>
                    <p><input type="submit" value="Submit" /></p>
                </form>
            </body>
        </html>
    """


@app.route("/")
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


if __name__ == "__main__":
    app.run(host="127.0.0.1", port=6666, debug=True)