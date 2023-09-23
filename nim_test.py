import hard_script
import impossible_script
import medium_script
import easy_script

nim_start2 = ["|", "|", "|", "|", "|", "|", "|", "|", "|", "|", "|", "|", "|", "|", "|", "|", "|", "|", "|", "|", "|"]
amount = len(nim_start2)

pname = input("Welcome to Nim, hope you don't have fun! what's your name?\n")
dif = input("do you want to play on easy(1), medium(2) or hard(3) or impossible?(4)\n")



if dif == "impossible" or dif == "imp" or dif == "i" or dif == "4":
    print("okay! " + str(pname) + ", you'll be playing against me, the impossible Nim, i wish you bad luck!")
    while amount > 0:
        impossible_script.impossible(pname, nim_start2)

elif dif == "hard" or dif == "h" or dif == "3":
    print("okay! " + str(pname) + ", guess it's me then, the less good nim, good luck!")
    while amount > 0:
        hard_script.hard(pname, nim_start2)

elif dif == "medium" or dif == "med" or dif == "2" or dif == "m":
    print("okay! " + str(pname) + ", i'm the one who's up? i'm not good enough but i hope you have fun!")
    while amount > 0:
        medium_script.medium(pname, nim_start2)

elif dif == "easy" or dif == "ez" or dif == "1" or dif == "e":
    print("okay! " + str(pname) + ", this will be a cakewalk!")
    while amount > 0:
        easy_script.easy(pname, nim_start2)
