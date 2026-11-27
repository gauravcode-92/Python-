# Exercise 6 : Count vowels in a String

sentence=input("Enter a sentence:")
sent=sentence.lower()
count=0

for char in sent:
    if char in "aeiou":
        count += 1

print("Total vowels :",count)
