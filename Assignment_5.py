#Input number of students
n = int(input("Enter number of students: "))
total_class = 0

#For each student
for i in range(1, n+1):
	total = 0

	#Input 5 test scores
	print("Enter the marks for Student", i)
	for j in range(1, 6):
		marks = float(input("Enter test score" + str(j) + ": "))
		total += marks
	
	#Calculate student average
	average = total / 5
	print("Average score of students: ", i, "=", average)

	total_class += average

#Calculate class average
class_average = total_class / n
print("Overall average score of the class= ", class_average)