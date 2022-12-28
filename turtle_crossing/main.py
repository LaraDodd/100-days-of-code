import time
from turtle import Screen
from player import Player
from car_manager import CarManager
from scoreboard import Scoreboard

# set up screen
screen = Screen()
screen.setup(width=600, height=600)
screen.tracer(0)
screen.listen()

# create classes
player = Player()
cars = CarManager()
score = Scoreboard()

# event listeners
screen.onkey(key="Up", fun=player.move_up)
screen.onkey(key="Down", fun=player.move_down)

# set initial variables
counter = 0
game_is_on = True

# main code
while game_is_on:
    time.sleep(0.1)
    screen.update()
    cars.move()
    counter += 1

    if counter % 40 == 0:  # every 4s a new row of cars will be generated
        cars.add_car_row()

    # detect collision
    for car in cars.cars_list:
        if car.distance(player) < 15:
            score.game_over()
            screen.update()
            game_is_on = False

    # detect finish line
    if player.ycor() > 280:
        player.restart_pos()
        score.increase_score()
        cars.increase_speed()
        cars.increase_cars_and_reset()

screen.exitonclick()
