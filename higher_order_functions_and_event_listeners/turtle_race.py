from turtle import Turtle, Screen
import random


def randomly_move_turtles(turtle_object):
    rand_int = random.randint(0, 1)
    if rand_int == 0:
        move_forward(turtle_object)
        #print(f"{turtle_object.name} {turtle_object.pos()[0]}")


def move_forward(turtle_object):
    """Moves inputted turtle object forward by 10"""
    turtle_object.forward(10)

#  Creating turtle object from the turtle class, with the name 'tim'
tim = Turtle()
tim.name = "Tim!!"  # assigning a name attribute 'Tim!!' to the turtle object tim

red = Turtle()
red.color("red")  # assigning a colour to the turtle object red
red.name = "Red Turtle"

yellow = Turtle()
yellow.color("yellow")
yellow.name = "Yellow Turtle"

green = Turtle()
green.color("green")
green.name = "Green Turtle"

purple = Turtle()
purple.color("purple")
purple.name = "Purp Turt"

turtle_object_list = [red, yellow, green, purple, tim]  # creating list of all the turtle objects created
end_reached = False  # initialising end_reach = False, for the while loop

# for all objects in turtle lists, use method shape and pen up to remove pen and give them turtle shapes
for turtle in turtle_object_list:
    turtle.penup()
    turtle.shape("turtle")

#colours = ["red", "green", "blue", "purple", "yellow"]

my_screen = Screen()
user_guess = my_screen.textinput(title="Place ya bets!",
                                 prompt="Which turtle do you think will win? Red, green, yellow, purple, or Tim?").lower()
my_screen.setup(500, 400)
my_screen.bgcolor("LightBlue")

# setting initial coordinates for each turtle
y = -100
for turtle in turtle_object_list:
    turtle.setpos(-225, y)
    y += 50

while not end_reached:
    x_positions = []
    for turtle in turtle_object_list:
        randomly_move_turtles(turtle)
        x_positions.append(turtle.pos()[0])
        #print(x_positions)
        if max(x_positions) > 200.0:
            end_reached = True

index = x_positions.index(max(x_positions))
winner = turtle_object_list[index].name
print(f"The winner is {winner}")

if user_guess[0] == winner.lower()[0]:
    print("Well done you win!")
else:
    print("Unlucky... betted on the wrong horse!")


my_screen.exitonclick()
