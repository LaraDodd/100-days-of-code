from turtle import Turtle
import random

COLORS = ["red", "orange", "yellow", "green", "blue", "purple", "gold"]
STARTING_MOVE_DISTANCE = 5
MOVE_INCREMENT = 10

class CarManager():
    def __init__(self):
        self.no_cars = 6
        self.cars_list = []
        self.move_distance = STARTING_MOVE_DISTANCE
        self.create_cars()
        self.initial_positions()

    def create_cars(self):
        for i in range(self.no_cars):
            new_car = Turtle()
            new_car.shape("square")
            new_car.color(random.choice(COLORS))
            new_car.penup()
            new_car.shapesize(0.5, 1)
            self.cars_list.append(new_car)
        print(self.cars_list)

    def initial_positions(self):
        y_pos = -100
        for car in self.cars_list:
            car.goto(250, y_pos)
            y_pos += 50

    def move(self):
        for car in self.cars_list:
            random_int = random.randint(0, 1)
            if random_int == 0:
                car.goto(car.xcor() + self.move_distance, car.ycor())

    def increase_speed(self):
        self.move_distance += MOVE_INCREMENT


