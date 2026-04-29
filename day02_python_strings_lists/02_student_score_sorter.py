if __name__ == '__main__':
    # Student score sorter
    # Create a dictionary of students and their marks, and then sort the students based on their average marks
    students = list(input("Enter a list of student names separated by space: ").split())
    students_marks = {}
    for student in students:
        marks_list = list(map(int, input(f"Enter marks for {student}: ").split()))
        students_marks[student] = marks_list

    total_marks = int(input("Enter the total marks for the exam: "))
    # Calculate percentage marks for each student
    print("Student list:", students_marks)
    percentage = {student: round(sum(marks)/total_marks*100, 2) for student, marks in students_marks.items()}
    print("Percentage of students:", percentage)

    # Sort students by average marks in descending order
    sorted_students = sorted(percentage.items(), key=lambda x: x[1], reverse=True)
    print("Students sorted by highest percentage marks:", sorted_students)

    #find the student(s) with the highest average mark
    highest_percentage = sorted_students[0][1]
    top_students = [student for student, avg_mark in sorted_students if avg_mark == highest_percentage]
    print("Top student(s) with the highest percentage mark:", top_students)


    class_average = sum(percentage.values())/ len(percentage)
    print("Class average percentage mark:", class_average)