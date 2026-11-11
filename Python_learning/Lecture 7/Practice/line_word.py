def line_word():
    data=True
    word="learning"
    line=1

    with open("practice.txt","r") as f:
        while data:
            data=f.readline()
            if(word in data):
                print(line)
                return
            line += 1
    return -1
print(line_word())
        