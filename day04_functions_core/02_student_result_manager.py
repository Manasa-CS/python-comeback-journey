# Define a class Student with attributes name, date_of_birth, grade, score (list of scores in 3 subjects) and total (sum of scores in all subjects). Create a list of students and implement the following functions:
class Student:
    def __init__(self, name, date_of_birth, grade, score):
        self.name = name
        self.date_of_birth = date_of_birth
        self.grade = grade
        self.score = score
        self.total = sum(score)

    def __repr__(self):
        return f"Student(name='{self.name}', DOB={self.date_of_birth}, Grade={self.grade}, score={self.score})"


# Add a student to the list of students.
def add_student(stud_list: [Student], stud: Student):
    stud_list.append(stud)


# Print the name of the student with the highest total score.
def print_topper(stud_list: [Student]):
    top_score = max(stud.total for stud in stud_list)
    top_students = [stud for stud in stud_list if stud.total == top_score]
    print(f"Toppers with total score {top_score}:")
    for stud in top_students:
        print(stud.name)


# Print the average score of the class in all subjects.
def print_average(stud_list: [Student]):
    average = sum(stud.total for stud in stud_list) / len(stud_list)
    print(f"class average score in all subjects:{average}")


# Print the name, date of birth, grade and total score of all students in a tabular format.
def print_all(stud_list: [Student]):
    print("Name\t    DOB\t\tGrade\tTotal_Score")
    print(
        "-----------------------------------------------------------------------------------------"
    )
    for stud in stud_list:
        print(f"{stud.name:<10}{stud.date_of_birth:<15}{stud.grade:<8}{stud.total:<10}")


if __name__ == "__main__":
    student_list = []
    student1 = Student("John", "03/19/2016", "4", [89, 93, 92])
    student2 = Student("Mary", "05/9/2016", "4", [90, 93, 94])
    student3 = Student("Kate", "29/07/2016", "4", [75, 80, 91])
    student4 = Student("Linda", "18/01/2017", "4", [94, 90, 93])
    add_student(student_list, student1)
    add_student(student_list, student2)
    add_student(student_list, student3)
    add_student(student_list, student4)
    print(student_list)
    print_topper(student_list)
    print_average(student_list)
    print_all(student_list)
