"""creates line in the middle of the screen"""

from turtle import Turtle

# global constants
SCREEN_HEIGHT = 600
SCREEN_WIDTH = 1000
NUMBER_OF_DASHES = 12


class Line():

    def __init__(self):
        self.dash_object_list = []
        self.create_dash()
        self.initialise_positions()

    def create_dash(self):
        for i in range(NUMBER_OF_DASHES):
            dash = Turtle()
            dash.shape("square")
            dash.color("white")
            dash.penup()
            dash.shapesize(1, 0.25)
            self.dash_object_list.append(dash)

    def initialise_positions(self):
        y_pos = (SCREEN_HEIGHT / 2) - 25
        for dash in self.dash_object_list:
            dash.setpos(0, y_pos)
            y_pos -= 70
