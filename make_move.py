from new_board import new_board
from get_move import get_move

def make_move(old_board, move, player):
    x = move[0]
    y = move[1]
    
    """ if old_board[x][y] == "X" or "Y":
        print("That is an invalid move, try again!\n")
        get_move()
        make_move(old_board, move, player)

 """
    move_board = old_board
    move_board[x][y] = "X\t"

    return move_board 
           
           
     