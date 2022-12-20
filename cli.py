# This file contains the Command Line Interface (CLI) for
# the Tic-Tac-Toe game. This is where input and output happens.
# For core game logic, see logic.py.

from logic import make_empty_board, get_winner, other_player


if __name__ == '__main__':
    board = make_empty_board()
    winner = None
    current_player = '0'
    while winner == None:
        print("TODO: take a turn!")
        for row in board:
            print(row) # TODO: Show the board to the user.
        row = int(input('enter row')) # TODO: Input a move from the player.
        col = int(input('enter col'))
        print(row, col)

        if current_player == '0' and board[row][col] is None:
            board[row][col] = 'O' 
        if current_player == '1' and board[row][col] is None:
            board[row][col] = 'X' 
        if board[row][col] is not None:
            print('Spot taken, please enter a different value')
        winner = get_winner(board) 
        if winner is not None: 
            print(winner)  
        # TODO: Update the board.
        current_player = other_player(current_player) # TODO: Update who's turn it is.
       
