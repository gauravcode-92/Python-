# WAF to find the factorial of n.

def fact(n):
    fact1=1
    for i in range(1,n+1):
        fact1*=i
    print(fact1)

fact(5)
fact(8)