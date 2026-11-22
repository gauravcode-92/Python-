# This is Shopping discount checker

amount=int(input("Enter your shopping amount:"))

if amount>=5000:
    discount=amount*(20/100)
    Total=amount-discount
    print(Total)
elif amount>=3000:
    discount=amount*(10/100)
    Total=amount-discount
    print(Total)
else:
    print(amount)


