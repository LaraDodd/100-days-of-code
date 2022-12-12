# -*- coding: utf-8 -*-
"""
Created on Tue Dec  6 13:39:21 2022

@author: larad
"""

import random
#from may import may_is

#initial conditions
EASY_LIVES = 10
HARD_LIVES = 5
is_game_over = False

def decrease_life():
  '''decreases number of lives by 1 every time it is called'''
  return lives-1

def check_correct(user_input):
  '''checks if guess is correct, if it is then returns 0, else it returns 1, prints a hint'''
  if user_input == COMPUTER_CHOICE:
    print("YOU WIN")
    print(f"{user_input} was the correct answer!")
    return 0

  elif user_input > COMPUTER_CHOICE:
    print("value is lower than this")
    return 1

  elif user_input < COMPUTER_CHOICE:
    print("value higher than this")
    return 1

def assign_lives(user_input):
  '''returns number of lives based on a difficulty input'''
  if user_input == "easy":
    return EASY_LIVES
  elif user_input == "hard":
    return HARD_LIVES
  
#welcome    
print("Welcome to the umber guesser game!!")
#print(may_is)

#assigning lives based on the chosen difficulty
difficulty = input("choose difficulty, type 'easy' or 'hard'? ")
lives = assign_lives(difficulty)


#create list 1 to 100
numbers = []
for i in range(1,101,1):
  numbers.append(i)

#choose random integer
COMPUTER_CHOICE = random.choice(numbers)


while not is_game_over and lives > 0:
  
  print("\n")
  user_guess = int(input("guess a number "))
  print("\n")
  
  if check_correct(user_guess) == 0:
    is_game_over = True
  else:
    lives = decrease_life()
    
  if not is_game_over:
    if lives > 0:
      print(f"lives left {lives}. Guess again")
    else:
      print("you lose")
      print(f"The answer was {COMPUTER_CHOICE}")




  
  



































