def medium(player, nim_start):
    answer = input(f"so {player},  1, 2 or 3? ")

    if answer == "1":
        del nim_start[0]
    elif answer == "2":
        del nim_start[0:2]
    elif answer == "3":
        del nim_start[0:3]
    amount = len(nim_start)
    print(*nim_start, amount)

    if amount == 1:
        del nim_start[0]
        print("damn, i lose. good game!")
        print("0")
        input("enter anything to exit game ")
        quit()

    if amount == 4:
        del nim_start[0:3]
        print("uh oh")

    if amount == 3:
        del nim_start[0:2]
        print("this doesn't look good for you")

    if amount == 2:
        del nim_start[0]
        print("guess i win!")

    if amount == 0:
        print("good game, i win."),
        input("enter anything to exit game ")
        quit()
    if amount > 4:
        r1 = random.randint(1, 3)
        if r1 == 1:
            del nim_start[0]
            print("i delete 1")
        if r1 == 2:
            del nim_start[0:2]
            print("i remove 2")
        if r1 == 3:
            del nim_start[0:3]
            print("i take away 3")


    amount = len(nim_start)
    print(*nim_start, amount)


import random
