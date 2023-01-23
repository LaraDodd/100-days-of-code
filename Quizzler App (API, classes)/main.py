from question_model import Question
from data import question_data
from quiz_brain import QuizBrain
from tkinter import *
from tkinter import messagebox
from tkinter.simpledialog import askstring
import pandas
import html


def go_blue():
    canvas.config(bg=THEME_COLOR)
    window.config(bg=THEME_COLOR)


def correct():
    canvas.config(bg="green")
    window.config(bg="green")
    canvas.after(200, go_blue)


def incorrect():
    canvas.config(bg="red")
    window.config(bg="red")
    canvas.after(200, go_blue)


def display_q():
    if quiz.still_has_questions():
        q_text = html.unescape(quiz.question_list[quiz.question_number].text)
        canvas.itemconfig(quiz_text, text=f"{quiz.question_number + 1} {q_text}")
        score.config(text=f"{quiz.score}/{quiz.question_number + 1}")
    else:
        canvas.itemconfig(quiz_text, text=f"You've completed the quiz!\nYour final score was: "
                                          f"{quiz.score}/{quiz.question_number}", font=("Ariel", 30, "italic"))
        add_to_leaderboard()
        # window.after(5000, exit)


def true_ticked():
    display_q()
    next_q("true")


def false_ticked():
    display_q()
    next_q("false")


def next_q(answer):
    if quiz.current_question.answer.lower() == answer:
        correct()
    else:
        incorrect()
    quiz.next_question(answer)
    display_q()


# =================UI===========


THEME_COLOR = "#375362"

window = Tk()
window.title("Quizzle")
window.minsize(500, 400)
window.config(padx=20, pady=20, bg=THEME_COLOR)

canvas = Canvas(width=600, height=500, bg=THEME_COLOR, highlightthickness=0)
quiz_bg_img = PhotoImage(file="images/speech.png")
canvas_background = canvas.create_image(300, 263, image=quiz_bg_img)
quiz_text = canvas.create_text(300, 200, text="", font=("Ariel", 20, "italic"), width=350)
canvas.grid(row=1, column=0, columnspan=2)

cross_image = PhotoImage(file="images/false.png")
wrong_button = Button(image=cross_image, highlightthickness=0, command=false_ticked)
wrong_button.config(pady=20, padx=20)
wrong_button.grid(row=2, column=0)

check_image = PhotoImage(file="images/true.png")
right_button = Button(image=check_image, highlightthickness=0, command=true_ticked)
right_button.grid(row=2, column=1)

# ==============MAIN CODE==============
question_bank = []
# iteration through question data, create question object using Question class and append to question bank list
for question in question_data:
    question_text = question["question"]
    question_answer = question["correct_answer"]
    new_question = Question(question_text, question_answer)
    question_bank.append(new_question)

# create quiz object using QuizBrain and pass in list of question objects
quiz = QuizBrain(question_bank)
for q in question_bank:
    print(q.text)

canvas.itemconfig(quiz_text, text=f"{quiz.question_number + 1} {html.unescape(quiz.current_question.text)}")

score = Label(text=f"{quiz.score}/{quiz.question_number}", font=("Ariel", 12), bg=THEME_COLOR)
score.grid(row=0, column=0, columnspan=2)


def add_to_leaderboard():
    name = askstring('Name', 'What is your name?')
    window.after(1000, exit)


    try:
        leaderboard_df = pandas.read_csv("leaderboard.csv", index_col=False)
    except FileNotFoundError:
        first_row = {'Name': [name], 'Score': [quiz.score], }
        leaderboard_df = pandas.DataFrame.from_dict(first_row)
        leaderboard_df.to_csv("leaderboard.csv", index=False)
    else:
        name_list = leaderboard_df.Name.to_list()
        if name not in name_list:
            new_row = {'Name': name, 'Score': quiz.score, }
            leaderboard_df = leaderboard_df.append(new_row, ignore_index=True)
            leaderboard_df.to_csv("leaderboard.csv", index=False)

        else:
            name_row = leaderboard_df[leaderboard_df.Name == name]
            name_score = int(name_row.Score)
            if quiz.score > name_score:
                leaderboard_df.loc[leaderboard_df.Name == name, "Score"] = quiz.score
            leaderboard_df.to_csv("leaderboard.csv", index=False)


window.mainloop()

print("You've completed the quiz")
print(f"Your final score was: {quiz.score}/{quiz.question_number}")
