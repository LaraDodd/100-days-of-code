# -*- coding: utf-8 -*-
"""
Created on Tue Nov 29 17:24:17 2022

@author: larad
"""

import random

queen = '''
 ,adPPYb,d8 88       88  ,adPPYba,  ,adPPYba, 8b,dPPYba,   
a8"    `Y88 88       88 a8P_____88 a8P_____88 88P'   `"8a  
8b       88 88       88 8PP""""""" 8PP""""""" 88       88  
"8a    ,d88 "8a,   ,a88 "8b,   ,aa "8b,   ,aa 88       88  
 `"YbbdP'88  `"YbbdP'Y8  `"Ybbd8"'  `"Ybbd8"' 88       88  
         88                                                
         88                                                
'''

rock = '''
    _______
---'   ____)
      (_____)
      (_____)
      (____)
---.__(___)
'''

paper = '''
    _______
---'   ____)____
          ______)
          _______)
         _______)
---.__________)
'''

scissors = '''
    _______
---'   ____)____
          ______)
       __________)
      (____)
---.__(___)
'''

#Write your code below this line 👇

print("What do you choose? Enter 0 for rock, 1 for paper, or 2 for scissors")
choice = input("0, 1 or 2? ")

if choice == "fiyah":
  print("You are a legend and you will win every time! <3")
elif int(choice) == 0:
  print(f"You chose rock {rock}")
elif int(choice) == 1: 
  print(f"You chose paper {paper}")
elif int(choice) == 2:
  print(f"You chose scissors {scissors}")
else:
  print("Invalid inout... try typing fiyah")

computer_choice = random.randint(0,2)



if computer_choice == 0:
  print(f"Computer chose:\n{rock}")
elif computer_choice == 1: 
  print(f"Computer chose:\n{paper}")
else:
  print(f"Computer chose:\n{scissors}")

if choice == "fiyah":
  print(f"YAAAAAAAAAAAAAAAAAS {queen}")
elif int(choice) < 0 or int(choice) > 2:
  print("Typed in invalid number... you lose!")
elif int(choice) == computer_choice:
  print("draw")
elif computer_choice - int(choice) == 1: 
  print(" you lose :(")
else: 
  print("WIN!!")