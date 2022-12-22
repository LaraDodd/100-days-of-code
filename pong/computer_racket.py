"""this program contains all information to do with the computer racket"""

from turtle import Turtle


class Comp:
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
            segment.setpos(380, y_pos)
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
            segment.forward(40)

    def move_down(self):
        self.down()
        for segment in self.turtle_object_list:
            segment.forward(40)

    def move(self):
        while self.turtle_object_list[1].ycor() < 280 and self.turtle_object_list[1].heading() == 90:
            self.move_up()
        while self.turtle_object_list[1].ycor() > -280 and self.turtle_object_list[1].heading() == 270:
            self.move_down()


