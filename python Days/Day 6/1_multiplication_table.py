# Exercise 1 : Print multiplication tables from 1 to 5.

for i in range(1,6):
    print("Table of",i)
    for j in range(1,11):
        mul=i * j
        print(i ,"x", j,"=",mul)
    print()
