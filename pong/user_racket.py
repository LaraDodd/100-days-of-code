"""this module contains all information regarding the user racket"""
from turtle import Turtle


class Racket(Turtle):
    def __init__(self):
        super().__init__()
        self.turtle_object_list = []
        self.length = 3
        self.head = self.turtle_object_list[0]
        self.create_racket()
        self.initialise_positions()

    def create_racket(self):
        pass
