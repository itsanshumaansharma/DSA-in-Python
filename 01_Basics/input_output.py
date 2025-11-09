# 🧠 Input and Output in Python — Practice File
# Author: Anshumaan Sharma
# Topic: Input(), Output(), Type Conversion, and Formatting

# =========================================
# 1️⃣ INPUT IN PYTHON
# =========================================

# The input() function is used to take user input.
# By default, input() returns data as a string.

name = input("Enter your name: ")
print("Hello,", name)

# -----------------------------------------
# Taking numeric input (type conversion)
age = int(input("Enter your age: "))       # converting string → integer
height = float(input("Enter your height: "))  # converting string → float
print("Your age is:", age)
print("Your height is:", height)

# -----------------------------------------
# Taking multiple inputs in one line
a, b = map(int, input("Enter two numbers: ").split())
print("Sum =", a + b)
print("Difference =", a - b)
print("Product =", a * b)

print("-" * 60)


# =========================================
# 2️⃣ OUTPUT IN PYTHON
# =========================================

# The print() function is used to display output to the user.

# Simple output
print("Welcome to Python Programming!")

# -----------------------------------------
# Printing variables
name = "Anshumaan"
age = 22
print("My name is", name, "and I am", age, "years old.")

# -----------------------------------------
# Using f-string (modern formatting)
print(f"My name is {name} and I am {age} years old.")

# -----------------------------------------
# Formatting numbers
pi = 3.14159265
print("Value of pi:", round(pi, 2))       # round to 2 decimals
print(f"Pi upto 3 decimals: {pi:.3f}")    # format using f-string

# -----------------------------------------
# Printing on the same line using end=""
for i in range(3):
    print(i, end=" ")  # default adds a space instead of new line

print("\n")  # just for line break
print("-" * 60)


# =========================================
# 3️⃣ PRACTICE TASK
# =========================================
# Take user input and perform some calculations.

# Task: Take two numbers and display sum, difference, and product
x = int(input("Enter first number: "))
y = int(input("Enter second number: "))

print(f"Sum = {x + y}")
print(f"Difference = {x - y}")
print(f"Product = {x * y}")
print(f"Average = {(x + y) / 2}")

print("-" * 60)


# =========================================
# 4️⃣ BONUS — Formatting Output Nicely
# =========================================
# You can format text output using escape characters (\n, \t)

print("Name:\tAnshumaan Sharma")
print("Course:\tMCA")
print("University:\tGalgotias University\n")

# Another example of formatted string output
marks = 88
print(f"Your marks are: {marks}/100 — Excellent Work! 👏")

# =========================================
# ✅ Summary Output
# =========================================
print("✅ All Input and Output examples executed successfully!")
