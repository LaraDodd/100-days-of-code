from turtle import Turtle
import random
import time


class Ball(Turtle):
    def __init__(self):
        super().__init__()
        self.create_ball()
        self.start_position()

    def create_ball(self):
        self.shape("circle")
        self.color("gold")
        self.penup()
        self.speed(1)

    def start_position(self):
        self.goto(0,0)
        self.setheading(random.randint(0, 360))


    def move(self):
        self.forward(20)
        time.sleep(0.01)

    def rebound(self):
        new_heading = self.heading()+random.randint(85, 95)
        if new_heading > 360:
            new_heading -= 360
        self.setheading(new_heading)
