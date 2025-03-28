from new_board import new_board
from get_move import get_move

def make_move(old_board, move, player):
    x = move[0]
    y = move[1]
    move_board = old_board

    try:
        if old_board[x][y] == "X" or old_board[x][y] == "O":
            raise ValueError("That spot is already taken.")
        
        move_board[x][y] = player + "\t"
        return move_board

    except ValueError as e:
        print(f"Invalid move: ({x}, {y}) {e}\n")
        make_move(old_board, get_move(), player)
        return None

           
           
     