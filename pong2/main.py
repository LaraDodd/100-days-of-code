from turtle import Screen
from paddle import Paddle

# global constants
SCREEN_HEIGHT = 600
SCREEN_WIDTH = 800

#  set initial variables
game_is_on = True

# first create screen
screen = Screen()
screen.bgcolor("Black")
screen.setup(height=SCREEN_HEIGHT, width=SCREEN_WIDTH)
screen.title("PING PONG Game")
screen.listen()
screen.tracer(0)

#create classes
r_paddle = Paddle(350, 0)
l_paddle = Paddle(-350, 0)

# event listeners
screen.onkey(key="Up", fun=r_paddle.move_up)
screen.onkey(key="Down", fun=r_paddle.move_down)
screen.onkey(key="w", fun=l_paddle.move_up)
screen.onkey(key="s", fun=l_paddle.move_down)



#  main code
while game_is_on:
    screen.update()



screen.exitonclick()
