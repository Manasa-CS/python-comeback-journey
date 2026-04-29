if __name__ =='__main__':
    # List comprehension practice
    # Create a list of squared numbers from a given list of numbers
    num = list(map(int, input("Enter a list of numbers separated by space: ").split()))
    sqaured_list = [x**2 for x in num]
    print("Squared list:", sqaured_list)

    # Create a list of even numbers from a given list of numbers
    even_list = [x for x in num if x % 2 == 0]
    print("Even numbers:", even_list)

    # Create a list of uppercase names from a given list of names
    names = list(input("Enter a list of names separated by space: ").split())
    uppercase_names = [name.upper() for name in names]
    print("Uppercase names:", uppercase_names)

    # Create a dictionary of students and their marks, and then create a new dictionary with the average marks of each student
    students = list(input("Enter a list of student names separated by space: ").split())
    for student in students:
        marks_list = list(map(int, input(f"Enter marks for {student}: ").split()))
        students_marks= {student: marks_list for student in students}

    print("Student list:", students_marks)
    average_marks = {student: sum(marks)/len(marks) for student, marks in students_marks.items()}
    print("Average marks of students:", average_marks)