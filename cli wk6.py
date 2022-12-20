# This file contains the Command Line Interface (CLI) for
# the Tic-Tac-Toe game. This is where input and output happens.
# For core game logic, see logic.py.

from logic_wk6 import Board, Bot, Game, Human

if __name__ == "__main__":
    game_start = True
    while game_start: 
        determine_player_1 = int(input("Choose first player, 0 for a human, 1 for a bot:"))
        if determine_player_1 == 0:
            human_name = input("Name of the player: ")
            player1 = Human(human_name)
        else:
            bot_name = input("Name of the player: ")
            player1 = Bot(bot_name)

        determine_player_2 = int(input("Choose second player, 0 for a human, 1 for a bot:"))
        if determine_player_2 == 0:
            human_name = input("Name of the player: ")
            while human_name == player1.name:
                human_name = input("Player existing, pick another name: ")
            player2 = Human(human_name)
        else:
            bot_name = input("Name of the player: ")
            while bot_name == player1.name:
                bot_name = input("Player existing, pick another name: ")
            player2 = Bot(bot_name)
           

        print(player1.name, "vs", player2.name)
        game = Game(player1, player2)
        winner = game.run()
        print(winner, " won the game")

        end_game = input("End game or not, Y for end, N for continue: ")

        if end_game == "Y":
            game_start = False



    
   