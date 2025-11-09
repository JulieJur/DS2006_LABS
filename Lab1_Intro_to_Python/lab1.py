print("Welcome to Python programming!")
# This initial lab is just to get you familiar with python.

# Basic arithmetic operations
# Adding two numbers
result_addition = 2 + 6
print("The result of the addition is:", result_addition)

# Multiplying two numbers
result_multiplication = 5 * 3
print("The result of the multiplication is:", result_multiplication)

# Printing a simple message
print("Hello world")

# Variable assignments
A = 10  # Assigning value 10 to variable A
B = 4  # Assigning value 4 to variable B

# Performing and printing results of arithmetic operations
print("The result of the addition is", A + B)
print("The result of the multiplication is", A * B)
print("The result of the division is", A / B)

# Using variables to store user information
name = "Bob"
age = 28

# Printing user information
print("Hi! My name is", name, "and I am", age, "years old.")
print(f"In 2 years, I will be {age + 2} years old")

# Conditional statement based on age
if age > 30:
    print(f"Access granted. Welcome {name}.")
else:
    print(f"Access refused. Common {name}, you can come back in {30 - age} years.")

# List of usernames
usernames = ["Mark", "Sara", "Ahmad", "Johanna"]

# Looping through the list and printing welcome messages
for user in usernames:
    print(f"Welcome {user}")

# Looping to demonstrate range and multiplication
for i in range(0, 10):
    print(f"The double of {i} is {2 * i}")

# Experimenting with the print() function
print("Hello, Data Scientists!")
print("Your full name")

# Demonstrating input function
pseudoname = input("Please enter your pseudoname: ")
print("Hello", pseudoname)

# Demonstrate final variable values
print("The variable A is", A)
print("The variable B is", B)
print("The variable name is", name)
print("The variable age is", age)
print("The variable pseudoname is", pseudoname)
print("The variable usernames is", usernames)
