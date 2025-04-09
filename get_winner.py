board_1 = [
  ['X', 'X', 'O'],
  ['O', 'X', None],
  ['O', 'O', 'X']
]

def get_winner(board):
    win = False
    rows = []
    diagonal = []
    reverse_diagonal = []
    columns = []
    for i in range(3):
        rows.append(board[i])
    for i in range(3):
        diagonal.append(board[i][i])
    for i in range(3):
        reverse_diagonal.append(board[i][2 - i])
    for j in range(3):
        column = [board[i][j] for i in range(3)]
        rows.append(column)

    rows.append(diagonal)
    rows.append(reverse_diagonal)
    
    player = None

    for line in rows: 
        if line[0] == line[1] == line[2]:
            win = True
            player = line[0]
            return(player)
    
    

    return "None   "

#get_winner(board_1)