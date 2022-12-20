from flask import Flask, render_template, request, redirect
from logic_wk10 import Board, Bot, Game, Human
import pandas as pd
app = Flask(__name__)

game=""
moves = 0
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
def start():
    # player1 = Game("Player 1", "human")
    # player2 = Game("Player 2", "human")
    # game = Game(player1, player2)
    # winner = game.run()

    return render_template('index.html')

@app.route('/play',methods=['POST'])
def play():
    # player1 = Game("Player 1", "human")
    # player2 = Game("Player 2", "human")
    # game = Game(player1, player2)
    # winner = game.run()
    determine_player_1 = request.form.get('player0_mode')
    if determine_player_1 == "human":
        human_name = request.form.get('player1')
        player1 = Human(human_name, "Human")
    else:
        bot_name = "Bot"
        player1 = Bot(bot_name, "Bot")

    determine_player_2 = request.form.get('player1_mode')
    if determine_player_2 == "human":
        human_name = request.form.get('player2')
        player2 = Human(human_name, "Human")
    else:
        bot_name = "Bot2"
        player2 = Bot(bot_name, "Bot")

    print(player1.name, "vs", player2.name)
    global game
    game = Game(player1, player2)
    return render_template('play.html')


@app.route('/move',methods=['POST'])
def move():
    global moves
    global game
    x=int(request.form.get('row'))
    y=int(request.form.get('column'))
    game.set_nextmove(x,y)
    #game_not_over = game.board.get_winner() is None
    game.make_move()
    for row in game.board.board:
        print(row)
    game.get_next_player()
    moves += 1
    game_not_over = game.board.get_winner() is None
    if not game_not_over:
        winner = game.board.get_winner()
        df = pd.read_csv('game_stats.csv')
        game_count = len(df)
        game.addGametoCSV(winner, game_count, moves)
        return returnBoard(game,"Game Over! Winner is "+winner)
    else:
        return returnBoard(game)

def returnBoard(game,result=""):
    p11=game.board.board[0][0]
    p12=game.board.board[0][1]
    p13=game.board.board[0][2]
    p21=game.board.board[1][0]
    p22=game.board.board[1][1]
    p23=game.board.board[1][2]
    p31=game.board.board[2][0]
    p32=game.board.board[2][1]
    p33=game.board.board[2][2]
    return render_template('play.html',
                           p11=p11,p12=p12,p13=p13,
                           p21=p21,p22=p22,p23=p23,
                           p31=p31,p32=p32,p33=p33,result=result)

@app.route('/stats',methods=['POST'])
def stats():
    return render_template('stats.html')



if __name__ == "__main__":
    app.run(host='127.0.0.1', port=5000, debug=True)