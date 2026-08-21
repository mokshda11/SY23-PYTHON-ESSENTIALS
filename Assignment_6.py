#Keep checking until "Stop"
while True:
	password  = input("Enter password: ")

	if password.lower() == "stop":
		break

	upper = lower = digit = False

	#Check password characters
	for ch in password:
		if ch.isupper():
			upper = True
		elif ch.islower():
			lower = True
		elif ch.isdigit():
			digit = True

	#Check all conditions
	if len(password) >= 8 and upper and lower and digit:
		print("Strong Password")
	else:
		print("Weak Password")