"""
Python to AI Bootcamp - Day 1 Practice
GDG CUI Wah Campus
Covers: variables, operators, control flow, strings, data structures,
functions and the Student Marks Analyzer mini-project.
"""

# ---------------------------------------------------------------
# 1. VARIABLES & DATA TYPES
# ---------------------------------------------------------------
print("=== 1. Variables & Data Types ===")
age = 21                 # int
gpa = 3.45               # float
name = "Ayesha"          # str
is_student = True        # bool
nothing = None           # NoneType

for v in (age, gpa, name, is_student, nothing):
    print(f"{v!r:10} -> {type(v).__name__}")

# Type conversion (input() always returns str)
# Using a simulated input so the script runs without stopping.
# Replace with: raw = input("Enter your age: ")
raw = "25"
age_next_year = int(raw) + 1
print("Next year age:", age_next_year)
print("float('3.14') =", float("3.14"), "| str(100) =", str(100) + "!", "| bool(0) =", bool(0))

# ---------------------------------------------------------------
# 2. OPERATORS
# ---------------------------------------------------------------
print("\n=== 2. Operators ===")
a, b = 17, 5
print("a + b =", a + b, "| a - b =", a - b, "| a * b =", a * b, "| a / b =", a / b)
print("a // b =", a // b, "(floor division)")
print("a % b  =", a % b, "(remainder)")
print("a ** b =", a ** b, "(power)")

print("a > b:", a > b, "| a == b:", a == b, "| a != b:", a != b)
print("a > 10 and b < 10:", a > 10 and b < 10)
print("a < 10 or b < 10:", a < 10 or b < 10)
print("not (a > b):", not (a > b))

fruits = ["apple", "banana", "mango"]
print("'apple' in fruits:", "apple" in fruits)       # membership
print("'kiwi' not in fruits:", "kiwi" not in fruits)

x = [1, 2]
y = [1, 2]
z = x
print("x == y:", x == y, "| x is y:", x is y, "| x is z:", x is z)  # identity
print("value is None:", nothing is None)

# Edge cases
print("-17 // 5 =", -17 // 5, "| -17 % 5 =", -17 % 5)
print("0.1 + 0.2 =", 0.1 + 0.2, "(floating point!)")

# ---------------------------------------------------------------
# 3. CONTROL FLOW
# ---------------------------------------------------------------
print("\n=== 3. Control Flow ===")


def grade(marks):
    if marks >= 90:
        return "A+"
    elif marks >= 80:
        return "A"
    elif marks >= 70:
        return "B"
    elif marks >= 60:
        return "C"
    else:
        return "Fail"


for m in (95, 82, 71, 64, 30):
    print(m, "->", grade(m))

print("\nfor loop with range(1, 11, 2):", list(range(1, 11, 2)))
for i in range(1, 6):
    if i == 3:
        continue          # skip 3
    if i == 5:
        break             # stop at 5
    print("i =", i)

count = 3
while count > 0:
    print("Countdown:", count)
    count -= 1
print("Liftoff!")

# Multiplication table
n = 7
for i in range(1, 6):
    print(f"{n} x {i} = {n * i}")

# ---------------------------------------------------------------
# 4. STRINGS
# ---------------------------------------------------------------
print("\n=== 4. Strings ===")
s = "   python to ai bootcamp   "
print("strip():", repr(s.strip()))
clean = s.strip()
print("title():", clean.title())
print("upper():", clean.upper())
print("split():", clean.split())
print("replace():", clean.replace("python", "Python"))
print("Indexing: first =", clean[0], "| last =", clean[-1])
print("Slicing: clean[:6] =", clean[:6], "| clean[-8:] =", clean[-8:], "| reversed =", clean[::-1])
print("Length:", len(clean), "| count of 'o':", clean.count("o"))
print("startswith('py'):", clean.startswith("py"))

# ---------------------------------------------------------------
# 5. DATA STRUCTURES
# ---------------------------------------------------------------
print("\n=== 5. Data Structures ===")

# List (mutable, ordered)
nums = [5, 3, 8, 1]
nums.append(10)
nums.insert(0, 99)
nums.remove(3)
nums.sort()
print("List:", nums, "| pop():", nums.pop(), "| now:", nums)

# Tuple (immutable)
point = (10, 20)
px, py = point                    # unpacking
print("Tuple:", point, "| x =", px, "| y =", py)

# Set (unique, unordered)
dupes = [1, 2, 2, 3, 3, 3]
uniq = set(dupes)
print("Set:", uniq)
print("Union:", {1, 2, 3} | {3, 4}, "| Intersection:", {1, 2, 3} & {3, 4},
      "| Difference:", {1, 2, 3} - {3, 4})

# Dictionary (key -> value)
student = {"name": "Ali", "age": 20, "courses": ["Math", "CS"]}
student["gpa"] = 3.7
student["age"] = 21
print("Dict:", student)
print("keys:", list(student.keys()))
print("get missing key:", student.get("email", "not provided"))
for k, v in student.items():
    print(f"  {k}: {v}")

# List comprehension
squares = [i ** 2 for i in range(1, 8) if i % 2 == 1]
print("Odd squares:", squares)

# ---------------------------------------------------------------
# 6. FUNCTIONS
# ---------------------------------------------------------------
print("\n=== 6. Functions ===")


def greet(name, greeting="Hello"):
    """Return a greeting string."""
    return f"{greeting}, {name.title()}!"


def is_even(n):
    return n % 2 == 0


def average(values):
    return sum(values) / len(values) if values else 0


print(greet("sara"))
print(greet("bilal", "Salam"))
print("is_even(10):", is_even(10), "| is_even(7):", is_even(7))
print("average([]):", average([]), "| average([2,4,6]):", average([2, 4, 6]))

# ---------------------------------------------------------------
# 7. MINI-PROJECT: STUDENT MARKS ANALYZER (extended)
# ---------------------------------------------------------------
print("\n=== 7. Student Marks Analyzer ===")


def analyze_marks(marks):
    """marks: dict of {student_name: marks}"""
    if not marks:
        print("No data to analyze.")
        return None

    values = list(marks.values())
    total = sum(values)
    avg = total / len(values)
    highest = max(values)          # extension: max()
    lowest = min(values)           # extension: min()

    top_students = [n for n, m in marks.items() if m == highest]
    low_students = [n for n, m in marks.items() if m == lowest]

    print(f"{'Student':<10}{'Marks':>7}  Grade")
    print("-" * 26)
    for n, m in marks.items():
        print(f"{n:<10}{m:>7}  {grade(m)}")
    print("-" * 26)
    print("Total marks    :", total)
    print("Average marks  :", round(avg, 2))
    print("Highest marks  :", highest, "->", ", ".join(top_students))
    print("Lowest marks   :", lowest, "->", ", ".join(low_students))
    print("Passed         :", sum(1 for v in values if v >= 60), "of", len(values))
    print("Above average  :", [n for n, m in marks.items() if m > avg])

    return {"total": total, "average": avg, "highest": highest, "lowest": lowest}


students = {"Ali": 85, "Sara": 92, "Bilal": 58, "Hina": 76, "Usman": 92}
result = analyze_marks(students)

# Edge case: empty data
analyze_marks({})
