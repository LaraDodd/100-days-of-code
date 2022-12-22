"""Module containing a snake class which has movement methods and initialises snake object information"""
from turtle import Turtle

#  define global constants
MOVE_DISTANCE = 20


class Snake:

    def __init__(self):
        """creates initial instance of snake object, initialising a turtle object list, a length attribute
             running the create snake method and running the initialise positions method"""
        self.turtle_object_list = []
        self.length = 3
        self.create_snake()
        self.head = self.turtle_object_list[0]
        self.initialise_positions()

    def create_snake(self):
        """creates a turtle object for each segment of snake, the number of objects created = length of snake"""
        for i in range(self.length):
            new_turtle = Turtle()
            new_turtle.shape("square")
            new_turtle.color("white")
            new_turtle.penup()
            new_turtle.speed(10)
            self.turtle_object_list.append(new_turtle)

    def initialise_positions(self):
        """Initialises positions of each turtle object in the snake"""
        x = 0.0
        for turtle in self.turtle_object_list:
            turtle.setpos(x, 0)
            x -= 20.0

    def move(self):
        """moves through each segment of the snake, from end to segment before head, and moves the segment to
        the position of the segment in front of it"""
        for seg_num in range(len(self.turtle_object_list) - 1, 0, -1):
            new_x_coord = self.turtle_object_list[seg_num - 1].xcor()
            new_y_coord = self.turtle_object_list[seg_num - 1].ycor()
            self.turtle_object_list[seg_num].goto(new_x_coord, new_y_coord)

        self.head.forward(MOVE_DISTANCE)

    def increase_length(self):
        """adds a segment (which is a turtle object) on to the snake, appends this to the turtle object list"""
        self.length = self.length + 1
        new_turtle = Turtle()
        new_turtle.shape("square")
        new_turtle.color("white")
        new_turtle.penup()
        new_turtle.speed("fastest")
        #new_turtle.goto(-250,-250)
        #  set position of when segment comes in
        new_turtle.goto(self.turtle_object_list[-1].pos())
        self.turtle_object_list.append(new_turtle)

    def up(self):
        if not self.head.heading() == 270:
            self.head.setheading(90)

    def down(self):
        if not self.head.heading() == 90:
            self.head.setheading(270)

    def left(self):
        if not self.head.heading() == 0:
            self.head.setheading(180)

    def right(self):
        if not self.head.heading() == 180:
            self.head.setheading(0)
