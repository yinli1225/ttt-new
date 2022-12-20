from flask import Flask, render_template, request, redirect
from logic_wk8 import Board, Bot, Game, Human

app = Flask(__name__)



# @app.route('/')
# def mode():
#     player1 = Game("Player 1", "human")
#     player2 = Game("Player 2", "human")
#     game = Game(player1, player2)
#     winner = game.run()
#     return render_template('index.html')

# if __name__ == '__main__':
#     app.run()


# @app.route('/')
# def play():
#     player1 = Game("Player 1", "human")
#     player2 = Game("Player 2", "human")
#     game = Game(player1, player2)
#     winner = game.run()
#     return render_template('play.html')

# if __name__ == '__main__':
#     app.run()
   

@app.route('/')
def stats():
    # player1 = Game("Player 1", "human")
    # player2 = Game("Player 2", "human")
    # game = Game(player1, player2)
    # winner = game.run()
    return render_template('stats.html')


if __name__ == "__main__":
    app.run(debug=True)