def render(board):
    print("       0\t1\t2\t")
    print("   _________________________")
    for i in range(3):
        print(i, "| ", "\t".join(board[i]), "|")
    print("   _________________________")



