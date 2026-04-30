#Bug fixing for faulty snippets

# Snippet 1 - The "Off-by-One" Average

# Goal: Calculate the average of the list
grades = [85, 90, 75, 100]
total = 0
for i in range(len(grades)):
    total += grades[i]
    
#average = total / i  # Something is wrong here
average = total / len(grades)  # Fixed
print(f"Average: {average}")


# Snippet 2 - The Duplicate Disaster

# Goal: Remove duplicates while keeping order
items = ["apple", "banana", "apple", "cherry"]
unique_items = []
for item in items:
    if item not in unique_items:
        #unique_items = unique_items.append(item) 
        unique_items.append(item) #fix because automatically adds no need to assign

print(unique_items) # Why is this printing 'None'?



# Snippet 3 -  The Dictionary Key Crash
# Goal: Check if a user has a specific setting
settings = {"theme": "dark", "notifications": True}

# If 'font_size' isn't there, I want it to say "Not Set"
#if settings["font_size"]: 
if "font_size" in settings:  # fixed one correct syntax to find if key present in tuple
    print(settings["font_size"])
else:
    print("Not Set")



# Snippet 4 - The Accidental Tuple
# Goal: Set a default coordinate
point = (10, 20)
# I want to move it 5 units to the right
#point[0] = point[0] + 5 - we cannot assign to tuple
list_point = list(point) #fix convert to list increment and convert back to tuple
list_point[0] +=  5
point = tuple(list_point)
print(point)



# Snippet 5 - The Case Sensitivity Fail
# Goal: Check if the answer is "yes"
answer = input("Do you want to continue? ") # User types "Yes" or "YES"
if str.lower(answer) == "yes":
    print("Continuing...")
else:
    print("Exiting...")



# Snippet 6 - The Shadowed Built-in
# Goal: Sum a list of numbers
sum = 0
values = [1, 2, 3]
for v in values:
    sum += v

# Later in the code...
#new_total = sum([10, 20]) # This crashes now. Why? #type change sum is int

new_total = sum +10+ 20 # This crashes now. Why? #type change sum is int
print(new_total)

#or
total = 0 # re-name sum to total to avoid shadowing built-in function
values = [1, 2, 3]
for v in values:
    total += v

# Later in the code...
new_total = sum([10, 20]) # This crashes now. Why? #type change sum is int

print(new_total)

# Snippet 7 - The "Infinite" While Loop
# Goal: Countdown from 5 to 1
count = 5
while count > 0:
    print(count)
    # The user forgot something here...
    count-=1 #decrement to end the loop was missing



# Snippet 8 - The String Splitter
# Goal: Get the first word of a sentence
sentence = "Python is fun"
#first_word = sentence.split()[1] 
first_word = sentence.split()[0] #fixed one - index starts from 0 not from 1
print(first_word) # Why does this print 'is' instead of 'Python'?
