# -*- coding: utf-8 -*-
"""
Created on Thu Dec  1 11:53:55 2022

@author: larad
"""

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
import string

hangman = '''
 _                                             
| |                                            
| |__   __ _ _ __   __ _ _ __ ___   __ _ _ __  
| '_ \ / _` | '_ \ / _` | '_ ` _ \ / _` | '_ \ 
| | | | (_| | | | | (_| | | | | | | (_| | | | |
|_| |_|\__,_|_| |_|\__, |_| |_| |_|\__,_|_| |_|
                    __/ |                      
                   |___/ '''
                   
loser = '''
 ___________.._______
| .__________))______|
| | / /      ||\n
| |/ /       ||\n
| | /        ||.-''.\n
| |/         |/  _  \ \n
| |          ||  `/,|\n
| |          (\\`_.'\n
| |         .-`--'.\n
| |        /Y . . Y\ \n
| |       // |   | \\\n
| |      //  | . |  \\\n
| |     ')   |   |   (`\n
| |          ||'||
| |          || ||
| |          || ||
| |          || ||
| |         / | | \
""""""""""|_`-' `-' |"""|\n
|"|"""""""\ \       '"|"|\n
| |        \ \        | |\n
: :         \ \       : :  \n
. .          `'       . .\n
'''

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
''', '''
  +---+
      |
      |
      |
      |
      |
=========
''', '''
 
      |
      |
      |
      |
      |
=========
''']

# Establish a list of words that can be chosen for the game
with open("words.txt") as f:
    word_list = f.read().splitlines()
#word_list = ["ardvark", "baboon", "camel", "friend", "person", "evidence", "love", "peanut butter"]


#initial conditions
random_word = random.choice(word_list)
guess_word = []
end_of_game = False
alphabet = list(string.ascii_lowercase)
guessed_letters = []

#greet
print("Hello! Welcome to hangman! GOOD LUCK...")
print(hangman)


#calculating lives
difficulty = (input("Choose difficulty level: E, M or H? "))

if difficulty.lower() == "e":
    hangman_steps_left = 9
elif difficulty.lower() == "m":
    hangman_steps_left = 7
else:
    hangman_steps_left = 5

#hangman_steps_left = int(len(stages))
    


#debugging
#print(f"debuggin cheat, word is {random_word}")

#draws hang man stage depending on how many lives left
def draw_hangman():
    print(stages[hangman_steps_left])
    

        
#creating _ _ _ _ for number of letters in chosen word
for i in range(len(random_word)):
    guess_word +=("_")

#prints the underscore word as a string, as more readable
guess_word_str = ' '.join(guess_word)
print(guess_word_str)

while not end_of_game:
    guess_letter = input("Guess a letter ").lower()
    
    #check if already entered letter
    if guess_letter in guessed_letters:
        print(f"You have already tried {guess_letter}")
    else:
        #removes letters from list of letters
        alphabet.remove(guess_letter)
    
    #cycles through each letter of the random word 
    #and compares it to the user's guessed letter    
    for a in range(len(random_word)):
                       
        if random_word[a] == guess_letter:
            guess_word[a] = guess_letter
            if not "_" in guess_word:
                end_of_game = True
                print("You win!!")#if no more _ in word... win
                  
    
    #if letter wrong, life lost and if 0 lives... game over
    if guess_letter not in random_word: 
        print("wrong guess")
        hangman_steps_left -= 1 #lives counter
        if hangman_steps_left == 0:
            end_of_game = True
            print("LOOOOOOOSER! YOU LOSE BIG TIME")
            print(loser)
        else:
            print(f"guesses left: {hangman_steps_left}")
            draw_hangman()
    
    
    #creates list of letters
    guessed_letters.append(guess_letter)
        
    print(' '.join(guess_word))
    #print(f"letters left: {alphabet}")
    print(f"Letters already guessed: {guessed_letters}")
    

        

        

    