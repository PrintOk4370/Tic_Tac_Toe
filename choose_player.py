import random
def choose_player():
    choice = input("Heads (H) or Tails (T)\n")

    if(choice.lower() == "h"):
        choice = 0
    else:
        choice = 1

    if random.randint(0, 1) == choice:
        print("You are X!")
        return("X")
    else:
        print("You are O!")
        return("O")


