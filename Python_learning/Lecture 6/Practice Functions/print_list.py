# WAF to print the elements of a list in a single line.
list1=[1,2,3,4,5]
list2=["hi","hello","function"]

def list_print(list):
    for i in list:
        print(i,end=" ")

list_print(list1)