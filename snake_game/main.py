from turtle import Screen
import time
from snake import Snake

#  set up screen
screen = Screen()
screen.bgcolor("Black")
screen.setup(height=600, width=600)
screen.title("Snakety Snake Game")
screen.listen()
screen.tracer(0)


#  initialise starting variables
game_on = True

#  create snake object
snake = Snake(length=30)

screen.listen()
screen.onkey(key="Up", fun=snake.up)
screen.onkey(key="Down", fun=snake.down)
screen.onkey(key="Left", fun=snake.left)
screen.onkey(key="Right", fun=snake.right)


#  main code
while game_on:
    screen.update()  # updates animation after all segments have moved one step
    time.sleep(.1)  # slows animation down by putting time delay after update

    snake.move()


screen.exitonclick()
