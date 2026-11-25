# This is a number guessing game.
num=89

attempt=1
while num>0:
    g_num=int(input("Guess the numer:"))
    if g_num>num:
        print("Too High.")
    elif g_num<num:
        print("Too Low.")
    elif num==g_num:
        print("Congratulations.")
        break
    attempt=attempt+1

print("Your total attempt is :",attempt)
        


