# File to implement basic functions in python
# define functions
from numbers import Number
from typing import Any


# Addition - takes any type to add
def add(a: Any, b: Any) -> Any:
    return a + b


# Subtraction - takes any type
def subtract(a, b):
    if not (isinstance(a, Number) and isinstance(b, Number)):
        return None
    return a - b


# Multiplication
def multiply(a: Number, b: Number):
    if not (isinstance(a, Number) and isinstance(b, Number)):
        return "Invalid input for multiplication"
    return a * b


# Divide
def divide(a: Number, b: Number) -> Number:
    if not (isinstance(a, Number) and isinstance(b, Number)):
        return None
    if b == 0:
        return "Divide by zero Error"
    return a / b


# is_even
# a function can return a different type unless we manually control it
def is_even(a) -> bool:
    if not (isinstance(a, int)):
        return "Not an integer number"
    return a % 2 == 0


# type hints are not enforced at runtime automatically
# find_max
def find_max(arr):
    max_num = arr[0]
    for num in arr:
        if num > max_num:
            max_num = num
    return max_num

    # Count vowels


def vowel_count(text):
    vowel = "aeiouAEIOU"
    count = 0
    for ch in text:
        if ch in vowel:
            count += 1
    return count


if __name__ == "__main__":
    num1 = 7
    num2 = 23
    num3 = 6.3
    num4 = 12.8
    str1 = "Test"
    str2 = " method"
    num_list = [45, 23, 87, 14, 95]

    print("\n------Addition-------")
    print(f"{num1}+{num2}={add(num1,num2)}")
    print(f"{num3}+{num4}={add(num3,num4)}")
    print(f"{str1}+{str2}={add(str1,str2)}")

    print("\n------Subtraction-------")
    print(f"{num1}-{num2}={subtract(num1,num2)}")
    print(f"{num3}-{num4}={subtract(num3,num4)}")
    print(f"{str1}-{str2}={subtract(str1,str2)}")

    print("\n------Multiplication-------")
    print(f"{num1}*{num2}={multiply(num1,num2)}")
    print(f"{num3}*{num4}={multiply(num3,num4)}")
    print(f"{str1}*{str2}={multiply(str1,str2)}")

    print("\n------Division-------")
    print(f"{num1}/{num2}={divide(num1,num2)}")
    print(f"{num3}/{num4}={divide(num3,num4)}")
    print(f"{num3}/0={divide(num3,0)}")
    print(f"{str1}/{str2}={divide(str1,str2)}")

    print("\n------Even Check-------")
    print(f"{num1} is even: {is_even(num1)}")
    print(f"{num3} is even: {is_even(num3)}")
    try:
        print(f"{str1} is even: {is_even(str1)}")
    except:
        print("Cannot perform arithemetic operations on string")

    print("\n------Get max in list-------")
    print(f"Max nunber is {num_list}: {find_max(num_list)}")

    print(f"Vowel count in {str1}:{vowel_count(str1)}")
    print(f"Vowel count in {str2}:{vowel_count(str2)}")
    print(f"Vowel count in {str1+str2}:{vowel_count(add(str1,str2))}")
