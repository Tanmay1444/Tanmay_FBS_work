## Enter number of students from user. For those many students accept marks of 5
#subject marks from user and calculate percentage. Display all percentage and
#average percentage of students.

# Enter number of students
n = int(input("Enter number of students: "))

total_percentage = 0

for i in range(1, n + 1):
    print("Enter marks for Student", i)
    
    total_marks = 0
    
    for j in range(1, 6):
        marks = float(input("Enter marks of Subject {}: ".format(j)))
        total_marks += marks
    
    percentage = total_marks / 5
    total_percentage += percentage
    
    print("Percentage of Student", i, "=", percentage)


average_percentage = total_percentage / n
print("Average Percentage of all students =", average_percentage)
