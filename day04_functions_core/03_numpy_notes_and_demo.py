# Notes on NumPy - short for numerical Python
# NumPy is a powerful library for numerical computing in Python.
# widely used in AI/ML for handling large datasets and performing mathematical operations efficiently.
# It provides support for arrays, matrices, and a large collection of mathematical functions.
# written in C, making it much faster than Python lists for numerical operations.
# NumPy arrays are more compact and efficient than Python lists, especially for large datasets.

import numpy as np

print(np.__version__)  # Print the version of NumPy being used

# Dimensions in NumPy:
one_d_array = np.array([1, 2, 3, 4, 5])  # Create a NumPy array from a Python list
print(
    f"Number of dimensions for the array {one_d_array}: {one_d_array.ndim}"
)  # Output: 1 (number of dimensions)

zero_d_array = np.array("Hello, NumPy!")  # Create a NumPy array from a string
print(
    f"Number of dimensions for the array {zero_d_array}: {zero_d_array.ndim}"
)  # Output: 0 (number of dimensions))

# Matrix - rows and columns 2d Array
two_d_array = np.array([[1, 2, 3], [4, 5, 6]])  # Create a 2D NumPy array
print(
    f"Number of dimensions for the array {two_d_array}: {two_d_array.ndim}"
)  # Output: 2 (number of dimensions)

# Missing matrix match the number of rows and columns
try:
    invalid_array = np.array(
        [[1, 2], [3, 4, 5]]
    )  # This will raise an error due to mismatched dimensions
except ValueError as e:
    print(f"Error: {e}")

# Element-wise operations in NumPy:
doubled_array = one_d_array * 2  # Element-wise multiplication of the array by 2
print(
    f"Array after element-wise multiplication by 2: {doubled_array}"
)  # Output: [ 2  4  6  8 10]
