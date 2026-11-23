# This is Leap year checker.

year=int(input("Enter any year:"))

if (year % 400 == 0):
    print(year,"is a Leap Year.")
elif (year % 4 == 0):
    print(year,"is a Leap Year.")
elif (year % 100 == 0):
    print(year,"is not a Leap Year.")
else:
    print(year,"is not a Leap Year.")