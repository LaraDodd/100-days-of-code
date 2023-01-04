"""this program creates a state guessing game, using pandas DataFrames and Turtle"""
import turtle
from turtle import Turtle, Screen
from scoreboard import ScoreBoard
import pandas

# create screen
screen = Screen()
screen.setup(width=800, height=600)
screen.title("State Guessing Game")

# add turtle shape
image = "blank_states_img.gif"
screen.addshape(image)

# create turtle
usa = Turtle()
usa.shape(image)

# read in csv
states_df = pandas.read_csv("50_states.csv")

# states as list
states_to_guess = states_df.state.to_list()

# initialise correct guesses list
correct_guesses = []


def create_turtle(x, y, name):
    new_turtle = Turtle()
    new_turtle.penup()
    new_turtle.hideturtle()
    new_turtle.goto(x, y)
    new_turtle.write(name, align="center", font=("Arial", 10, "bold"))


# create classes
score = ScoreBoard()

while len(states_to_guess) > 0:

    # create pop up window
    user_answer = screen.textinput("Guess", "Please guess a state: ")

    if user_answer in states_to_guess:
        df_row = states_df[states_df.state == user_answer]
        x_cor = int(df_row.x)
        y_cor = int(df_row.y)
        create_turtle(x_cor, y_cor, user_answer)

        states_to_guess.remove(user_answer)
        correct_guesses.append(user_answer)

        score.increase_score()

        print(len(states_to_guess))
    else:
        wrong = Turtle()
        wrong.write("wrong guess", align="center", font=("Arial", 8, "normal"))

screen.exitonclick()
