# Exercise 5: Calcultor using conditional statement.

num1=int(input("Enter First Number:"))
num2=int(input("Enter Second Number:"))
operator=input("Enter operator:")

if operator=="+":
    operation=num1+num2
elif operator=="-":
    operation=num1-num2
elif operator=="*":
    operation=num1*num2
elif operator=="/":
    operation=num1/num2
else:
    operation="Invalid operaor."

print(operation)