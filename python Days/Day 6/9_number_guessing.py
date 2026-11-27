# This is number guessing game.

num=25
while num>0:
    num1=int(input("Guess the number:"))
    if num1>25:
        print("Too high.")
    elif num1<25:
        print("Too low.")
    elif num==num1:
        print("Correct!")
        break
