# Write a recursive function to calculate the sum of first n natural numbers

def sum_print(n):
    if(n==0):
        return 0
    return (sum_print(n-1) + n)

print(sum_print(8))