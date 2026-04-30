import json

#create a dictionary and write it to a json file
candidate_profile = {
    "name": "Manasa",  
    "experience": 7,
    "primary_skills": ["Java", "React", "Python"],
    "ai_learning_day": True
}

#Write the dictionary to a JSON file
with open("candidate_profile.json", "w") as file:
    json.dump(candidate_profile, file)

#Read the JSON file and load it back into a dictionary
with open("candidate_profile.json", "r") as file:
    loaded_profile = json.load(file)    
    print(loaded_profile)
    print("Candidate Name:", loaded_profile["name"])
    print("Primary Skills:", loaded_profile["primary_skills"])
    print("Target Role:", loaded_profile.get("target_role", "Not Mentioned"))