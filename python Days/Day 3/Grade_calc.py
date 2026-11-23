# Exercise 4: Grade calculator.
marks=int(input("Enter your marks:"))

if marks<0:
    Grade="Invalid input."
elif marks>=90 and marks<=100:
    Grade="A+"
elif marks>=80 and marks<=89:
    Grade="A"
elif marks>=70 and marks<=79:
    Grade="B"
elif marks>=60 and marks<=69:
    Grade="C"
elif marks>=40 and marks<=59:
    Grade="D"
else:
    Grade="F"

print(Grade)



