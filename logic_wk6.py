# This file is where game logic lives. No input
# or output happens here. The logic in this file
# should be unit-testable.
import random
import pandas as pd
import os

class Board:
    def __init__(self):
        self.board = [    
            [None, None, None],
            [None, None, None],
            [None, None, None],
        ]

    def get_winner(self):
        """Determines the winner of the given board.
        Returns 'X', 'O', or None."""

        if self.board[0][0] == self.board[0][1] == self.board[0][2]:
            return self.board[0][0]
        if self.board[1][0] == self.board[1][1] == self.board[1][2]:
            return self.board[1][0]                
        if self.board[2][0] == self.board[2][1] == self.board[2][2]:
            return self.board[2][0]
        if self.board[0][0] == self.board[1][0] == self.board[2][0]:
            return self.board[0][0]
        if self.board[0][1] == self.board[1][1] == self.board[2][1]:
            return self.board[0][1]
        if self.board[0][2] == self.board[1][2] == self.board[2][2]:
            return self.board[0][2]
        if self.board[0][0] == self.board[1][1] == self.board[2][2]:
            return self.board[0][0]
        if self.board[0][2] == self.board[1][1] == self.board[2][0]:
            return self.board[0][2]
        found = False
        for i in range(3):
            for j in range(3):
                if self.board[i][j] == None:
                    found = True

            if not found:
                return "Draw"
        
        return None

class Game:

    def __init__(self, player1, player2):
        self.player1 = player1
        self.player2 = player2
        self.board = Board()
        self.turn = 0

    def current_player(self):
        if self.turn %2 == 0:
            return self.player1
        else:
            return self.player2
           
    def make_move(self):
        current_player = self.current_player()
        x, y = current_player.get_move(self.board)
        if current_player == self.player1:
            self.board.board[x][y] = "X"
        else:
            self.board.board[x][y] = "O"

    def get_next_player(self):
        if self.turn == 1:
            self.turn = 2
        else:
            self.turn = 1

    def addGametoCSV(self, winner):
        current_game = {
            'Player 1':[self.player1.name],
            'Player 2':[self.player2.name],
            'Winner': [winner]
            }
        current_game_df = pd.DataFrame.from_dict(current_game)
        output_path = 'game_stats.csv'
        current_game_df.to_csv(output_path, mode="a",header=not os.path.exists(output_path))
        # a for exsiting, w for new file


    def run(self):
        game_not_over = self.board.get_winner() is None
        while game_not_over:
            print(game_not_over, self.board.get_winner())
            self.make_move()
            for row in self.board.board:
                print(row)
            self.get_next_player()
            game_not_over = self.board.get_winner() is None

        self.addGametoCSV(self.board.get_winner())

        return self.board.get_winner()

class Human:
    def __init__(self,name):
        self.name = name

    def get_move(self, board):
        """returns x, and y coordinates"""
        invalid = True
        while invalid or not 0<=x<3 or not 0<=y<3:

            x = int(input("Enter row"))
            y = int(input("Enter column"))
            # Check for valid move
            invalid = board.board[x][y] != None
            if invalid or not 0<=x<3 or not 0<=y<3:
                print("invalid move")

        return [x, y]


class Bot:
    def __init__(self,name):
        self.name = name


    def get_move(self, board):
        """returns x, and y coordinates of the bot"""
        x = random.randrange(3)
        y = random.randrange(3)
        invalid = board.board[x][y] != None
        while invalid: 
            x = random.randrange(3)
            y = random.randrange(3)
            invalid = board.board[x][y] != None

        return [x, y]


