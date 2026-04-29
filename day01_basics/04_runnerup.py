if __name__ == "__main__":
    num = int(input("Enter number of participants: "))
    for i in range(num):
        score = int(input(f"Enter score for participant {i + 1}: "))
        if i == 0:
            highest = score
            second_highest = None
        else:
            if score > highest:
                second_highest = highest
                highest = score
            elif second_highest is None or score > second_highest:
                second_highest = score

    print(f"The second highest score is: {second_highest}")