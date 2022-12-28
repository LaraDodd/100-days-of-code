from turtle import Screen
from paddle import Paddle
from ball import Ball
import time
from line import Line
from scoreboard import Scoreboard

# global constants
SCREEN_HEIGHT = 600
SCREEN_WIDTH = 800

# set initial variables
game_is_on = True
level = 0.075

# first create screen
screen = Screen()
screen.bgcolor("Black")
screen.setup(height=SCREEN_HEIGHT, width=SCREEN_WIDTH)
screen.title("PING PONG Game")
screen.listen()
screen.tracer(0)

# create classes
r_paddle = Paddle(370, 0)
l_paddle = Paddle(-370, 0)
ball = Ball()
line = Line()
scoreboard = Scoreboard()

# event listeners
screen.onkey(key="Up", fun=r_paddle.move_up)
screen.onkey(key="Down", fun=r_paddle.move_down)
screen.onkey(key="w", fun=l_paddle.move_up)
screen.onkey(key="s", fun=l_paddle.move_down)

# main code
while game_is_on:
    time.sleep(level)
    screen.update()
    ball.move()

    # detect collision with wall
    if ball.ycor() > (SCREEN_HEIGHT / 2 - 20) or ball.ycor() < (-SCREEN_HEIGHT / 2 + 20):
        ball.bounce_y()

    # detect collision with paddles
    if ball.xcor() > 340 and ball.distance(r_paddle) < 50 or ball.xcor() < -340 and ball.distance(l_paddle) < 50:
        ball.bounce_x()

    # detect when left goal scored
    if ball.xcor() > 380:
        ball.refresh_pos()
        ball.bounce_x()
        scoreboard.l_point()
        if level > 0.005:
            level -= 0.005

    # detect when right goal scored
    if ball.xcor() < - 380:
        ball.refresh_pos()
        ball.bounce_x()
        scoreboard.r_point()
        if level > 0.005:
            level -= 0.005

screen.exitonclick()
