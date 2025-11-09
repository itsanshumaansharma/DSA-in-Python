# 🧠 Control Statements in Python — Practice File
# Author: Anshumaan Sharma
# Topic: if-else, loops (for, while), break, continue, pass

# =========================================
# 1️⃣ CONDITIONAL STATEMENTS (if, elif, else)
# =========================================

# Definition:
# Used to make decisions — run certain code only if a condition is true.

# Example 1: Simple if
num = 10
if num > 0:
    print("Number is positive")

# Example 2: if-else
age = 18
if age >= 18:
    print("You are eligible to vote.")
else:
    print("You are not eligible to vote.")

# Example 3: if-elif-else ladder
marks = 85
if marks >= 90:
    print("Grade: A+")
elif marks >= 75:
    print("Grade: A")
elif marks >= 60:
    print("Grade: B")
else:
    print("Grade: C")

print("-" * 60)


# =========================================
# 2️⃣ NESTED IF STATEMENT
# =========================================

# if inside another if
num = int(input("Enter a number: "))

if num >= 0:
    if num == 0:
        print("Number is Zero")
    else:
        print("Number is Positive")
else:
    print("Number is Negative")

print("-" * 60)


# =========================================
# 3️⃣ LOOPING STATEMENTS
# =========================================
# Loops help repeat code multiple times.

# -----------------------------------------
# FOR LOOP — iterate over a sequence
print("For Loop Example:")
for i in range(5):  # 0 to 4
    print("Value of i:", i)

# -----------------------------------------
# WHILE LOOP — repeat until condition false
print("\nWhile Loop Example:")
count = 1
while count <= 5:
    print("Count =", count)
    count += 1  # increment by 1

print("-" * 60)


# =========================================
# 4️⃣ LOOP CONTROL STATEMENTS
# =========================================

# 🔹 break → exits the loop immediately
print("Break Example:")
for i in range(1, 10):
    if i == 5:
        break  # stop loop when i=5
    print(i, end=" ")
print("\nLoop stopped using break")

# 🔹 continue → skips the current iteration
print("\nContinue Example:")
for i in range(1, 10):
    if i == 5:
        continue  # skip 5
    print(i, end=" ")
print("\nLoop skipped value 5")

# 🔹 pass → does nothing (placeholder)
print("\nPass Example:")
for i in range(1, 6):
    if i == 3:
        pass  # future code placeholder
    print("Number:", i)

print("-" * 60)


# =========================================
# 5️⃣ NESTED LOOPS
# =========================================
print("Nested Loop Example:")
for i in range(1, 4):       # Outer loop
    for j in range(1, 4):   # Inner loop
        print(f"i={i}, j={j}")
print("-" * 60)


# =========================================
# 6️⃣ LOOP WITH ELSE
# =========================================
# The else block in a loop executes only when the loop completes fully (no break)
print("Loop with Else Example:")
for i in range(1, 6):
    print(i, end=" ")
else:
    print("\nLoop completed successfully!")

print("-" * 60)


# =========================================
# 7️⃣ MINI PRACTICE TASKS
# =========================================

# Task 1: Find if a number is even or odd
num = int(input("Enter a number to check even/odd: "))
if num % 2 == 0:
    print(f"{num} is Even")
else:
    print(f"{num} is Odd")

# Task 2: Print numbers 1 to 10 but skip 5
for i in range(1, 11):
    if i == 5:
        continue
    print(i, end=" ")
print("\n")

# Task 3: Print sum of first 5 natural numbers using while loop
sum_n = 0
i = 1
while i <= 5:
    sum_n += i
    i += 1
print("Sum of first 5 natural numbers =", sum_n)

print("-" * 60)


# =========================================
# ✅ SUMMARY OUTPUT
# =========================================
print("✅ All Control Statement examples executed successfully!")
