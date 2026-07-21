# ==========================================
# Basic ML/AI Concepts in Python
# Author: Kainat Fatima
# ==========================================

# -----------------------------
# 1. Variables and Data Types
# -----------------------------
name = "Aliya Zainab"
age = 21
cgpa = 3.75
is_intern = True

print("===== VARIABLES & DATA TYPES =====")
print("Name:", name)
print("Age:", age)
print("CGPA:", cgpa)
print("Intern:", is_intern)

# -----------------------------
# 2. Conditional Statements
# -----------------------------
print("\n===== CONDITIONAL STATEMENTS =====")

if cgpa >= 3.5:
    print("Excellent Academic Performance")
elif cgpa >= 3.0:
    print("Good Academic Performance")
else:
    print("Needs Improvement")

# -----------------------------
# 3. Loops
# -----------------------------
print("\n===== FOR LOOP =====")

for i in range(1, 6):
    print("Iteration:", i)

print("\n===== WHILE LOOP =====")

count = 1
while count <= 3:
    print("Count:", count)
    count += 1

# -----------------------------
# 4. Functions
# -----------------------------
print("\n===== FUNCTIONS =====")

def calculate_square(number):
    return number * number

result = calculate_square(8)
print("Square of 8 =", result)

# -----------------------------
# 5. List Comprehension
# -----------------------------
print("\n===== LIST COMPREHENSION =====")

numbers = [1, 2, 3, 4, 5]

squares = [num ** 2 for num in numbers]

print("Numbers :", numbers)
print("Squares :", squares)

# -----------------------------
# 6. Dictionary Comprehension
# -----------------------------
print("\n===== DICTIONARY COMPREHENSION =====")

square_dictionary = {num: num ** 2 for num in numbers}

print(square_dictionary)

# -----------------------------
# 7. Exception Handling
# -----------------------------
print("\n===== EXCEPTION HANDLING =====")

try:
    a = 20
    b = 5
    print("Division =", a / b)

except ZeroDivisionError:
    print("Cannot divide by zero.")

except Exception as e:
    print("Error:", e)

finally:
    print("Exception Handling Completed Successfully.")

# -----------------------------
# 8. File Handling
# -----------------------------
print("\n===== FILE HANDLING =====")

with open("student.txt", "w") as file:
    file.write("Name: Aliya Zainab \n")
    file.write("Department: Artificial Intelligence\n")
    file.write("Course: basic ML/AI Concepts\n")

with open("student.txt", "r") as file:
    content = file.read()

print(content)

# -----------------------------
# 9. Classes and Objects
# -----------------------------
print("\n===== CLASSES & OBJECTS =====")

class Student:

    def __init__(self, name, department):
        self.name = name
        self.department = department

    def display(self):
        print("Student Name :", self.name)
        print("Department   :", self.department)

student1 = Student("Aliya Zainab", "Artificial Intelligence")
student1.display()

# -----------------------------
# 10. Modules and Packages
# -----------------------------
print("\n===== MODULES & PACKAGES =====")

import math
import random

print("Square Root of 81 =", math.sqrt(81))
print("Random Number =", random.randint(1, 100))

print("\n=================================")
print("All Required Python Concepts Executed Successfully!")
print("=================================")
