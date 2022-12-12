# -*- coding: utf-8 -*-
"""
Created on Mon Dec  5 12:53:50 2022

@author: larad
"""

import random

def blackjack(): 
  play = input("Do you want to play a game of blackjack? 'y' or 'n' ")
  
  if play == "y":
    user_wants_to_play = True
  elif play =="n":
    user_wants_to_play = False
  
  #initial conditions 
  card_numbers = [11, 2, 3, 4, 5, 6, 7, 8, 9, 10, 10, 10, 10]
  cards = ["A", "2", "3", "4", "5", "6", "7", "8", "9", "10", "J", "Q", "K"]
  
  def deal(num): 
    '''randomly deals cards from a list, the input num = the number of cards dealt'''
  
    chosen_cards = {"card numbers": 0,
                   "cards": 0}
    card_number_list = []
    card_list = []
    
    for i in range(num):
      rand_index = random.randint(0,len(card_numbers)-1)
      card_number_list.append(card_numbers[rand_index])
      card_list.append(cards[rand_index])
  
    chosen_cards["card numbers"] = card_number_list
    chosen_cards["cards"] = card_list
  
    return chosen_cards

  def add(list):
    sum_cards = 0
    for card in range(len(list)):
        sum_cards += int(card)
    return sum_cards
        
    
  
  while user_wants_to_play:
  
    user_cards = deal(2)
    
    computer_cards = deal(2)
  
    should_continue = True 
  
    while should_continue:
        
        
        user_score = (add(user_cards["card numbers"]))
        computer_score = (add(computer_cards["card numbers"]))

        print(f"You were dealt {user_cards['cards']} your score is {user_score}")
        print(f"computer score is {computer_score}")
        
        print(type(user_score))
        
blackjack()

'''
        if user_score == 21: 
            print("win")
            win = True
            user_wants_to_play = False
        
        if computer_score == 21: 
            print("lose")
            win = False
            user_wants_to_play = False
        
        if (user_score) > 21: 
            if 11 in user_cards["card_numbers"]:
                if (user_score - 10) > 21: 
                    print("lose")
                    win = False
                    user_wants_to_play = False
                else: 
                    user_cards["card_numbers"].remove(11)
                    user_cards["card_numbers"].append(1)
            else: 
                print("lose")
                user_wants_to_play = False
                win = False
                
        if computer_score > 21: 
            if 11 in computer_cards["card_numbers"]:
                if (computer_score - 10) > 21: 
                    print("lose")
                    win = False
                    user_wants_to_play = False
                else: 
                    computer_cards["card_numbers"].remove(11)
                    computer_cards["card_numbers"].append(1)
            else: 
                print("lose")
                win = False
                user_wants_to_play = False
        
        if user_score > computer_score: 
            win = True
        elif user_score == computer_score: 
            draw = True
        elif user_score < computer_score:
            win = False
        
        another_card = input("Do you want to be dealt another card? ")
        
        if another_card == "y" and user_score <= 21:
            rand_index = random.randint(0,len(card_numbers)-1)
            user_cards["card_numbers"].append(card_numbers[rand_index])
            user_cards["cards"].append(cards[rand_index])
            
      
            should_continue = True
            
        else:
            if computer_score < 17:
                rand_index = random.randint(0,len(card_numbers)-1)
                computer_cards["card_numbers"].append(card_numbers[rand_index])
                computer_cards["cards"].append(cards[rand_index])
                should_continue = True
            
            else:
                should_continue = False

    if draw:
        print("draw")
    elif win:
        print("win")
    else:
        print("lose")
            
            

blackjack()'''
    
  
  




























############### Blackjack Project #####################

#Difficulty Normal 😎: Use all Hints below to complete the project.
#Difficulty Hard 🤔: Use only Hints 1, 2, 3 to complete the project.
#Difficulty Extra Hard 😭: Only use Hints 1 & 2 to complete the project.
#Difficulty Expert 🤯: Only use Hint 1 to complete the project.

############### Our Blackjack House Rules #####################

## The deck is unlimited in size. 
## There are no jokers. 
## The Jack/Queen/King all count as 10.
## The the Ace can count as 11 or 1.
## Use the following list as the deck of cards:
## cards = [11, 2, 3, 4, 5, 6, 7, 8, 9, 10, 10, 10, 10]
## The cards in the list have equal probability of being drawn.
## Cards are not removed from the deck as they are drawn.
## The computer is the dealer.

##################### Hints #####################

#Hint 1: Go to this website and try out the Blackjack game: 
#   https://games.washingtonpost.com/games/blackjack/
#Then try out the completed Blackjack project here: 
#   http://blackjack-final.appbrewery.repl.run

#Hint 2: Read this breakdown of program requirements: 
#   http://listmoz.com/view/6h34DJpvJBFVRlZfJvxF
#Then try to create your own flowchart for the program.

#Hint 3: Download and read this flow chart I've created: 
#   https://drive.google.com/uc?export=download&id=1rDkiHCrhaf9eX7u7yjM1qwSuyEk-rPnt

#Hint 4: Create a deal_card() function that uses the List below to *return* a random card.
#11 is the Ace.
#cards = [11, 2, 3, 4, 5, 6, 7, 8, 9, 10, 10, 10, 10]

#Hint 5: Deal the user and computer 2 cards each using deal_card() and append().
#user_cards = []
#computer_cards = []

#Hint 6: Create a function called calculate_score() that takes a List of cards as input 
#and returns the score. 
#Look up the sum() function to help you do this.

#Hint 7: Inside calculate_score() check for a blackjack (a hand with only 2 cards: ace + 10) and return 0 instead of the actual score. 0 will represent a blackjack in our game.

#Hint 8: Inside calculate_score() check for an 11 (ace). If the score is already over 21, remove the 11 and replace it with a 1. You might need to look up append() and remove().

#Hint 9: Call calculate_score(). If the computer or the user has a blackjack (0) or if the user's score is over 21, then the game ends.

#Hint 10: If the game has not ended, ask the user if they want to draw another card. If yes, then use the deal_card() function to add another card to the user_cards List. If no, then the game has ended.

#Hint 11: The score will need to be rechecked with every new card drawn and the checks in Hint 9 need to be repeated until the game ends.

#Hint 12: Once the user is done, it's time to let the computer play. The computer should keep drawing cards as long as it has a score less than 17.

#Hint 13: Create a function called compare() and pass in the user_score and computer_score. If the computer and user both have the same score, then it's a draw. If the computer has a blackjack (0), then the user loses. If the user has a blackjack (0), then the user wins. If the user_score is over 21, then the user loses. If the computer_score is over 21, then the computer loses. If none of the above, then the player with the highest score wins.

#Hint 14: Ask the user if they want to restart the game. If they answer yes, clear the console and start a new game of blackjack and show the logo from art.py.

