# 🧠 Functions in Python — Practice File
# Author: Anshumaan Sharma
# Topic: Function Basics, Parameters, Return, Default, *args, **kwargs, Recursion

# =========================================
# 1️⃣ FUNCTION BASICS
# =========================================

# Definition:
# A function is a block of code that runs only when called.
# It helps to reuse code and organize logic properly.

# Syntax:
# def function_name(parameters):
#     statement(s)

# Example 1: Simple function
def greet():
    print("Hello, welcome to Python functions!")

# Calling the function
greet()

print("-" * 60)


# =========================================
# 2️⃣ FUNCTION WITH PARAMETERS
# =========================================
def welcome(name):
    print(f"Hello {name}, glad to see you learning Python!")

welcome("Anshumaan")
welcome("Rahul")

print("-" * 60)


# =========================================
# 3️⃣ FUNCTION WITH RETURN VALUE
# =========================================
def add_numbers(a, b):
    return a + b

sum_result = add_numbers(10, 20)
print("Sum =", sum_result)

# You can use return value in other expressions too
print("Sum + 5 =", add_numbers(10, 20) + 5)

print("-" * 60)


# =========================================
# 4️⃣ FUNCTION WITH MULTIPLE RETURNS
# =========================================
def calculate(a, b):
    sum_val = a + b
    diff = a - b
    prod = a * b
    return sum_val, diff, prod  # returning multiple values as tuple

result = calculate(10, 5)
print("Sum, Difference, Product:", result)

print("-" * 60)


# =========================================
# 5️⃣ DEFAULT PARAMETERS
# =========================================
def greet_user(name="User"):
    print(f"Hello, {name}!")

greet_user("Anshumaan")
greet_user()  # uses default

print("-" * 60)


# =========================================
# 6️⃣ ARBITRARY ARGUMENTS (*args)
# =========================================
# Used when you don’t know how many arguments will be passed
def show_fruits(*fruits):
    print("Fruits list:", fruits)
    for fruit in fruits:
        print(f"- {fruit}")

show_fruits("Apple", "Mango", "Banana")

print("-" * 60)


# =========================================
# 7️⃣ KEYWORD ARGUMENTS (**kwargs)
# =========================================
# Used when passing arguments as key-value pairs
def student_details(**info):
    print("Student Details:")
    for key, value in info.items():
        print(f"{key}: {value}")

student_details(name="Anshumaan", course="MCA", university="Galgotias")

print("-" * 60)


# =========================================
# 8️⃣ FUNCTION RETURNING DIFFERENT TYPES
# =========================================
def get_square_list(n):
    squares = []
    for i in range(1, n + 1):
        squares.append(i ** 2)
    return squares

print("Squares from 1 to 5:", get_square_list(5))

print("-" * 60)


# =========================================
# 9️⃣ RECURSIVE FUNCTION
# =========================================
# A function that calls itself (used in factorial, Fibonacci, etc.)
def factorial(n):
    if n == 0 or n == 1:
        return 1
    else:
        return n * factorial(n - 1)

num = 5
print(f"Factorial of {num} =", factorial(num))

print("-" * 60)


# =========================================
# 🔟 LAMBDA (ANONYMOUS FUNCTION)
# =========================================
# Small one-line function without name

square = lambda x: x * x
add = lambda a, b: a + b

print("Square of 4 =", square(4))
print("Sum using lambda =", add(3, 5))

print("-" * 60)


# =========================================
# 🧩 MINI PRACTICE TASKS
# =========================================

# Task 1: Create a function to find max of three numbers
def max_of_three(a, b, c):
    return max(a, b, c)

print("Maximum of (10, 20, 15):", max_of_three(10, 20, 15))

# Task 2: Function to check even or odd
def check_even(num):
    if num % 2 == 0:
        return "Even"
    else:
        return "Odd"

print("10 is", check_even(10))
print("7 is", check_even(7))

# Task 3: Recursive Fibonacci function
def fibonacci(n):
    if n <= 1:
        return n
    else:
        return fibonacci(n - 1) + fibonacci(n - 2)

n = 7
print(f"Fibonacci sequence up to {n}:")
for i in range(n):
    print(fibonacci(i), end=" ")
print("\n")

print("-" * 60)


# =========================================
# ✅ SUMMARY OUTPUT
# =========================================
print("✅ All Function examples executed successfully!")
