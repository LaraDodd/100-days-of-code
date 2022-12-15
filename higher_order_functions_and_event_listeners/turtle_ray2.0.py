from turtle import Turtle, Screen
import random

def random_move_forward(turtle_object):
    turtle_object.forward(random.randint(0,10))

colours = ["red", "green", "blue", "purple", "yellow"]
initial_y_pos = [-100, -50, 0 , 50, 100]
is_race_on = True
turtle_object_list = []

my_screen = Screen()
user_guess = my_screen.textinput(title="Place ya bets!",
                                 prompt="Which turtle do you think will win? Red, green, yellow, purple, or Tim?").lower()
my_screen.setup(500, 400)
my_screen.bgcolor("LightBlue")

for turtle_index in range(0,5):
    new_turtle = Turtle()
    new_turtle.penup()
    new_turtle.color(colours[turtle_index])
    new_turtle.shape("turtle")
    new_turtle.setpos(-225, initial_y_pos[turtle_index])
    turtle_object_list.append(new_turtle)

while is_race_on:
    for turtle_object in turtle_object_list:
        random_move_forward(turtle_object)
        if turtle_object.xcor() > 230:
            is_race_on = False
            winner = turtle_object.pencolor()

if winner == user_guess:
    print(f"Well done! You guessed correctly... the winner was {winner}")
else:
    print(f"Oh dear! You guessed INcorrectly... the winner was {winner}")



my_screen.exitonclick()