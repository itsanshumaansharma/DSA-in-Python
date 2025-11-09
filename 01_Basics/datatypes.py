# 🧠 Python Data Types — Full Practice File
# Author: Anshumaan Sharma
# Topic: Data Types & Type Conversion
# Data types define what kind of data a variable holds and what operations can be done on it.

# =========================================
# 1️⃣ Basic Data Types in Python
# =========================================

# Integers (int)
a = 10
print("Integer:", a, "| Type:", type(a))  # int

# Float
b = 10.5
print("Float:", b, "| Type:", type(b))    # float

# String
c = "Anshumaan"
print("String:", c, "| Type:", type(c))   # str

# Boolean
d = True
print("Boolean:", d, "| Type:", type(d))  # bool

# NoneType
e = None
print("NoneType:", e, "| Type:", type(e)) # NoneType

print("-" * 50)


# =========================================
# 2️⃣ Sequence Data Types
# =========================================

# List → Mutable (changeable)
fruits = ["apple", "banana", "cherry"]
print("List:", fruits, "| Type:", type(fruits))
fruits[1] = "grapes"  # modifying list
print("Modified List:", fruits)

# Tuple → Immutable (unchangeable)
colors = ("red", "green", "blue")
print("Tuple:", colors, "| Type:", type(colors))
# colors[0] = "yellow" ❌ (This will cause an error)

# Range
nums = range(5)
print("Range:", list(nums), "| Type:", type(nums))

# String → Sequence of characters
name = "Python"
print("String (sequence):", name[0], name[-1])  # P, n
print("-" * 50)


# =========================================
# 3️⃣ Set Data Type
# =========================================

# Set → Unordered, no duplicates
numbers = {1, 2, 3, 3, 4}
print("Set:", numbers, "| Type:", type(numbers))

numbers.add(5)
numbers.remove(2)
print("Updated Set:", numbers)
print("-" * 50)


# =========================================
# 4️⃣ Dictionary Data Type
# =========================================

# Dictionary → Key-Value pairs
student = {
    "name": "Anshumaan",
    "age": 22,
    "course": "MCA"
}
print("Dictionary:", student, "| Type:", type(student))
print("Access value:", student["name"])

# Modify dictionary
student["age"] = 23
student["college"] = "Galgotias University"
print("Updated Dictionary:", student)
print("-" * 50)


# =========================================
# 5️⃣ Type Conversion (Casting)
# =========================================

# int → float
x = 10
y = float(x)
print("int to float:", y, "| Type:", type(y))

# float → int
z = int(9.8)
print("float to int:", z, "| Type:", type(z))

# string → int
s = "50"
num = int(s)
print("string to int:", num, "| Type:", type(num))

# int → string
a = 100
text = str(a)
print("int to string:", text, "| Type:", type(text))
print("-" * 50)


# =========================================
# 6️⃣ Checking Data Type Dynamically
# =========================================
value = [1, 2, 3]
if type(value) == list:
    print("✅ value is a list")

# Another way (recommended)
if isinstance(value, list):
    print("✅ Checked using isinstance()")
print("-" * 50)


# =========================================
# 7️⃣ Complex Numbers (Extra)
# =========================================
comp = 3 + 5j
print("Complex Number:", comp, "| Type:", type(comp))
print("Real part:", comp.real)
print("Imaginary part:", comp.imag)
print("-" * 50)


# =========================================
# ✅ Summary Output
# =========================================
print("✅ All Data Type examples executed successfully!")
