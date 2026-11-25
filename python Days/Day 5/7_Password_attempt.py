# This is Password attempt system.
n=1
password="Goru98"
attempt=3
while n<=3:
    password1=input("Enter your password :")
    if password1==password:
        print("Login Successful.")
    else:
        attempt=attempt-1
        print("Your remaining attempts :",attempt)
    if attempt==0:
        print("Your Account Locked.")
        break
    n=n+1