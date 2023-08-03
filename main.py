def perform_calculation(num1, num2, operator):

    if operator == '+':
        return num1 + num2
    elif operator == '-':
        return num1 - num2
    elif operator == '*':
        return num1 * num2
    elif operator == '/':
        return num1 / num2
    else:
        return None

def main():
    # Get user input for the two numbers and the arithmetic operator
    num1 = int(input("Enter First Number: "))
    num2 = int(input("Enter Second Number: "))

    print("Enter which operation would you like to perform?")
    operator = input("Enter any of these char for specific operation +, -, *, /: ")

    # Calculate the result using the perform_calculation function
    result = perform_calculation(num1, num2, operator)
    
    # Display the result if the operator is valid; otherwise, show an error message
    if result is not None:
        print(f"{num1} {operator} {num2} = {result}")
    else:
        print("Input character is not recognized!")

if __name__ == "__main__":
    main()

