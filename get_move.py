def get_move(): 
    while True: 
        try: 
            Xmove = int(input("What is your move's X co-oridnate?\n")) 
            Ymove = int(input("What is your move's Y co-oridnate?\n"))
            if Xmove >= 3 or Ymove >= 3 or Xmove < 0 or Ymove < 0:
                print("Invalid move, choose something between 0 and 2. \n")
                continue
            return[Xmove,Ymove]
        except: 
            print("Invalid move!!! Please enter numbers between 0 and 2 only. \n\n")
