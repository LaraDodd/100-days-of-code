from turtle import Screen
import time
from snake import Snake
from food import Food
from scoreboard import Scoreboard

#  set up screen
screen = Screen()
screen.bgcolor("Black")
screen.setup(height=600, width=600)
screen.title("Snakety Snake Game")
screen.listen()
screen.tracer(0)

#  initialise starting variables
game_on = True

#  create snake, food and scoreboard instances
snake = Snake()
food = Food()
score = Scoreboard()

#  set listen keys for screen
screen.listen()
screen.onkey(key="Up", fun=snake.up)
screen.onkey(key="Down", fun=snake.down)
screen.onkey(key="Left", fun=snake.left)
screen.onkey(key="Right", fun=snake.right)

#  main code
while game_on:
    screen.update()  # updates animation after all segments have moved one step
    time.sleep(.1)  # slows animation down by putting time delay after update

    snake.move()  # snake moves forward continuously

    #  food detection
    if snake.head.distance(food.x_pos, food.y_pos) < 20:  # don't have to put x&y coords, object 'food' would suffice
        score.increase_score()
        food.reset()
        snake.increase_length()

    #  wall detection
    if snake.head.xcor() > 280 or snake.head.xcor() < -280 or snake.head.ycor() > 280 or snake.head.ycor() < -280:
        score.reset_score()
        snake.reset_snake()

    #  colliding with tail interaction
    for segment in snake.turtle_object_list[1:]:  # cycles through all segments except snake head
        if segment.distance(snake.head) < 10:
            score.reset_score()
            snake.reset_snake()

screen.exitonclick()
