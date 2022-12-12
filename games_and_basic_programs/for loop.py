# -*- coding: utf-8 -*-
"""
Created on Tue Nov 29 17:44:29 2022

@author: larad
"""

# 🚨 Don't change the code below 👇
student_heights = input("Input a list of student heights (cm) ")
if "," in student_heights: 
    student_heights = student_heights.split(",")
else:
    student_heights = student_heights.split()

for n in range(0, len(student_heights)):
  student_heights[n] = int(student_heights[n])
# 🚨 Don't change the code above 👆


#Write your code below this row 👇
sum_of_heights = 0

for height in student_heights:
    sum_of_heights += height


average_height = round(sum_of_heights/len(student_heights))
print(f"average height: {average_height}")




