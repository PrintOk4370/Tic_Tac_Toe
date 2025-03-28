from make_move import make_move 
from render import *
from new_board import new_board
from get_move import get_move

board = new_board()

player = "X"

for i in range(9): 
    if i%2 == 0: 
        player = "X"
    else:
        player = "O"
        
    move = get_move()
    make_move(board, move, player)
    render(board)