# This is an ATM Machine to perform different tasks.

pin=4535
balance=10000

pin1=int(input("Enter your pin:"))

if pin1==pin:
    print("These are menu:")
    print(" Check Balance")
    print(" Withdraw Money")
    print(" Deposit Money")
    menu=input("Enter Menu:")
    if menu=="Check Balance":
        print("Your Balance is:",balance)
    elif menu=="Withdraw Money":
        amt=int(input("Enter Withdraw Amount:"))
        if amt>10000:
            print("Enter valid withdraw balance amount.")
        else:
            Total=balance-amt
            print("Withdraw Successfully",amt)
            print("Your balance is:",Total)
    elif menu=="Deposit Money":
        amt=int(input("Enter Deposit Amount:"))
        Total=balance+amt
        print("Deposit Successfully",amt)
        print("Your balance is:",Total)
    else:
        print("Invalid menu.")
else:
    print("Invalid pin.")


