def impossible(player, nim_start):

    answer = input(f"so {player},  1, 2 or 3? ")

    if answer == "1":
        del nim_start[0]
    elif answer == "2":
        del nim_start[0:2]
    elif answer == "3":
        del nim_start[0:3]
    amount = len(nim_start)
    print(*nim_start, amount)

    if answer == "1":
        del nim_start[0:3]
        print("i remove three")
    if answer == "2":
        del nim_start[0:2]
        print("i remove two")
    if answer == "3":
        del nim_start[0]
        print("i remove one")
    amount = len(nim_start)
    print(*nim_start, amount)

    if amount == 4:
        del nim_start[0:3]
        print("i delete three, good luck!")

    if amount == 3:
        del nim_start[0:2]
        print("i delete two, your turn")

    if amount == 2:
        del nim_start[0]
        print("i delete one, do your last move")

    if amount == 1:
        del nim_start[0]
        print("you won! that was a fun game")
        input("enter anything to exit game ")
        quit()

    if amount == 0:
        print("Game over, you lose, i win."),
        input("enter anything to exit game ")
        quit()
