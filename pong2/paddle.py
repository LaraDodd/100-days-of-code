"""this module creates a paddle"""

from turtle import Turtle

class Paddle(Turtle):
    def __init__(self, x_coord, y_coord):
        super().__init__()
        self.x_coord = x_coord
        self.y_coord = y_coord
        self.create_paddle()
        self.set_position()

        # create paddle
    def create_paddle(self):
        self.color("white")
        self.penup()
        self.shape("square")
        self.shapesize(5, 1)  # instead of connecting 3 turtles together, just stretch one turtle

    def set_position(self):
        self.goto(self.x_coord, self.y_coord)


    # functions
    def move_up(self):  # instead of moving by changing head and moving foward, move the position!!
        new_y = self.ycor() + 20
        self.goto(self.xcor(), new_y)

    def move_down(self):  # instead of moving by changing head and moving foward, move the position!!
        new_y = self.ycor() - 20
        self.goto(self.xcor(), new_y)