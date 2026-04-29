if __name__ =='__main__':
    student_list=[["John", 85,2], ["Bob", 78,3], ["Eve", 92,1],  ["Alice", 92,1]]

    # Sort students by rank in ascending order
    student_list.sort(key=lambda x: (x[2], x[0]))
    print("Students sorted by rank and name (ascending):", student_list)

    # Sort students by marks in descending order
    student_list.sort(key=lambda x:(x[1],x[0]), reverse=True)
    print("Students sorted by marks and name (descending):", student_list)

    student_list.sort(key=lambda x: len(x[0]))
    print("Students sorted by name length:", student_list)