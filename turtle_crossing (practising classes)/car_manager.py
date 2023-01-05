"""this program creates a group of cars with a random y pos and random colour. It has an add_car method which
increases the number of cars in the group created by 1. It has an add car row method which causes another group
 of cars to be created, initialises their positions at the start and adds this group of cars to the car list. It
 also has a move function, and an increase speed function"""

from turtle import Turtle
import random

COLORS = ["red", "orange", "yellow", "green", "blue", "purple", "gold"]
STARTING_MOVE_DISTANCE = 5
MOVE_INCREMENT = 2


class CarManager():

    def __init__(self):
        """initialises no_cars in group, cars_list, the starting move distance and creates the first car group"""
        self.no_cars = 6
        self.cars_list = []
        self.move_distance = STARTING_MOVE_DISTANCE
        self.create_car_row()

    def create_car_row(self):
        """creates new car objects, initialises starting position and appends them to a list,
        number of car objects made depends on no_cars"""
        for i in range(self.no_cars):
            new_car = Turtle()
            new_car.shape("square")
            new_car.color(random.choice(COLORS))
            new_car.penup()
            new_car.shapesize(1, 2)
            new_car.goto(random.randint(280, 310), random.randint(-200, 250))
            self.cars_list.append(new_car)

    def move(self):
        """moves all the cars in the list randomly"""
        for car in self.cars_list:
            random_int = random.randint(0, 1)
            if random_int == 0:
                car.goto(car.xcor() - self.move_distance, car.ycor())

    def increase_speed(self):
        """increases move distance by move increment"""
        self.move_distance += MOVE_INCREMENT

    def increase_cars_and_reset(self):
        """creates another car and adds to the list"""
        self.no_cars += 1


