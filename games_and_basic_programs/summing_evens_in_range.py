# -*- coding: utf-8 -*-
"""
Created on Tue Nov 29 18:11:08 2022

@author: larad
"""

#Write your code below this row 👇
even_list = []

#make list of all evens between 1 and 100
for i in range(101):
    if i%2 == 0:
        even_list.append(i)
sum_evens = 0 

for num in even_list:
    sum_evens += num

print(sum_evens)


''' or do it this way...'''
total = 0
for a in range(2,101,2):
    total += a
print(total)

