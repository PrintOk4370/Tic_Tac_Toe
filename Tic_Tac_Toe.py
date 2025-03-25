from render import *
from new_board import new_board

board = new_board()

board[0][1] = 'X'
board[1][1] = 'O'

render(board)
