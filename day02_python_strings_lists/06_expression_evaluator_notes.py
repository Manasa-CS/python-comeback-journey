if __name__=='__main__':
    expression = input("Enter a mathematical expression: ")
    result = eval(expression)
    print(f"The result of the expression '{expression}' is: {result}")

    expression = "print(result)"
    eval(expression)

    string = "Hello, World!"
    print(eval(type(string).__name__))
