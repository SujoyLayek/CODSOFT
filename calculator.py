def calculator():
    print("Welcome to the basic calculator!")
    
    num1 = float(input("Enter the first number: "))
    num2 = float(input("Enter the second number: "))
    
    print("Choose an operation:")
    print("1. Addition (+)")
    print("2. Subtraction (-)")
    print("3. Multiplication (*)")
    print("4. Division (/)")
    
    operation = input("Enter the operation (+, -, *, /): ")

    if operation == '+':
        result = num1 + num2
        print(f"The result of {num1} + {num2} is: {result}")
    elif operation == '-':
        result = num1 - num2
        print(f"The result of {num1} - {num2} is: {result}")
    elif operation == '*':
        result = num1 * num2
        print(f"The result of {num1} * {num2} is: {result}")
    elif operation == '/':
        if num2 != 0:
            result = num1 / num2
            print(f"The result of {num1} / {num2} is: {result}")
        else:
            print("Error: Division by zero is not allowed.")
    else:
        print("Invalid operation choice. Please try again.")


calculator()
