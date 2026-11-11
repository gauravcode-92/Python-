count=0
with open("demo.txt","r") as f:
    data=f.read()
    print(data)

    nums=data.split(",")
    for get in nums:
        if(int(get) %2 == 0):
            count += 1

print(count)

