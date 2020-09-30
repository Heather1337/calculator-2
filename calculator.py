"""CLI application for a prefix-notation calculator."""

from arithmetic import (add, subtract, multiply, divide, square, cube,
                        power, mod, )


# Create a function that takes in a users input and returns an float 
# Create a loop 
while True:
# Tokenize a string
    input_string = input("Enter your equation")
    tokens = input_string.split(' ')
    result = None

    operator = tokens[0]
    if operator == "q":
    break

    if len(tokens) < 2:
        print('Invalid entry, please try again.')
    num1 = float(tokens[1])

    elif len(tokens) > 2:
        num2 = float(tokens[2])
    

    
# Create conditional statements to compare users input to our tokens

    
    elif operator == "+":
        result = add(num1, num2)

    elif operator == "-":
        result = subtract(num1, num2)

    elif operator == "*":
        result = multiply(num1, num2)

    elif operator == "/":
        result = divide(num1, num2)

    elif operator == "square":
        result = square(num1)

    elif operator == "cube":
        result = cube(num1)

    elif operator == "power":
        result = power(num1, num2)

    elif operator == "mod":
        result = mod(num1, num2)
    
    print(result)
# Based on the users input we will call the necessary functions
# Print the end result 



