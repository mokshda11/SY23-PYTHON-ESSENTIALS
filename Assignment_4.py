#Input secret message (substring)
substring = input("The secret message: ")

#Input coded message (string)
string = input("The coded message is: ")

#Check if the substring is in string
if substring in string:
	print("The secret message is in the coded message")
else:
	print("The secret message is NOT in the coded message")