# 🧠 Python Operators — Full Practice File
# Author: Anshumaan Sharma
# Topic: Operators in Python (All Types)
# Operators are symbols or keywords that perform operations on values or variables.

# =========================================
# 1️⃣ Arithmetic Operators
# =========================================
a = 10
b = 3

print("Arithmetic Operators:")
print("Addition:", a + b)       # 13
print("Subtraction:", a - b)    # 7
print("Multiplication:", a * b) # 30
print("Division:", a / b)       # 3.333...
print("Floor Division:", a // b)# 3
print("Modulus:", a % b)        # 1
print("Exponent:", a ** b)      # 1000
print("-" * 40)


# =========================================
# 2️⃣ Comparison (Relational) Operators
# =========================================
x = 5
y = 8

print("Comparison Operators:")
print("Equal to:", x == y)       # False
print("Not equal to:", x != y)   # True
print("Greater than:", x > y)    # False
print("Less than:", x < y)       # True
print("Greater or Equal:", x >= 5) # True
print("Less or Equal:", y <= 10)   # True
print("-" * 40)


# =========================================
# 3️⃣ Assignment Operators
# =========================================
num = 10
print("Assignment Operators:")
num += 5  # num = num + 5
print("After += :", num)         # 15
num -= 3
print("After -= :", num)         # 12
num *= 2
print("After *= :", num)         # 24
num /= 4
print("After /= :", num)         # 6.0
num //= 2
print("After //= :", num)        # 3.0
num **= 3
print("After **= :", num)        # 27.0
print("-" * 40)


# =========================================
# 4️⃣ Logical Operators
# =========================================
a, b = 7, 10

print("Logical Operators:")
print("AND:", a > 5 and b < 12)  # True
print("OR :", a < 5 or b == 10)  # True
print("NOT:", not(a == 7))       # False
print("-" * 40)


# =========================================
# 5️⃣ Bitwise Operators
# =========================================
p = 5  # binary: 0101
q = 3  # binary: 0011

print("Bitwise Operators:")
print("AND (&):", p & q)   # 1 (0001)
print("OR (|):", p | q)    # 7 (0111)
print("XOR (^):", p ^ q)   # 6 (0110)
print("NOT (~):", ~p)      # -6
print("Left Shift (<<):", p << 1)  # 10
print("Right Shift (>>):", p >> 1) # 2
print("-" * 40)


# =========================================
# 6️⃣ Membership Operators
# =========================================
fruits = ["apple", "banana", "cherry"]

print("Membership Operators:")
print("'apple' in fruits:", "apple" in fruits)       # True
print("'grapes' not in fruits:", "grapes" not in fruits) # True
print("-" * 40)


# =========================================
# 7️⃣ Identity Operators
# =========================================
x = [1, 2, 3]
y = x       # Same object
z = [1, 2, 3] # Different object, same content

print("Identity Operators:")
print("x is y:", x is y)         # True
print("x is z:", x is z)         # False
print("x is not z:", x is not z) # True
print("-" * 40)


# =========================================
# ✅ Summary Output
# =========================================
print("✅ All operators executed successfully!")
