from get_move import get_move

def make_move(old_board, move, player):
    x = move[0]
    y = move[1]
    move_board = old_board

    try:
        if move_board[x][y] != "None   " or move_board[x][y] != "None   ":
            raise ValueError("That spot is already taken.")
        
        move_board[x][y] = player + "      "
        return move_board

    except ValueError as e:
        print(f"Invalid move: ({x}, {y}) {e}\n")
        make_move(move_board, get_move(), player)
        return None     