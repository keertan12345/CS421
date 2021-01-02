# Create tuple for each student
student_1 = ("abe", 16, 88)
student_2 = ("barb", 30, 72)
student_3 = ("chris", 14, 92)
student_4 = ("dan", 20, 80)
student_5 = ("ethan", 16, 60)

# Create a tuple to represent the class
big_tuple = (student_1, student_2, student_3, student_4, student_5)

# Function that gets the average age
def getAverageAge(big_tuple):
    total_age = 0
    for x in big_tuple:
        name, age, marks = x
        total_age = total_age + age
    
    no_of_students = len(big_tuple)
    average_age = total_age / no_of_students
    
    return average_age
    
# Function that gets the average marks
def getAverageMarks(big_tuple):

    total_marks = 0
    for x in big_tuple:
        name, age, marks = x
        total_marks = total_marks + marks
    
    no_of_students = len(big_tuple)
    average_marks = total_marks / no_of_students
    return average_marks
    
# Function that returns the lowest mark
def getLowestMark(big_tuple):
    marks_list = []
    
    for x in big_tuple:
        name, age, marks = x
        marks_list.append(marks)
    
    marks_list.sort
    lowest_mark = marks_list[0]
    return lowest_mark
    
# Function that returns the highest mark
def getHighestMark(big_tuple):
    marks_list = []
    
    for x in big_tuple:
        name, age, marks = x
        marks_list.append(marks)
    
    marks_list.sort(reverse = True)
    highest_mark = marks_list[0]
    return highest_mark

# Function that returns the summary of all the previous functions
def getSummary(big_tuple):
      #1. total_no_of_students
      total_no_of_students = len(big_tuple)
      
      #2. average_age
      average_age = getAverageAge(big_tuple)
   
      #3. average_marks
      average_marks = getAverageMarks(big_tuple)
      
      #4 highest_mark
      highest_mark = getHighestMark(big_tuple)
      
      #5 lowest_mark
      lowest_mark = getLowestMark(big_tuple)
      
      # construct the summary tuple
      summary_tuple = (total_no_of_students,average_age,average_marks,highest_mark,lowest_mark)
      
      return summary_tuple

result = getSummary(big_tuple)
print(result)