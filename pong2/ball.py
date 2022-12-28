"""this program contains all information relating to the ball, including:
creation, moving, rebounding"""

from turtle import Turtle


class Ball(Turtle):

    def __init__(self):
        super().__init__()
        self.create_ball()

    def create_ball(self):
        self.color("white")
        self.penup()
        self.shape("square")

    def move(self):
        self.goto(self.xcor()+10, self.ycor()+10)