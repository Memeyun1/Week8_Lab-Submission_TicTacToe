# This file contains the Command Line Interface (CLI) for
# the Tic-Tac-Toe game. This is where input and output happens.
# For core game logic, see logic.py.

import logic
def show_board(board):
    for x in range(3):               #show a 3X3 board to the terminal
        for y in range(3):    
            if board[x][y] == None:
                print(" ", end = "|")
            else: 
                print(board[x][y],end ="|")    
        print("\n")
game = logic.Game()                  #initialize all object
human = logic.Player("O")
bot = logic.Robot("X")
if __name__ == '__main__':
    game.board = game.make_empty_board()
    winner = None
    while winner == None:
        print("TODO: take a turn!")
        # TODO: Show the board to the user.
        show_board(game.board)
        
        # TODO: Input a move from the player.
        row = input("pls enter the row: ")
        col = input("pls enter the col: ")

        # TODO: Update the board.
        game.board = human.player_move(int(row),int(col),game.board)
        show_board(game.board)
        
        # TODO: Check who win
        winner = game.get_winner(game.board)

        
        
        # TODO: if someone win, break the loop
        if winner != None:
            break
        
        # TODO: Robot's turn
        game.board = bot.robot_move(game.board)
        
        # TODO: Update the board.
        show_board(game.board)
        
        # TODO: Check who win
        winner = game.get_winner(game.board)

    print('--------winner is'+ winner +'-------------')