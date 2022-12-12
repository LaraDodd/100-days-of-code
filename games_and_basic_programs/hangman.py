# -*- coding: utf-8 -*-
"""
Created on Thu Dec  1 09:46:31 2022

@author: larad
"""
# Establish a list of words that can be chosen for the game
with open("words.txt") as f:
    word_list = f.read().splitlines()


'''random_word = "hangman"
guess_word = []
hangman_steps_left = 8

def draw_hangman():
    if hangman_steps_left == 7:
        print("leg")
    elif hangman_steps_left == 6:
        print("leg, leg")
    elif hangman_steps_left == 5:
        print("leg, leg, body")  
    elif hangman_steps_left == 4:
        print("leg, leg, body, arm")  
    elif hangman_steps_left == 3:
        print("leg, leg, body, arm, arm")
    elif hangman_steps_left == 2:
        print("leg, leg, body, arm, arm, head")    
    elif hangman_steps_left == 1:
        print("leg, leg, body, arm, arm, head, noose") 
    elif hangman_steps_left == 0:
        print("GAME OVER") 
        

for i in range(len(random_word)):
    guess_word +=("_")
print(guess_word)

guess_word_str = ' '.join(guess_word)
print(guess_word_str)

if hangman_steps_left > 0:
    while "_" in guess_word:
        guess_letter = input("Guess a letter ")
        
        for a in range(len(random_word)):
                       
            if random_word[a] == guess_letter:
                guess_word[a] = guess_letter
                win = True
                  
        
        if win == False:
            print("wrong guess")
            hangman_steps_left -= 1
            print(hangman_steps_left)
            draw_hangman()
        
        print(guess_word)'''
        
            
        

    