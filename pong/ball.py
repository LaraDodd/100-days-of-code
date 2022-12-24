from turtle import Turtle
import random
import time


class Ball(Turtle):
    def __init__(self):
        super().__init__()
        self.create_ball()
        self.start_position()

    def create_ball(self):
        self.shape("square")
        self.color("white")
        self.penup()
        self.speed(1)

    def start_position(self):
        self.goto(0,0)
        if random.randint(0,1) == 0:
            rand_heading = random.randint(135,225)
        else:
            rand_heading = random.randint(-45,45)
            if rand_heading < 0:
                rand_heading -= 360
        self.setheading(rand_heading)


    def move(self):
        self.forward(20)
        time.sleep(0.01)

    def rebound(self):
        new_heading = self.heading()+random.randint(85, 95)
        if new_heading > 360:
            new_heading -= 360
        self.setheading(new_heading)
