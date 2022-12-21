from turtle import Turtle
import random

"""This module contains all the methods and attributes relating to the snakes food. It must: randomly 
generate a position of the food; have all the attributes of turtle within it; disappear when the snake head
hits it and make snake longer"""


class Food(Turtle):

    def __init__(self):
        super().__init__()
        self.x_pos = None
        self.y_pos = None
        self.create_food()
        self.generate_rand_pos()

    def create_food(self):
        self.shape("circle")
        self.color("blue")
        self.penup()

    def generate_rand_pos(self):
        self.x_pos = random.randint(-275, 275)
        self.y_pos = random.randint(-275, 275)
        self.goto(self.x_pos, self.y_pos)
