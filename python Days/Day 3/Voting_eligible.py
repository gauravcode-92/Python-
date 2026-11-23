# Exercise 5 : Voting Eligibility checker.

age=int(input("Enter your age:"))

if age>=18:
    print("Person is Eligible to vote.")
elif age<=0:
    print("Invalid input.")
else:
    print("Person is not Eligible to vote.")