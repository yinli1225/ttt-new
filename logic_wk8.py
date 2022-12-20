# This file is where game logic lives. No input
# or output happens here. The logic in this file
# should be unit-testable.
import random
import pandas as pd
import os
import numpy as np
import matplotlib.pyplot as plt

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

    def run(self):
        game_not_over = self.board.get_winner() is None
        moves = 0
        while game_not_over:
            print(game_not_over, self.board.get_winner())
            self.make_move()
            for row in self.board.board:
                print(row)
            self.get_next_player()
            moves += 1
            game_not_over = self.board.get_winner() is None

        winner = self.board.get_winner()
        df = pd.read_csv('game_stats.csv')
        game_count = len(df)

        self.addGametoCSV(winner, game_count, moves)
        
        return winner

    def addGametoCSV(self, winner, game_count, moves):
        if winner == 'X':
            winner_name = self.player1.name
            winner_type = self.player1.player_type
        elif winner == 'O':
            winner_name = self.player2.name
            winner_type = self.player2.player_type
        else:
            winner_name = 'N/A'
            winner_type = 'N/A'

        current_game = {
            'Game ID': [game_count],
            'Player 1':[self.player1.name],
            'Player 1 Type':[self.player1.player_type],
            'Player 2':[self.player2.name],
            'Player 2 Type':[self.player2.player_type],
            'Winner': [winner],
            'Winner Name': [winner_name],
            'Winner Type': [winner_type],
            'Moves': [moves]
            }
        current_game_df = pd.DataFrame.from_dict(current_game)
        output_path = 'game_stats.csv'
        current_game_df.to_csv(output_path, mode="a",header=not os.path.exists(output_path))
        # a for exsiting, w for new file
        

class Human:
    def __init__(self,name,player_type):
        self.name = name
        self.player_type = player_type

    def get_move(self, board):
        """returns x, and y coordinates"""

        while True:

            x = int(input("Enter row"))
            y = int(input("Enter column"))
            # Check for valid move
            if x < 0 or x > 2 or y < 0 or y > 2:
                print("invalid move")
            elif board.board[x][y] != None:
                print("invalid move")
            else:
                break

        return [x, y]

class Bot:
    def __init__(self,name,player_type):
        self.name = name
        self.player_type = player_type


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


