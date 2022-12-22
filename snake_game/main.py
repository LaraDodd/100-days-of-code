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


#  create snake and object
snake = Snake()
food = Food()
score = Scoreboard()

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

    #  food detection
    if snake.head.distance(food.x_pos, food.y_pos) < 20:
        score.add()
        food.reset()
        snake.increase_length()

    #  wall detection
    if snake.head.xcor() > 290 or snake.head.xcor() < -290 or snake.head.ycor() > 290 or snake.head.ycor() < -290:
        game_on = False
        score.game_over()

    #  colliding with tail interaction
    for i in range(1, len(snake.turtle_object_list)-1):
        if snake.turtle_object_list[i].distance(snake.head) < 10:
            game_on = False
            score.game_over()

screen.exitonclick()
