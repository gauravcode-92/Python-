# This is a program to find Prime number checker.
prime=True
num=int(input("Enter a number :"))
if num<=1:
    prime=False
else:
    for i in range(2,num):
        if num % i == 0:
            prime=False
            break
    
if prime:
    print(num,"is a prime number.")
else:
    print(num,"is not a prime number.")
