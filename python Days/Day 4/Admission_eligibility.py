# Exercise 3 Admission eligibility checker.

marks=int(input("Enter your marks:"))
attendence=int(input("Enter your attendence in %:"))
exam=input("Did you passed your entrance exam yes or no:")

if marks>=60:
    if attendence>=75:
        if exam=="yes":
            print("You are eligible for Admission.")
        else:
            print("Student is not eligible for Admission.")
    else:
        print("Your attendence is not atleast 75%.")
else:
    print("Your marks is not atleast 60.")
