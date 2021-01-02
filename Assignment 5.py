# This is the list of students enrolled
student = ["abe", "barb", "chris", "abe", "dan", "chris", "ellie", "peter"]
print("All students --> ", student)

# Creating a temporary list
student_temp = []

# A loop iterating over each value in the student list
for x in range(len(student)):
    # if the student is not in the temporary list then appending it
    if student[x] not in student_temp:
        student_temp.append(student[x])

# Assigning the temporary list values to the students list     
student = student_temp 

# Printing out the unique student names with no duplicates
print("Unique students", student)