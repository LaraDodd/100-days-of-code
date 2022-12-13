import turtle
from turtle import Turtle, Screen
import random

turtle.colormode(255)
laz = Turtle()

laz.shape("classic")
laz.pensize(1)
laz.speed(7)

for i in range(0,360,5):

    laz.circle(75)
    laz.setheading(i)





my_screen = Screen()
my_screen.exitonclick()