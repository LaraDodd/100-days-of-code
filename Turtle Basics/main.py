import turtle
import prettytable

timmy_the_turtle = turtle.Turtle()

#or can do this:
from turtle import Turtle, Screen
timster_the_turtle = Turtle()

print(timster_the_turtle)
timster_the_turtle.shape("turtle")
timster_the_turtle.color("Lavender", "coral4")
timster_the_turtle.forward(100)
timster_the_turtle.circle(4,2.0,1)

my_screen = Screen()
print(my_screen.canvheight)

my_screen.exitonclick()

#print(dir(turtle))

from prettytable import PrettyTable

table = PrettyTable()
print(table)

table.add_column("Name", ["pika", "dika", "doo"])
table.add_column("Type", ["Electric", "Water", "Fire"])

table.align = "l"

print(table)


