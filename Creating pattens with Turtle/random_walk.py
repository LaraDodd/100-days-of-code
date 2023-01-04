import turtle
from turtle import Turtle, Screen
import random

colours = [ "yellow", "gold", "orange", "red", "maroon", "violet", "magenta", "purple", "navy", "blue", "skyblue"
    , "cyan", "turquoise", "lightgreen", "green", "darkgreen", "chocolate", "brown", "black", "gray"]

turtle.colormode(255)

tish = Turtle()
tish.pensize(15)
tish.shape("classic")
tish.speed(0)

total_distance = 3000
distance_travelled = 0
step_distance = 30
directions = [0,90,180,270]

def random_direction(object):
    object.setheading(random.choice(directions))

def random_rgb():
    r = random.randint(0,255)
    b = random.randint(0,255)
    g = random.randint(0,255)
    return (r,g,b)
def random_colour(object):
    object.pencolor(random_rgb())

def move_step(object, step_distance):
    object.forward(step_distance)


while distance_travelled < total_distance:
    random_direction(tish)
    random_colour(tish)
    move_step(tish, step_distance)
    distance_travelled += step_distance
    print(distance_travelled)


my_screen = Screen()
my_screen.exitonclick()