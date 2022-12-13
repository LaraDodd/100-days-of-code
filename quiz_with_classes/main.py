from question_model import QuestionMaker
from data import question_data
import random

#  initialise empty list
question_object_list = []

#  iterates through each dictionary in the list, creates a question object containing text and answer
#  adds the question object to a list
for question in question_data:
    question_object = QuestionMaker(question["text"], question["answer"])
    question_object_list.append(question_object)

play_again = True

while play_again:
    question_choice = random.choice(question_object_list)  # chooses a random question object in list

    print(question_choice.text)
    user_answer = input("Answer True or False? ").lower()

    if user_answer == question_choice.answer.lower():
        print("Well done that is correct!")
    else:
        print("Wrong... better luck next time")

    ask_user_to_cont = input("Do you wanna go again? y or n? ")

    if ask_user_to_cont == "n":
        play_again = False
