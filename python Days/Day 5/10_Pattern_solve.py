# This is a program for Pattern.

print("Pattern no. 1 :")

for i in range(1,6):
    for j in range(1,i+1):
        print("*",end="")
    print()

print("Pattern no. 2 :")

for i in range(1,6):
    for j in range(1,i+1):
        print(j,end="")
    print()

print("Patern no. 3 :")

for i in range(1,6):
    for j in range(5,i-1,-1):
        print("*",end="")
    print()