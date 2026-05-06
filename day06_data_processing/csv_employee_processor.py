import csv
from collections import Counter


def read_employees(file_path):
    # Read file options: r -read, w -write, a -append, r+ -read/write, w+ -write/read, a+ -append/read
    with open(file_path, "r") as file:
        reader = csv.reader(file)
        header = next(reader)
        for row in reader:
            print(row)


def add_employee(file_path, emp_data):
    with open(file_path, "a", newline="") as file:
        writer = csv.writer(file)
        writer.writerow(emp_data)
        file.close()  # not necessary as it is handled by with open()


def print_active_inactive_employee(file_path):
    # 1 - method 1 opening file twice Space complexity and time complexity both increases increases O(N)- twice
    """active_count = 0
    inactive_count = 0
    with open(file_path, "r") as file:
        reader = csv.DictReader(file)
        active_count = sum(1 for employee in reader if employee["status"] == "active")
        file.close()
    with open(file_path, "r") as file:
        reader = csv.DictReader(file)
        inactive_count = sum(
            1 for employee in reader if employee["status"] == "inactive"
        )
        file.close()
    print(f"Total Active Employees{active_count}")
    print(f"Total Inactive Employees:{inactive_count}")"""

    # 2 - method 2 opening file once and going to start position time complexity  increases O(N)- twice
    """active_count = 0
    inactive_count = 0
    with open(file_path, "r") as file:
        reader = csv.DictReader(file)
        active_count = sum(1 for employee in reader if employee["status"] == "active")
        file.seek(0)
        inactive_count = sum(
            1 for employee in reader if employee["status"] == "inactive"
        )
        file.close()
    print(f"Total Active Employees{active_count}")
    print(f"Total Inactive Employees:{inactive_count}") """

    # 3 - method 3 opening file once and going once to count both  incretime complexity will be O(N)- once
    active_count = 0
    inactive_count = 0
    with open(file_path, "r") as file:
        reader = csv.DictReader(file)
        for employee in reader:
            if employee["status"] == "active":
                active_count += 1
            else:
                inactive_count += 1
        file.close()
    print(f"Total Active Employees{active_count}")
    print(f"Total Inactive Employees:{inactive_count}")


def average_salary(file_path):
    # 3 - method 3 opening file once and going once to count both  incretime complexity will be O(N)- once
    with open(file_path, "r") as file:
        total_salary = 0
        total_count = 0
        reader = csv.DictReader(file)
        for employee in reader:
            total_salary += float(employee["salary"])
            total_count += 1
        try:
            average_salary = total_salary / total_count
        except ZeroDivisionError:
            print("Divide by zero error")
        print(f"Average salsry of Employees:{average_salary:.2f}")


def department_count(file_path):
    with open(file_path, "r") as file:
        reader = csv.DictReader(file)
        department = Counter(employee["department"] for employee in reader)
        print(department)


def get_highest_salary(file_path):
    with open(file_path, "r") as file:
        highest_salary = 0
        reader = csv.DictReader(file)
        for employee in reader:
            if float(employee["salary"]) > highest_salary:
                highest_salary = float(employee["salary"])
        return highest_salary


def highest_salary_employee(file_path):
    highest_salary = get_highest_salary(file_path)
    print(highest_salary)
    with open(file_path, "r") as file:
        reader = csv.DictReader(file)
        employee = (
            (employee["id"], employee["name"])
            for employee in reader
            if float(employee["salary"]) == highest_salary
        )
        print(f"Highest salaried employees:{list(employee)}")


if __name__ == "__main__":
    file_path = "resources/employee_data.csv"
    read_employees(file_path)
    add_employee(file_path, ["6", "Shan", "HR", "4000", "active"])
    print_active_inactive_employee(file_path)
    average_salary(file_path)
    department_count(file_path)
    highest_salary_employee(file_path)
