# This is logic authentication system for login.

username="User23"
password="gavu53"

user1=input("Enter Username:")
pass1=input("Enter Password:")

if username==user1 and password==pass1:
    print("Sucessfully logged in.")
elif username!=user1:
    print("Invalid username.")
elif password!=pass1:
    print("Invalid password.")

