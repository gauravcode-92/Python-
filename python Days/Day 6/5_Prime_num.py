#Exercise 5 : Print all prime numbers between 1 and 100



for num in range(1,101):
    prime=True
    if num<=1:
        prime=False
    else:
        for i in range(2,num):
            if num % i == 0:
                prime=False
                break
    if prime:
        print(num)


           
        




