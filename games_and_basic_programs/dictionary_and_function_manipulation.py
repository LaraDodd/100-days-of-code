# -*- coding: utf-8 -*-
"""
Created on Fri Dec  2 13:22:41 2022

@author: larad
"""

student_scores = {
  "Harry": 81,
  "Ron": 78,
  "Hermione": 99, 
  "Draco": 74,
  "Neville": 62,
}

student_grades = {}

def grade_calculator(score):
    global grade
    if score > 90:
       grade = "Outstanding"
    elif score > 80: 
       grade = "Exceeds Expectations"
    elif score > 70: 
       grade = "Acceptable"
    else: 
       grade = "Fail"


for key in student_scores:
    (grade_calculator(student_scores[key]))
    student_grades[key] = grade 

print(student_grades)