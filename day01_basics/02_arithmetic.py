if __name__ == "__main__":
    num1 = int(input("Enter the first number: "))
    num2 = int(input("Enter the second number: "))
    # Addition
    sum_result = num1 + num2
    print(f"{num1} + {num2} = {sum_result}")

    # Subtraction
    difference = num1 - num2
    print(f"{num1} - {num2} = {difference}")

    # Multiplication
    product = num1 * num2
    print(f"{num1} * {num2} = {product}")

    # Division
    quotient = num1 / num2
    print(f"{num1} / {num2} = {quotient}")
    print(f"division value with two place precision:{num1} / {num2} = {round(quotient, 2)}")
    print(f"division value with two place precision:{num1} / {num2} = {f'{quotient:.2f}'}")
    quotient2 = num1 // num2
    print(f"division value in int:{num1} // {num2} = {quotient2}")

    # Modulus
    remainder = num1 % num2
    print(f"{num1} % {num2} = {remainder}")

    # Exponentiation
    power = num1 ** num2
    print(f"{num1} ** {num2} = {power}")    