def calculator():
    print("Simple Calculator")
    print("Available operations: +, -, *, /")

    try:
        num1 = float(input("Enter the first number: "))
        num2 = float(input("Enter the second number: "))
        operation = input("Choose an operation (+, -, *, /): ")

        if operation == '+':
            result = num1 + num2
        elif operation == '-':
            result = num1 - num2
        elif operation == '*':
            result = num1 * num2
        elif operation == '/':
            if num2 != 0:
                result = num1 / num2
            else:
                print("Error: Cannot divide by zero.")
                return
        else:
            print("Invalid operation selected.")
            return

        print(f"The result is: {result}")

    except ValueError:
        print("Invalid input. Please enter numbers only.")

# Run the calculator
calculator()
