"""this module contains all information regarding the user racket"""
from turtle import Turtle


class Racket():
    def __init__(self):
        self.turtle_object_list = []
        self.length = 3
        self.create_racket()
        self.initialise_positions()

    def create_racket(self):
        for i in range(self.length):
            new_turtle = Turtle()
            new_turtle.shape("square")
            new_turtle.color("white")
            new_turtle.penup()
            new_turtle.speed(10)
            self.turtle_object_list.append(new_turtle)

    def initialise_positions(self):
        y_pos = 20
        for segment in self.turtle_object_list:
            segment.setpos(-280, y_pos)
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
            segment.forward(20)

    def move_down(self):
        self.down()
        for segment in self.turtle_object_list:
            segment.forward(20)

