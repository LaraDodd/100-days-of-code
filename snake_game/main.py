from turtle import Turtle, Screen
import time

#  set up screen
screen = Screen()
screen.bgcolor("Black")
screen.setup(height=600, width=600)
screen.title("Snakety Snake Game")
screen.listen()
screen.tracer(0)


#  initialise starting variables
len_snake = 3
turtle_object_list = []
game_on = True

#  create turtle objects and put in list
for i in range(len_snake):
    new_turtle = Turtle()
    new_turtle.shape("square")
    new_turtle.color("white")
    new_turtle.penup()
    new_turtle.speed(10)
    turtle_object_list.append(new_turtle)


#  set initial positions of turtle objects
x = 0.0
for turtle in turtle_object_list:
    turtle.setpos(x, 0)
    x -= 20.0

#  main code
while game_on:
    screen.update()  # updates animation after all segments have moved one step
    time.sleep(.1)  # slows animation down by putting time delay after update

    #  moves through each segment of the snake, from end to segment before head, and moves the segment to
    #  the position of the segment in front of it
    for seg_num in range(len(turtle_object_list)-1, 0, -1):
        new_x_coord = turtle_object_list[seg_num - 1].xcor()
        new_y_coord = turtle_object_list[seg_num - 1].ycor()
        turtle_object_list[seg_num].goto(new_x_coord, new_y_coord)

    turtle_object_list[0].forward(20)
    #screen.onkey(key="Left", fun=turtle_object_list[0].right(90))
    #screen.onkey(key="Right", fun=turtle_object_list[0].left(90))


screen.exitonclick()
