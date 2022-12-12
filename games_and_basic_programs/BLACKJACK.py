import random 
#from art import logo

def deal():
  '''randomly chooses a card from the pack'''
  cards = [11, 2, 3, 4, 5, 6, 7, 8, 9, 10, 10, 10, 10]
  #cards = [11, 10]
  return random.choice(cards)

def add(list):
  '''adds up items in a list'''
  sum_cards = 0
  for card in list:
    sum_cards += card
  return sum_cards

def blackjack():
  should_continue = True 
  draw = False

  play = input("Do you wanna play?")

  if play == "y":
    #print(logo)
    
    user_cards = []
    for i in range(2):
      user_cards.append(deal())
    
    computer_cards = []
    for i in range(2):
      computer_cards.append(deal())

    user_score = add(user_cards)
    computer_score = add(computer_cards)

    #print(f"user {user_cards} {user_score}")
    #print(f"comp {computer_cards} {computer_score}")


  elif play =="n":
    should_continue == False
    blackjack()
  
  while should_continue:
    print(f"user {user_cards} {user_score}")
    print(f"comp {computer_cards} {computer_score}")
    
    if user_score == 21:#win if user gets 21
      win = True
      print("BLACKJACK")
  
    if computer_score == 21:#losr if comp gets 21
      win = False
      print("BLACKJACK")
  
    if user_score > 21: #if user score over 21... lose
      should_continue = False
      win = False
      
      if 11 in user_cards: #unless ace 
        
        if (user_score - 10) > 21: #except if ace is 1 and score still greater than 21
          win = False
          should_continue = False
          
        else:
          user_cards.remove(11)
          user_cards.append(1) # replace 11 with 1
          print("ace used as 1!")
          user_score = add(user_cards)
          print(f"new user score {user_cards} {user_score}")
          should_continue = True
      
      else:
        win = False
        should_contiue = False
           
    if should_continue:
      another_card = input("Want another card? ")
  
      if another_card == "y":
        user_cards.append(deal()) #assign another card to user and calculate new score
        user_score = add(user_cards)
        #print(f"user {user_cards} {user_score}")
        #print(f"comp {computer_cards} {computer_score}")
      
      elif another_card == "n":
        should_continue = False
      
  #calculating computer cards
  while computer_score < 17:
    computer_cards.append(deal())
    computer_score = add(computer_cards)
    
  print(f"user {user_cards} {user_score}")
  print(f"comp {computer_cards} {computer_score}")

  #calculating result
  if computer_score > 21 and user_score > 21:
    win = False
    print("both lose")
    
  elif user_score > 21:
    win = False 
    
  elif computer_score > 21:
    win = True

  elif computer_score == user_score: 
    draw = True
    
  elif user_score > computer_score:
    win = True
    
  else: 
    win = False
    
  #printing result
  if draw:
    print("draw")
    blackjack()
  elif win:
    print("win")
    blackjack()
  elif not win: 
    print("lose")
    blackjack()

should_continue = True 
blackjack()
  
        
        
        
      
        
      
  




  

  
  