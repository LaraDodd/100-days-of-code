from turtle import Turtle
import random

"""This module contains all the methods and attributes relating to the snakes food. It must: randomly 
generate a position of the food; have all the attributes of turtle within it; disappear when the snake head
hits it and make snake longer"""


class Food(Turtle):

    def __init__(self):
        super().__init__()
        self.create_food()
        self.y_pos = None
        self.x_pos = None
        self.generate_rand_pos()

    def create_food(self):
        new_food = Turtle()
        new_food.shape("circle")
        new_food.color("blue")

    def generate_rand_pos(self):
        self.x_pos = random.randint(0, 600)
        self.y_pos = random.randint(0, 600)
