password="Gorav"
pas=len(password)

if pas<6:
	strength="Weak"
elif pas<10:
	strength="Medium"
else:
	strength="Strong"
print("Your password is :",strength)