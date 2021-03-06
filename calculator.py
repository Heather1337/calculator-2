"""CLI application for a prefix-notation calculator."""

from arithmetic import (add, subtract, multiply, divide, square, cube,
                        power, mod, )


# Create a repl 
while True:
    # Tokenize a string
    input_string = input("Enter your equation: ")
    tokens = input_string.split(' ')
    result = None

    operator = tokens[0]
    if operator == "q":
        break

    #Checking for input of 1 and returning error 
    if len(tokens) < 2:
        print('Invalid entry, please try again.')

    #Assigning first input digit to var num1
    num1 = tokens[1]
    if not num1.isdigit():
        print("Please provide a number")    
    num2 = 0   

    #Checking if input is 3 or more 
    if len(tokens) > 2:
        num2 = tokens[2]
    if not num2.isdigit():
        print("Please provide a number")


    # Create conditional statements to compare users input to our tokens
    elif operator == "+":
        result = add(float(num1), float(num2))

    elif operator == "-":
        result = subtract(float(num1), float(num2))

    elif operator == "*":
        result = multiply(float(num1), float(num2))

    elif operator == "/":
        result = divide(float(num1), float(num2))

    elif operator == "square":
        result = square(float(num1))

    elif operator == "cube":
        result = cube(float(num1))

    elif operator == "power":
        result = power(float(num1), float(num2))

    elif operator == "mod":
        result = mod(float(num1), float(num2))
    
    print(result)