if __name__ == '__main__':
    candidate_profile = {
        "name": input("Enter candidate's name: "),
        "age": int(input("Enter candidate's age: ")),
        "skills": input("Enter candidate's skills (comma-separated): ").split(","),
        "experience_years": int(input("Enter candidate's years of experience: ")),
        "python_score": int(input("Enter candidate's Python skill score (1-10): ")),
        "ai_score": int(input("Enter candidate's AI skill score (1-10): ")),
    }

    print("\nCandidate Profile:")
    print(f"Name: {candidate_profile['name']}")
    print(f"Age: {candidate_profile['age']}")
    print(f"Skills: {', '.join(candidate_profile['skills'])}")
    print(f"Years of Experience: {candidate_profile['experience_years']}")
    print(f"Python Skill Score: {candidate_profile['python_score']}")
    # Analyze the profile
    if candidate_profile["experience_years"] >= 5:
        print("Candidate is experienced.")
    else:
        print("Candidate is a beginner.")

    if "Python" in candidate_profile["skills"]:
        print("Candidate has Python skills.")
    else:
        print("Candidate does not have Python skills.")

    #Rate Python skills -using if-elif-else
    if candidate_profile["python_score"] >= 7:
        print("Candidate has strong Python skills.")    
    elif candidate_profile["python_score"] >= 4:
        print("Candidate has moderate Python skills.")
    else:
        print("Candidate has weak Python skills.")

    #Rate AI skills - using match-case
    match candidate_profile["ai_score"]:
        case score if score >= 7:
            print("strong AI skills.")
        case score if score >= 4:
            print("moderate AI skills.")
        case score if score >= 1:
            print("basic AI skills.")
        case _:
            print("Candidate has no AI skills.")      