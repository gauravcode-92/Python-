# Exercise 1: Number comparison between two numbers

num1=int(input("Enter your first number:"))
num2=int(input("Enter your second number:"))

if num1>num2:
    print(num1, "is grater than",num2)
elif num2>num1:
    print(num2,"is grater than",num1)
elif num1==num2:
    print("both numbers are equal.")