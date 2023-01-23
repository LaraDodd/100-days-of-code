from question_model import Question
from data import question_data
from quiz_brain import QuizBrain
import time

def go_blue():
    canvas.config(bg=THEME_COLOR)

def true_ticked():
    print("you clicked true")
    next_q("true")

def correct():
    canvas.config(bg="green")
    canvas.after(500, go_blue)

def incorrect():
    canvas.config(bg="red")
    canvas.after(500, go_blue)


def false_ticked():
    next_q("false")


def next_q(answer):
    canvas.config(bg=THEME_COLOR)
    quiz.next_question(answer)
    canvas.itemconfig(quiz_text, text=f"{quiz.question_number} {quiz.current_question.text}")


#=================UI===========
from tkinter import *

THEME_COLOR = "#375362"

window = Tk()
window.title("Quizzle")
window.minsize(500, 500)
window.config(padx=50, pady=50, bg=THEME_COLOR)

canvas = Canvas(width=600, height=526, bg=THEME_COLOR, highlightthickness=0)
quiz_bg_img = PhotoImage(file="images/speech.png")
canvas_background = canvas.create_image(300, 263, image=quiz_bg_img)
quiz_text = canvas.create_text(300, 200, text="question 1", font=("Ariel", 20, "italic"), width=350)
canvas.grid(row=0, column=0, columnspan=2)


cross_image = PhotoImage(file="images/false.png")
wrong_button = Button(image=cross_image, highlightthickness=0, command=false_ticked)
wrong_button.config(pady=20, padx=20)
wrong_button.grid(row=1, column=0)


check_image = PhotoImage(file="images/true.png")
right_button = Button(image=check_image, highlightthickness=0, command=true_ticked)
right_button.grid(row=1, column=1)








question_bank = []
#iteration through question data, create question object using Question class and append to question bank list
for question in question_data:
    question_text = question["question"]
    question_answer = question["correct_answer"]
    new_question = Question(question_text, question_answer)
    question_bank.append(new_question)


#create suiz object using QuizBrain and pass in list of question objects
quiz = QuizBrain(question_bank)

print(f"wqje {question_bank}")

num = 0
while num <5:
    canvas.itemconfig(quiz_text, text=f"1. {question_bank[0].text}")
    num +=1



window.mainloop()

print("You've completed the quiz")
print(f"Your final score was: {quiz.score}/{quiz.question_number}")
