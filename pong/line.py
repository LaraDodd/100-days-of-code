"""creates line in the middle of the screen"""

from turtle import Turtle

NUMBER_OF_DASHES = 8

class Line(Turtle):

    def __init__(self):
        super().__init__()
        self.create_line()


    def create_line(self):
        x = 250
        for i in range(NUMBER_OF_DASHES):
            self.shape("turtle")
            self.color("white")
            self.goto(0, x)
            #self.stretch()
            X -= 50



