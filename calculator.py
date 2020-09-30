"""CLI application for a prefix-notation calculator."""

from arithmetic import (add, subtract, multiply, divide, square, cube,
                        power, mod, )


# Create a function that takes in a users input and returns an float 
# Create a loop 
while True:
# Tokenize a string
    input_string = input("Enter your equation")
    tokens = input_string.split(' ')

    operator = tokens[0]
    num1 = float(tokens[1])

    if len(tokens) > 2:
        num2 = float(tokens[2])
    
# Create conditional statements to compare users input to our tokens
    if operator == "q":
        break
    
    elif operator == "+":
        add(num1, num2)

    elif operator == "-":
        subtract(num1, num2)
    

# Based on the users input we will call the necessary functions
# Print the end result 



