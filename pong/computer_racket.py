"""this program contains all information to do with the computer racket"""

from turtle import Turtle
import time

# global constants
SCREEN_HEIGHT = 600
SCREEN_WIDTH = 1000

class Comp:
    def __init__(self):
        self.turtle_object_list = []
        self.length = 5
        self.create_racket()
        self.initialise_positions()

    def create_racket(self):
        for i in range(self.length):
            new_turtle = Turtle()
            new_turtle.shape("square")
            new_turtle.color("white")
            new_turtle.penup()
            new_turtle.speed(3)
            self.turtle_object_list.append(new_turtle)

    def initialise_positions(self):
        y_pos = 20
        for segment in self.turtle_object_list:
            segment.setpos((SCREEN_WIDTH/2)-20, y_pos)
            y_pos -= 20.0

    def up(self):
        for segment in self.turtle_object_list:
            segment.setheading(90)

    def down(self):
        for segment in self.turtle_object_list:
            segment.setheading(270)

    def move_up(self):
        self.up()
        for segment in self.turtle_object_list:
            segment.forward(10)

    def move_down(self):
        self.down()
        for segment in self.turtle_object_list:
            segment.forward(10)

    def move(self):
        time.sleep(.025)
        if self.turtle_object_list[1].ycor() < 270 and self.turtle_object_list[1].heading() == 90:
            self.move_up()
        else:
            self.down()

        if self.turtle_object_list[1].ycor() > -270 and self.turtle_object_list[1].heading() == 270:
            self.move_down()
        else:
            self.up()


