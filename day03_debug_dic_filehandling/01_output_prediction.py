#predict the output of the snippest before running it

#list comprehension
#snippet 1 - The Basic Filter
nums = [1, 2, 3, 4, 5]
result = [x * 2 for x in nums if x % 2 != 0]
print(result)
#predicted output: [2, 6, 10]

#snippet 2 - Ternary Logic (If-Else)
data = ["apple", "bat", "car", "dove"]
output = [word.upper() if len(word) > 3 else word[::-1] for word in data]
print(output)
#predicted output: ["APPLE", "tab","rac",DOVE"]

#snippet 3 - Nested Comprehension
matrix = [[1, 2], [3, 4]]
flat = [num + 1 for row in matrix for num in row]
print(flat)
#predicted output: [2, 3, 4, 5]

#Slicing
#snippet 4 - The "Step" & Reverse
word = "Python"
part_a = word[::2]
part_b = word[::-1]
print(part_a)
print(part_b)
print(part_a + part_b[2:4])
#predicted output: Ptoht

#snippet 5 -  Negative Overlap
nums = [10, 20, 30, 40, 50, 60]
slice_one = nums[-4:-1]
slice_two = nums[1:-2]
print(slice_one == slice_two)
#predicted output: False

#snippet 6 - The Out-of-Bounds "Gotcha"
vals = ["a", "b", "c"]
try:
    x = vals[5]
except IndexError:
    x = "Error"
y = vals[1:10]
print(x, y)
#predicted output: Error ["b","c"]

#snippet 7 -  Slice Assignment
letters = ['a', 'b', 'c', 'd', 'e']
letters[1:4] = ['z']
print(letters)
#predicted output: ['a', 'z', 'e']

#snippet 8 - The "Empty" Step
data = [10, 20, 30, 40, 50]
# Notice the start index is lower than the end index, 
# but the step is negative.
result = data[1:4:-1]
print(result)
#predicted output: []

#snippet 9 - Double Slicing
msg = "Interview_Ready"
output = msg[2:10][::-2]
print(output)
#predicted output: _eve 

#Tuple unpacking
#snippet 10- The "Single Item" Trap
val_a = (5)
val_b = (5,)
result = val_a * 2, val_b * 2
print(result)
#predicted output: (10,5,5)

#snippet 11-  The Immutability "Loophole"
my_tuple = (1, 2, [3, 4])
try:
    my_tuple[2].append(5)
    my_tuple[2] = [10]
except TypeError:
    print("Error Encountered")
print(my_tuple)
#predicted output: Error Encountered (1,2,[3,4,5])

#snippet 12- Starred Unpacking
coords = (10, 20, 30, 40, 50)
x, *y, z = coords
print(x) # first element is assigned
print(y) # in between all assigned as it says y* , if it was for *z then y would contain second element and z would contain the remaining
print(z) # last element
#predicted output: x= 10 y= [20,30,40] z= 50

#all/any 
# 0, None, and empty containers ([], "", {}) are falsy.
#  a container that contains a falsy value (like [0] or (None,)) is actually truthy
#snippet 13-  The Empty Collection Paradox
list_a = []
list_b = [0, False, None, ""]
print(any(list_a), all(list_a))
print(any(list_b), all(list_b))
#predicted output: False, True  False, False

#snippet 14-  Generator Short-Circuiting
def check_num(n):
    print(f"Checking {n}")
    return n > 0

nums = [1, -2, 3]

# Note: any() stops at the first True, all() stops at the first False
result = any(check_num(x) for x in nums)
print(f"Result: {result}")
#predicted output: Checking 1 Result:True

#snippet 15-   The "Truthy" Mixed Bag
data = [10, [0], " ", (None,)]

print(all(data))

#predicted output: True 

#Loops


#snippet 16-   The Loop Reset
count = 0
for i in range(2):
    for j in range(3):
        count += 1
    count += 1

print(count)
#predicted output: 8

#snippet 17-  The "Variable Dependency"
result = []
for i in range(1, 4):
    for j in range(i):
        result.append(i)

print(result)
#predicted output: [1,2,2,3,3,3]

#snippet 18-   The List Append Trap
matrix = []
row = []

for i in range(3):
    row.append(i)
    matrix.append(row) #the matrix does not store three different snapshots of the list; it stores the same memory reference three times.

print(matrix)
#predicted output: [[0, 1, 2], [0, 1, 2], [0, 1, 2]]