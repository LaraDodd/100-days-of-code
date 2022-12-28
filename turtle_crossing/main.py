import time
from turtle import Screen
from player import Player
from car_manager import CarManager
from scoreboard import Scoreboard

# set up screen
screen = Screen()
screen.setup(width=600, height=600)
screen.tracer(0)

# create classes
player = Player()
cars = CarManager()
score = Scoreboard()

game_is_on = True
while game_is_on:
    time.sleep(0.1)
    screen.update()
    cars.move()


screen.exitonclick()
