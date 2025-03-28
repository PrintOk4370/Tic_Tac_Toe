from make_move import make_move 
from render import *
from new_board import new_board
from get_move import get_move

player = "X"
board = new_board()

board[0][1] = 'X'
board[1][1] = 'O'

render(board)

move = get_move()

move_made = make_move(board, move, player)

render(board)