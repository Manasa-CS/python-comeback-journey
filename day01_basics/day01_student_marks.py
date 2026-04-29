if __name__ == "__main__":
    studentCount = int(input("Enter the number of students: "))
    students = {}
    for i in range(studentCount):
        name = input(f"Enter the name of student {i + 1}: ")
        marks = list(map(float, input(f"Enter the  three subject marks for {name}: ").split()))
        totalMarks = sum(marks)
        averageMarks = totalMarks / len(marks)
        students[name] = {"marks": marks, "total": totalMarks, "average": averageMarks}
    query_student = input("Enter the name of the student to query: ")
    if query_student in students:
        print(f"Marks for {query_student}: {students[query_student]['marks']}")
        print(f"Total marks for {query_student}: {students[query_student]['total']}")
        print(f"Average marks for {query_student}: {students[query_student]['average']}")
    else:
        print(f"Student {query_student} not found.")

