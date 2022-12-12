# -*- coding: utf-8 -*-
"""
Created on Mon Nov 28 22:14:33 2022

@author: larad
"""

# 🚨 Don't change the code below 👇
year = int(input("Which year do you want to check? "))
# 🚨 Don't change the code above 👆

#Write your code below this line 👇


if year%4 == 0:
    if year%100 == 0 and year%400 == 0:
        leap_year = True
        print("Leap year") 
    elif year%100 == 0 and year%400 != 0:
        leap_year = False
        print("Not a leap year")
    else: 
        leap_year = True
        print("Leap year")
else:
    leap_year = False
    print("Not a leap year")


    
    



