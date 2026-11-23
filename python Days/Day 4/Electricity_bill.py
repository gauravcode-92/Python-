#Exercise 6 : Elecricity bill with additional consitions.


units=int(input("Enter Units:"))
bill=0
if units<0:
    bill="Invalid input."
elif units==0:
    bill="zero"
    print("Bill is:",bill)
elif units<=100:
    bill=units*5
    print("Bill is:",bill)
elif units>=100 and units<=200:
    bill=(100*5)+((units-100) * 7)
    print("Bill is:",bill)
elif units>=200:
    bill=(100*5)+(100*7)+((units-200)*10)
    print("Bill is:",bill)

if bill>=2000:
    discount=bill*(5/100)
    f_bill=bill-discount
    print("Discount is:",discount)
    print("Final bill:",f_bill)

