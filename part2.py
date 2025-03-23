# main.py - My program to multiply and divide two numbers
# Ask for the first number
number1 = input("Enter the first number: ")

# Ask for the second number
number2 = input("Enter the second number: ")

# Make them numbers instead of words
number1 = int(number1)
number2 = int(number2)

# Multiply them together
multiply = number1 * number2

# Divide the first by the second
divide = number1 / number2

# Show the answers
print("The product is: ", multiply)
print("The quotient is: ", divide)