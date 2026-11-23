#Exercise 2: Age category checker.

age=int(input("Enter your age:"))

if  age>=0 and age<=12 :
    category="Child"
elif age>=13 and age<=19:
    category="Teenager"
elif age>=20 and age<=59:
    category="Adult"
else:
    category="Senior Citizen"

print(category)