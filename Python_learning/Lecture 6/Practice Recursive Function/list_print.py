# Write a recursive function to print all elements in a list

def list_print(list,idx=0):
    if (idx==len(list)):
        return
    print(list[idx])
    return list_print(list,idx+1)

fruits=["apple","banana","lichi"]
list_print(fruits)