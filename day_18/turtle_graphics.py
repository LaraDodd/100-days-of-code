from turtle import Turtle, Screen

timmy = Turtle()
timmy.shape("turtle")
timmy.color("purple", "blue")
timmy.forward(100)
timmy.right(90)

def square(object, distance):
    for i in range(3):
        object.forward(distance)
        object.right(90)

square(timmy, 100)


my_screen = Screen()
my_screen.exitonclick()


