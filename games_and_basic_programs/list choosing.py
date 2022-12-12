# -*- coding: utf-8 -*-
"""
Created on Tue Nov 29 10:47:15 2022

@author: larad
"""

# Import the random module here
import random

# Split string method
names_string = input("Give me everybody's names, separated by a comma. ")
#names_string = "Jake, Sally, Sarah, Guiya, Lia, John"
names = names_string.split(", ")
# 🚨 Don't change the code above 👆

#Write your code below this line 👇

random_number = random.randint(0,len(names))
print(random_number)
chosen_name = names[random_number]

print(f"{chosen_name} is going to buy the meal today!")
