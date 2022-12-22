from turtle import Screen
from line import Line
from user_racket import Racket
from computer_racket import Comp
from ball import Ball

# global constants
SCREEN_HEIGHT = 600
SCREEN_WIDTH = 800

# initial conditions
game_on = True

# set up screen
screen = Screen()
screen.bgcolor("Black")
screen.setup(height=SCREEN_HEIGHT, width=SCREEN_WIDTH)
screen.title("PING PONG Game")
screen.listen()
screen.tracer(0)

# create classes
dashed_line = Line()
racket = Racket()
comp = Comp()
ball = Ball()

#  set listen keys for screen
screen.listen()
screen.onkey(key="Up", fun=racket.move_up)
screen.onkey(key="Down", fun=racket.move_down)

# main code
while game_on:
    screen.update()

    #  move the computer racket up and down
    comp.move()

    #  move the ball constantly
    ball.move()

    #  detect collision with wall
    if ball.ycor() > SCREEN_HEIGHT / 2 or ball.ycor() < -SCREEN_HEIGHT / 2:
        ball.rebound()

    #  detect collision with rackets
    for segment in racket.turtle_object_list:
        if ball.distance(segment) < 20:
            ball.rebound()

    # #  detect goal scored
    #     if ball.ycor() > SCREEN_HEIGHT / 2 or ball.ycor() < -SCREEN_HEIGHT / 2:
    #         ball.rebound()

screen.exitonclick()

# classes:
"""user_racket: will have up and down methods, will have creat reacket method and will initialise in init
                will have initial position method, called in init, will have move
ball: change direction method, move method
scoreboard: game over, reset and update method, initial score methof
computer: will have move methods"""

# main
"""will create all the classes
in while loop:
will run ball.move and comp_racket.move 
will have updated
will detect when ball has hit the comp or user racket
will run ball.change direction method
will initialise screen, with line down middle?
will have event listener keys for up and down
will call score.gameover when user loses and end while loop
"""
