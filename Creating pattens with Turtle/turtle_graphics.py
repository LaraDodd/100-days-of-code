from turtle import Turtle, Screen

timmy = Turtle()
timmy.shape("turtle")
#timmy.color("purple", "blue")
#timmy.forward(100)
#timmy.right(90)

def square(object, distance):
    for i in range(3):
        object.forward(distance)
        object.right(90)

def dotted_line(object, distance):
    original_position = object.pos()
    while object.pos()-original_position < (distance,0):
        object.forward(5)
        object.penup()
        object.forward(5)
        object.pendown()

dotted_line(timmy, distance=100)

square(timmy, 100)


my_screen = Screen()
my_screen.exitonclick()


