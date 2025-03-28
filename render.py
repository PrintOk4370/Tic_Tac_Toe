def render(board):
    print("       0\t1\t2\t")
    print("   _____________________________")
    for i in range(3):
        row = [str(i), "|"]
        for cell in board[i]:
            row.append(str(cell))
            row.append("|")
        print(" ".join(row))

    #print("   _____________________________")
    print("  ```````````````````````````````")



