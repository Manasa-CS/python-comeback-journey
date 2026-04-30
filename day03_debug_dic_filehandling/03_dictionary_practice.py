# Dictionary Practice
employee = {
   "name": "Manasa",
   "experience": 7,
   "skills": ["Java","React","Python"],
   "scores": {"java": 8, "python": 5}
}
#Accessing Keys
for data in employee:
    print(data)

#Accessing values
for data in employee:
    print(employee[data])

#handle missing keys
if "salary" in employee:
    print(employee["salary"])
else:
    print("Salary not found")

#update values
if "scores" in employee:
    if "python" in employee["scores"]:
        employee["scores"]["python"] = 7

#add new key-value pair
employee["target_role"] = "Software Developer"

#Iterate over nested structures
if "scores" in employee:
    for skill in employee["scores"]:
        print(f"{skill}:{employee['scores'][skill]}")

#Iterate over list of skills
if "skills" in employee:
    for skill in employee["skills"]:
        print(skill)