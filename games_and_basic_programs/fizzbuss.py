# -*- coding: utf-8 -*-
"""
Created on Tue Nov 29 18:15:30 2022

@author: larad
"""

#Write your code below this row 👇

for i in range(1,101,1):
    if i%3 == 0 and i%5 == 0:
        print("FizzBuzz")
    elif i%3 == 0:
        print("Fizz")
    elif i%5 == 0:
        print("Buzz")
    else:
        print(i)
