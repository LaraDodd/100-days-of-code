from turtle import Turtle, Screen

# global constants
SCREEN_HEIGHT = 600
SCREEN_WIDTH = 800

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
def move_up(turtle_object):  # instead of moving by changing head and moving foward, move the position!!
    new_y = turtle_object.ycor() + 20
    turtle_object.goto(turtle_object.xcor(), new_y)


def move_down(turtle_object):  # instead of moving by changing head and moving foward, move the position!!
    new_y = turtle_object.ycor() - 20
    turtle_object.goto(turtle_object.xcor(), new_y)


# event listeners
screen.onkey(key="Up", fun=move_up(paddle))
screen.onkey(key="Down", fun=move_down(paddle))

screen.update()

screen.update()
screen.exitonclick()
