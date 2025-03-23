# main.py - My program to add and subtract two numbers
# Ask for the first number
number1 = input("Enter the first number: ")

# Ask for the second number
number2 = input("Enter the second number: ")

# Make them numbers instead of words
number1 = int(number1)
number2 = int(number2)

# Add them together
add = number1 + number2

# Subtract the second from the first
subtract = number1 - number2

# Show the answers
print("The sum is: ", add)
print("The difference is: ", subtract)