def basic_calculator_simplified():
    """
    A very basic calculator program for addition, subtraction,
    multiplication, or division. Assumes valid input.
    """
    print("Welcome My Basic Calculator!")

    # Get the first number
    num1 = float(input("Enter the first number: "))

    # Get the second number
    num2 = float(input("Enter the second number: "))

    # Get the operation
    operation = input("Enter the operation (+, -, *, /): ")

    # Perform the calculation based on the operation
    if operation == '+':
        result = num1 + num2
        print(f"{num1} + {num2} = {result}")
        
    elif operation == '-':
        result = num1 - num2
        print(f"{num1} - {num2} = {result}")
        
    elif operation == '*':
        result = num1 * num2
        print(f"{num1} * {num2} = {result}")
        
    elif operation == '/':
        # Basic check for division by zero
        if num2 != 0:
            result = num1 / num2
            print(f"{num1} / {num2} = {result}")
        else:
            print("Cannot divide by zero.")
    else:
        print("Invalid operation. Please use +, -, *, or /.")

# Run the simplified calculator
basic_calculator_simplified()