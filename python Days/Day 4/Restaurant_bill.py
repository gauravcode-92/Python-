# This is Restaurant billing system.

print("This is our menu:")
print(" 1. Pizza - 250")
print(" 2. Burger - 120")
print(" 3. Sandwich - 100")
print(" 4. Coffee - 80")

choice=int(input("Enter an item from menu (1-4) :"))
if choice==1:
    price=250
    item="Pizza"
elif choice==2:
    price=120
    item="Burger"
elif choice==3:
    price=100
    item="Sandwich"
elif choice==4:
    price=80
    item="Coffee"
else:
    print("Invalid choice:")
    pass
discount=0
quantity=int(input("Enter quantity of item :"))
if quantity>0:
    bill=price * quantity
    print("Your item is :",item)
    print("Your quantity is :",quantity)
    print("Your bill is :",bill)
    if bill>=500:
        discount=bill * (10/100)
        bill=bill-discount
    elif bill>=1000:
        discount=bill * (20/100)
        bill=bill-discount

    print("Your discount is :",discount)
    print("Your Grand total is :",bill)


