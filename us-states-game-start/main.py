"""this program creates a state guessing game, using pandas DataFrames and Turtle"""
import turtle
from turtle import Turtle, Screen
from scoreboard import ScoreBoard
import pandas
from IPython.display import display

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

# create classes
score = ScoreBoard()

def create_turtle(x, y, name):
    new_turtle = Turtle()
    new_turtle.penup()
    new_turtle.hideturtle()
    new_turtle.goto(x, y)
    new_turtle.write(name, align="center", font=("Arial", 10, "bold"))


def write_to_leaderboard(name):
    with open("leaderboard.csv", "a") as f:
        f.write(f"{name},{str(score.score)}")

#main code


while score.guesses_left > 0:

    # create pop up window
    user_answer = screen.textinput("Guess", "Please guess a state: ")

    #string checks
    user_answer = user_answer.title()
    user_answer = user_answer.strip()

    # if guess is correct, get the x and y coords for that state using pd dataframe, create a turtle at that position
    if user_answer in states_to_guess:

        # process data in states data frame to pull out row containing guessed answer and within that row x and y coords
        df_row = states_df[states_df.state == user_answer]
        x_cor = int(df_row.x)
        y_cor = int(df_row.y)
        create_turtle(x_cor, y_cor, user_answer)  # create turtle which writes answer and puts it at x and y coords

        states_to_guess.remove(user_answer) # remove state from list if already guessed

        # add to scoreboard class: decrease guesses left and increase score
        score.decrease_guesses_left()
        score.increase_score()

    else:
        # add to scoreboard class: decrease guesses left and pop up wrong
        score.decrease_guesses_left()
        score.wrong()

#pop up whats your name?
name = screen.textinput("Enter Name", "Please enter your name: ")
leaderboard_df = pandas.read_csv("leaderboard.csv")
name_list = leaderboard_df.Name.to_list()
print(name_list)

if name not in name_list:
    write_to_leaderboard(name)
    print("test")
else:
    print("got here")
    name_row = leaderboard_df[leaderboard_df.Name == name]
    name_score = int(name_row.score)
    if score.score > name_score:
        name_row.score = score.score
    leaderboard_df.to_csv("leaderboard.csv")

display(leaderboard_df)

screen.exitonclick()
