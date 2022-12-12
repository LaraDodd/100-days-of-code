# -*- coding: utf-8 -*-
"""
Created on Thu Dec  1 10:28:16 2022

@author: larad
"""

# -*- coding: utf-8 -*-
"""
Created on Thu Dec  1 09:46:31 2022

@author: larad

"""
import random

stages = ['''
  +---+
  |   |
  O   |
 /|\  |
 / \  |
      |
=========
''', '''
  +---+
  |   |
  O   |
 /|\  |
 /    |
      |
=========
''', '''
  +---+
  |   |
  O   |
 /|\  |
      |
      |
=========
''', '''
  +---+
  |   |
  O   |
 /|   |
      |
      |
=========''', '''
  +---+
  |   |
  O   |
  |   |
      |
      |
=========
''', '''
  +---+
  |   |
  O   |
      |
      |
      |
=========
''', '''
  +---+
  |   |
      |
      |
      |
      |
=========
''']


word_list = ["ardvark", "baboon", "camel", "friend", "person", "evidence", "love", "peanut butter"]
random_word = random.choice(word_list)
print(f"debuggin cheat, word is {random_word}")
guess_word = []
hangman_steps_left = int(len(stages))

#draws hang man stage depending on how many lives left
def draw_hangman():
    print(stages[hangman_steps_left])
        
#creating _ _ _ _ for number of letters in chosen word
for i in range(len(random_word)):
    guess_word +=("_")

#prints the underscore word as a string, as more readable
guess_word_str = ' '.join(guess_word)
print(guess_word_str)

while hangman_steps_left > 0:
    while "_" in guess_word:
        guess_letter = input("Guess a letter ")
        win = False
        
        for a in range(len(random_word)):
                       
            if random_word[a] == guess_letter:
                guess_word[a] = guess_letter
                win = True
                  
        
        if win == False:
            print("wrong guess")
            hangman_steps_left -= 1
            print(f"guesses left: {hangman_steps_left}")
            draw_hangman()
        
        print(' '.join(guess_word))
    
print("you losr")

        
if hangman_steps_left == 0:
    print("GAME OVER") 
else: 
    print("YOU WIN :)")
        

    