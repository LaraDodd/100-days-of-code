import turtle
from turtle import Turtle, Screen
import random


def random_rgb():
    r = random.randint(0, 255)
    b = random.randint(0, 255)
    g = random.randint(0, 255)
    return r, g, b


def random_colour(object):
    object.pencolor(random_rgb())


turtle.colormode(255)
laz = Turtle()

laz.shape("circle")
laz.shapesize(.1,.1)
laz.pensize(1)
laz.speed(0)

for i in range(0, 360, 5):
    laz.pencolor(random_rgb())
    laz.circle(75)
    laz.setheading(i)

my_screen = Screen()
my_screen.exitonclick()
