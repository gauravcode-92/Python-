# This is Student marks analysis.

math=int(input("Enter your maths marks:"))
science=int(input("Enter your science marks:"))
python=int(input("Enter your python marks:"))
biology=int(input("Enter your biology marks:"))
c=int(input("Enter your c++ marks:"))

total=math+science+python+biology+c
percentage=total/500 * 100

if percentage>=90:
    Grade="A"
elif percentage>=75:
    Grade="B"
elif percentage>=60:
    Grade="C"
else:
    Grade="D"

print("Your percentage is:",percentage)
print("Your grade is:",Grade)