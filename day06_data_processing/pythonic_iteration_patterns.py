"""
This script demonstrates various Pythonic iteration patterns, including:
- Iterating over a single list
- Iterating over multiple lists simultaneously
- Using enumerate()
- Using zip()
"""


def iterate_single_list(names):
    for name in names:
        print(name)


# Using Zip to iterate over multiple lists simultaneously.
#  zip() takes multiple iterables and returns an iterator of tuples, where the i-th tuple contains the i-th element from each of the input iterables.
#   if the iterables are of different lengths, zip() stops when the shortest iterable is exhausted.
def iterate_multiple_lists(names, ids, scores):
    for name, id, score in zip(names, ids, scores):
        print(f"{name} (ID: {id}) scored {score}")


def iterate_print_scors(names, scores):
    for name, score in zip(names, scores):
        print(f"{name} scored {score}")


def iterate_with_enumerate(names):
    # enumerate(names, start=1) to start index from 1 instead of 0
    for index, name in enumerate(names):
        print(f"{index}: {name}")


def iterate_with_enumerate_and_zip(names, ids, scores):
    for index, (name, id, score) in enumerate(zip(names, ids, scores)):
        print(f"{index}: {name} (ID: {id}) scored {score}")


# Example: Calculate the average score from a variable number of scores using *args
def find_average_score(*scores):
    if len(scores) == 0:
        return 0
    return round(sum(scores) / len(scores), 2)


# Example: Create a profile using **kwargs to accept a variable number of keyword arguments
def create_profile(**details):
    profile = {}
    for key, value in details.items():
        profile[key] = value
    return profile


def group_scores_by_grade(names, scores):
    grade_groups = {"A": [], "B": [], "C": [], "D": [], "F": []}
    for name, score in zip(names, scores):
        if score >= 90:
            grade_groups["A"].append(name)
        elif score >= 80:
            grade_groups["B"].append(name)
        elif score >= 70:
            grade_groups["C"].append(name)
        elif score >= 60:
            grade_groups["D"].append(name)
        else:
            grade_groups["F"].append(name)
    return grade_groups


if __name__ == "__main__":
    names = ["Alice", "Bob", "Charlie", "David"]
    ids = [101, 102, 103]
    scores = [85, 90, 78, 92]
    iterate_single_list(names)
    print("\nIterate with zip:")
    iterate_print_scors(names, scores)
    print(
        "Iterate with different lengths: id contains less so the iteration stops at the shortest list"
    )
    iterate_multiple_lists(names, ids, scores)
    print("\nIterate with enumerate:")
    iterate_with_enumerate(names)
    print("\nIterate with enumerate and zip:")
    iterate_with_enumerate_and_zip(names, ids, scores)

    print("\nFind average score:")
    print(find_average_score(85, 90, 78, 92))
    print(find_average_score())
    print(find_average_score(68, 74, 82))

    print("\nCreate profile:")
    profile = create_profile(name="Alice", age=30, city="New York")
    print(profile)
    profile2 = create_profile(name="Bob", profession="Engineer", hobby="Hiking")
    print(profile2)

    print("Unpacking example")
    x, *y, points = [10, 20, 3, 6, 7, 9]
    print(x)
    print(y)
    print(points)

    print("Filter even numbers")
    print(list(filter(lambda score: score % 2 == 0, scores)))

    print("Sort names by length")
    print(sorted(names, key=lambda name: len(name)))

    print("Square scores using map and lambda")
    print(list(map(lambda score: score**2, scores)))

    print("Group scores by grade:")
    grade_groups = group_scores_by_grade(names, scores)
    for grade, students in grade_groups.items():
        if grade_groups[grade]:  # Only print grades that have students
            print(f"Grade {grade}: {', '.join(students)}")
