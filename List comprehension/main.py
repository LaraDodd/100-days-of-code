# For Loop
numbers = [1, 2, 3]
new_list = []
for n in numbers:
    add_1 = n + 1
    new_list.append(add_1)

# List Comprehension
new_list = [n + 1 for n in numbers]

# String as List
name = "Lara"
letters_list = [letter for letter in name]

# Range as List
range_list = [n * 2 for n in range(1, 5)]

# Conditional List Comprenhension
names = ["Alex", "Beth", "Caroline", "Dave", "Elanor", "Freddie"]
short_names = [name for name in names if len(name) < 5]

upper_case_names = [name.upper() for name in names if len(name) > 4]

# conditional 2
#get data
with open("file1.txt", "r") as f1:
    numbers1 = f1.readlines()

with open("file2.txt", "r") as f2:
    numbers2 = f2.readlines()

#clean data
numbers1_cleaned = [int(num) for num in numbers1]
# print(numbers1_cleaned)
numbers2_cleaned = [int(num) for num in numbers2]
# print(numbers2_cleaned)

result = [num for num in numbers1_cleaned if num in numbers2_cleaned]
print(result)

# Dictionary Comprehension
import random

student_grades = {name: random.randint(1, 100) for name in names}
print(student_grades)

passed_students = {
    student: grade
    for (student, grade) in student_grades.items() if grade >= 60
}
print(passed_students)
