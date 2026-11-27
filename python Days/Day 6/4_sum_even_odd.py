# Exercise 4 : Sum of Even and Odd numbers.
sum=0
sum2=0
for i in range(1,101):
    if i<1:
        pass       
    else:
        if i % 2 == 0:
            sum=sum+i
        else:
            sum2=sum2+i


print("Sum of even numbers :",sum)   
print("Sum of odd numbers :",sum2)
        
