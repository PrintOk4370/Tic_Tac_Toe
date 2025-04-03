from http.client import ImproperConnectionState
import sys
import get_winner
from make_move import make_move 
from render import *
from new_board import new_board
from get_move import get_move
from get_winner import get_winner

board = new_board()

player = "X"

for i in range(9): 
    if i%2 == 0: 
        player = "X"
    else:
        player = "O"
        
    move = get_move()
    make_move(board, move, player)
    
    if(get_winner(board)) != "None   ":
        print("Thank you for playing, congratulations ", player)
        sys.exit()
              
    render(board)

    