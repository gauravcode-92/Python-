# This is Bank loan eligibility system.

age=int(input("Enter your age:"))
m_salary=int(input("Enter your salary:"))
c_score=int(input("Enter your credit score:"))

if age>=21:
    if m_salary>=25000:
        if c_score>=700:
            print("You are eligible for a loan.")
        else:
            print("Credit score must be at least 700.")
    else:
        print("Monthly salary must be at least 25000.")
else:
    print("Your age must be at least 21.")