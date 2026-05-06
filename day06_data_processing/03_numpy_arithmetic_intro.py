# This code demonstrates basic arithmetic operations on NumPy arrays, specifically adding a scalar to an array.
import numpy as np

array = np.array([1, 2, 3])

# Scalar Arithmentic
# Adding a scalar to an array
print("Original array:", array)
print("Add scalar to array:", array + 2)


print("Subtract scalar from array:", array - 2)

print("Multiply array by scalar:", array * 5)

print("Divide array by scalar:", array / 4)

print("To the power of 5 (Array ** 5):", array**5)

# Vectorized math Funcs
print(np.sqrt(array))

array1 = np.array([2.8, 4.24, 3.65])
print("Original floating value array:", array1)
print("Round to nearest:", np.round(array1))
print("Round down using np.floor:", np.floor(array1))
print("Round up using np.ceil:", np.ceil(array1))
print("constant pi defined in numpy pi:", np.pi)

# Example: Calculate the area of circles with different radii using NumPy's vectorized operations
radii = np.array([3, 6, 9])
print(
    "Areas of circles with radii", radii, " : ", np.round(np.pi * radii**2, decimals=2)
)


# Element wise operations
num1 = np.array([2, 5, 6])
num2 = np.array([1, 3, 9])

print("Addition of two numpy arrays:", num1 + num2)
print("Subtraction of two numpy arrays:", num1 - num2)
print("Multiplication of two numpy arrays:", num1 * num2)
print("Division of two numpy arrays:", num1 / num2)
print("Power of two numpy arrays:", num1**num2)


# Comparison of two numpy arrays
print("Comparison of two numpy arrays (num1 > num2):", num1 > num2)
print("Comparison of two numpy arrays (num1 < num2):", num1 < num2)
print("Comparison of two numpy arrays (num1 == num2):", num1 == num2)

# Comparison operations
scores = np.array([85, 92, 78, 90, 88])
# Check which scores are above 90
print("Scores above 90:", scores > 90)
print("Scores below 80:", scores < 80)
print("Scores equal to 88:", scores == 88)
# Logical operations on numpy arrays
attendance = np.array([True, False, True, True, False])
# Check which students attended and scored above 90
print("Students who attended and scored 90 or above:", attendance & (scores >= 90))
