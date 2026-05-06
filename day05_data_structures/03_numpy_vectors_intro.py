import numpy as np

array = np.array([[[1, 2, 3], [4, 5, 6]], [[7, 8, 9], [10, 11, 12]]])

array_letter = np.array(
    [
        [["a", "b", "c"], ["d", "e", "f"], ["g", "h", "i"]],
        [["j", "k", "l"], ["m", "n", "o"], ["p", "q", "r"]],
        [["s", "t", "u"], ["v", "w", "x"], ["y", "z", "aa"]],
    ]
)
print("Array shape:\n", array.shape)
# print("Array :\n", array)

print("Array letter shape:\n", array_letter.shape)
# print("Array letter:\n", array_letter)

# multi-dimensional array indexing
print("Element at [0, 1, 2]:", array[0, 1, 2])  # Output: 6
print("Element at [1, 0, 1]:", array[1, 0, 1])  # Output: 8

word = (
    array_letter[0, 0, 2]
    + array_letter[1, 1, 2]
    + array_letter[0, 1, 0]
    + array_letter[0, 1, 1]
)
print(
    "Word formed by array_letter[0, 0, 2], array_letter[1, 1, 2], array_letter[0, 1, 0], array_letter[0, 1, 1]:",
    word,
)

# array slicing
# syntax: array[start:stop:step]
array2 = np.array([[1, 2, 3], [4, 5, 6], [7, 8, 9], [10, 11, 12]])
print("Slicing Array from index 0:\n", array2[0])
print("Slicing Array from index 2:\n", array2[2])
print("Slicing Array from last index:\n", array2[-1])

print("Slicing Array from index 1 with step 2:\n", array2[1, ::2])
print("All array with step 2:\n", array2[::2])
print("All array with negative step 2:\n", array2[::-2])
print("Slicing Array from index 1 to 2:\n", array2[1:2])  # 2 is exclusive

print("Slicing Array from columns:\n", array2[:, 2])  # 2 column in all rows
print(
    "Slicing Array from columns:\n", array2[1:3, 1]
)  # 1st column in rows 1 to 2 , 3 is exclusive

print(
    "Slicing Array from column range:\n", array2[:, 0:2]
)  # 0 to 2d column in all rows , 2 is exclusive

print(
    "Slicing Array from  column in step -2\n", array2[:, ::2]
)  # All rows in column step to 2

print(
    "Slicing Array from column in step -2:\n", array2[:, ::-2]
)  # All rows in column step to - 2

print(
    "Slicing Array from columns from 1 in step -2:\n", array2[:, 1::-2]
)  # All rows in column from column 1 step to - 2

print(
    "Slicing Array from columns from 1 in step 2:\n", array2[:, 1::2]
)  # All rows in column from column 1 step to 2


print(
    "Selecting Qudrant Array from 1:3 rows and 0:2  columns:\n", array2[1:3, 0:2]
)  # All rows in column from column 1 step to 2
