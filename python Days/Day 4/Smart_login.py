# This is Smart login system.

username="User28"
password="Gavu123"
acc_status="active"

username1=input("Enter your username:")
password1=input("Enter your password:")

if username1==username:
    if password1==password:
        print("Login Successful.")
        if acc_status=="active":
            print("Your account is active.")
        else:
            print("Your account is blocked.")
    else:
        print("Your password is incorrect.")
else:
    print("Your username is incorrect")
