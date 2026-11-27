# This is ATM pin verification.

pin=1234
attempt=0

while attempt<3:
    pin1=int(input("Enter your pin:"))
    if pin1==pin:
        print("Access Granted.")
        break
    attempt+=1
    if attempt==3:
        print("Account Locked.")

    