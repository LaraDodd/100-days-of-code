import random
from art import logo, vs
from game_data import data
from replit import clear

def choose_rand_handle():
  #randomly choose user 1 from list
  random_index = random.randint(0, (len(data)-1))
  return data[random_index]

#use dictionary dictation to pull out correct information and print that
def user_info(user):
  '''returns the information about the user, where input is a dictionary'''
  info = f"{user['name']}, a {user['description']}, from the counry of {user['country']}"
  return info

def compare(user1, user2):
  '''Compares followers of user1 and user 2 and returns 'a' for person A higher and 'b' for person B higher'''
  if user1["follower_count"] > user2["follower_count"]:
    return "a"
  elif user1["follower_count"] < user2["follower_count"]:
    return "b"
  else:
    return "c"

def increase_score():
  '''adds a value of 1 to the score every time it is called'''
  return score + 1

#initial conditions
should_continue = True
score = 0
user1 = choose_rand_handle()
#print(user1)

#start while loop
while should_continue:
  #introduce, welcome, art 
  print(logo)
  
  print(f"Person A is: {user_info(user1)}")
  if score > 0:
    print(f"Correct! Your current score is {score}")
  
  #print vs art
  print(vs)

  # repeat above 2 lines for user 2 (so  write a function which does this)
  user2 = choose_rand_handle()
  if user2 == user1:
    user2 = choose_rand_handle()
  print(f"Person B is: {user_info(user2)}")

  #ask user which they think is better?
  player_guess = input("who has more followers A or B? ")

#calculate answer using a compare function which takes two users as inputs and compares their followers. If user 1 > user 2 it returns A, else returns B
  answer = compare(user1, user2)
  
#compare function with inputs of guess and answer. If correct return should_continue = True, else end game.
  if answer == "c":
    print("Same person, retry! ")
  
  elif player_guess.lower() == answer:
    win = True
    score = increase_score()
    
    if answer == "b":
      user1 = user2
    
  else:
    win = False
    should_continue = False
  
  clear()

if win:
  print("correct! ")
  print(f"score is {score} !")
elif not win:
  print("Sorry, that's the wrong answer")
  print(f"Final score was {score}")
  
  
