# This is Movie ticket booking system.

age=int(input("Enter your age:"))
discount=0
f_price=0
ticket=(input("You want a regular or premium ticket :"))

if ticket=="regular":
    t_price=150
elif ticket=="premium":
    t_price=250
else:
    print("Invalid Ticket Type. Please choose between regilar or premium ticket.")

if age>0:
    print("Your",ticket,"Ticket price is:",t_price)
    if age<=12:
        discount=t_price * (50/100)
        t_price=t_price - discount
    elif age>=60:
        discount=t_price * (30/100)
        t_price=t_price - discount
    print("Your discount is:",discount)
    print("Your total bill is:",t_price)
else:
    print("Enter valid age number:")




    



