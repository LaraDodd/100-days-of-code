from turtle import Turtle, Screen

tim = Turtle()

def move_forward():
    tim.forward(10)

def move_backward():
    tim.backward(10)

def turn_right():
    tim.right(5)

def turn_left():
    tim.left(5)



my_screen = Screen()
my_screen.listen()


my_screen.onkey(key="Down", fun=turn_right)
my_screen.onkey(key="Right", fun=move_forward)
my_screen.onkey(key="Left", fun=move_backward)
my_screen.onkey(key="Up", fun=turn_left)
my_screen.onkey(key="Down", fun=turn_right)
my_screen.onkey(key="c", fun=tim.reset)



my_screen.exitonclick()

