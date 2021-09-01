from flask import Flask
from loop import game_loop

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
def loop():
    game_loop()


if __name__ == "__main__":
    app.run(host="127.0.0.1", port=6666, debug=True)