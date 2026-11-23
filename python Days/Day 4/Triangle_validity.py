# Exercise 5 : Triangle validity checker.

angle1=int(input("Enter First angle:"))
angle2=int(input("Enter Second angle:"))
angle3=int(input("Enter Third angle:"))

sum=angle1+angle2+angle3

if sum==180:
    if angle1>=0 and angle2>=0 and angle3>=0:
        if angle1==angle2==angle3:
            print("This Triangle type is Equilateral.")
        elif angle1==angle2 or angle1==angle3 or angle2==angle3:
            print("This Triangle type is Isosceles.")
        else:
            print("This Triangle type is Scalene.")
    else:
        print("Angles are not negative.")
else:
    print("Sum of triangle angles must be 180.")
