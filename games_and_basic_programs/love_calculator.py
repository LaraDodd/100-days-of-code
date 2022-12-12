# -*- coding: utf-8 -*-
"""
Created on Mon Nov 28 23:01:40 2022

@author: larad
"""

# 🚨 Don't change the code below 👇
print("Welcome to the Love Calculator!")
name1 = input("What is your name? \n")
name2 = input("What is their name? \n")
# 🚨 Don't change the code above 👆

#Write your code below this line 👇


true_counter = 0
true_chars = ["t","r","u","e"]
love_counter = 0
love_chars = ["l","o","v","e"]
names = (name1+name2)
names = names.lower().strip(" ")



for i in names: 
    for a in true_chars:
        if i == a: 
            true_counter += 1
    for b in love_chars:
        if i == b: 
            love_counter += 1



score = int(str(true_counter)+str(love_counter))


if score < 10 or score > 90: 
    print(f"Your score is {score}, you go together like coke and mentos.")
elif score < 50 and score > 40: 
    print(f"Your score is {score}, you are alright together")
else: 
    print(f"Your score is {score}.")

