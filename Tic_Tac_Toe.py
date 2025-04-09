import sys
from choose_player import choose_player
from get_winner import get_winner
from make_move import make_move 
from render import *
from new_board import new_board
from get_move import get_move
from get_winner import get_winner

board = new_board()

player = choose_player()

for i in range(9): 
    move = get_move()
    make_move(board, move, player)

    render(board)

    if(get_winner(board)) != "None   ":
        print("Thank you for playing, congratulations ", player)
        sys.exit()
    
    if player == "X": 
        player = "O"
    elif player == "O":
        player = "X"

print("Its a draw :(")            