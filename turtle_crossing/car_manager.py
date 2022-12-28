from turtle import Turtle
import random

COLORS = ["red", "orange", "yellow", "green", "blue", "purple", "gold"]
STARTING_MOVE_DISTANCE = 5
MOVE_INCREMENT = 2


class CarManager():
    def __init__(self):
        self.no_cars = 6
        self.cars_list = []
        self.move_distance = STARTING_MOVE_DISTANCE
        self.create_cars()


    def create_cars(self):
        for i in range(self.no_cars):
            new_car = Turtle()
            new_car.shape("square")
            new_car.color(random.choice(COLORS))
            new_car.penup()
            new_car.shapesize(0.5, 1)
            new_car.goto(300, random.randint(-100, 250))
            self.cars_list.append(new_car)



    def move(self):
        for car in self.cars_list:
            random_int = random.randint(0, 1)
            if random_int == 0:
                car.goto(car.xcor() - self.move_distance, car.ycor())

    def increase_speed(self):
        self.move_distance += MOVE_INCREMENT

    def increase_cars_and_reset(self):
        self.no_cars += 1
        new_car = Turtle()
        new_car.shape("square")
        new_car.color(random.choice(COLORS))
        new_car.penup()
        new_car.shapesize(0.5, 1)
        new_car.goto(250, random.randint(-100, 250))
        self.cars_list.append(new_car)

    def add_car_row(self):
        self.create_cars()

