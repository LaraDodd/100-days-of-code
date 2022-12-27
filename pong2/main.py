from turtle import Turtle, Screen

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

# create paddle
paddle = Turtle()
paddle.color("white")
paddle.penup()
paddle.shape("square")
paddle.goto((SCREEN_WIDTH / 2) - 20, 0)
paddle.shapesize(5, 1)  # instead of connecting 3 turtles together, just stretch one turtle


# functions
def move_up():  # instead of moving by changing head and moving foward, move the position!!
    new_y = paddle.ycor() + 20
    paddle.goto(paddle.xcor(), new_y)


def move_down():  # instead of moving by changing head and moving foward, move the position!!
    new_y = paddle.ycor() - 20
    paddle.goto(paddle.xcor(), new_y)


# event listeners
screen.onkey(key="Up", fun=move_up)
screen.onkey(key="Down", fun=move_down)


#  main code
while game_is_on:
    screen.update()



screen.exitonclick()
