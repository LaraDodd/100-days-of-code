'''Module containing a snake class which has movement methods and snake object infomation'''
from turtle import Turtle

#  initial global variables
X = 0.0

class Snake:

    def __init__(self, length):
        self.turtle_object_list = []
        self.length = length
        self.create_snake()
        self.initialise_positions

    def create_snake(self):
        for i in range(self.length):
            new_turtle = Turtle()
            new_turtle.shape("square")
            new_turtle.color("white")
            new_turtle.penup()
            new_turtle.speed(10)
            self.turtle_object_list.append(new_turtle)

    def initialise_positions(self):
        for turtle in self.turtle_object_list:
            turtle.setpos(X, 0)
            X -= 20.0

    def move(self):
        #  moves through each segment of the snake, from end to segment before head, and moves the segment to
        #  the position of the segment in front of it
        for seg_num in range(len(self.turtle_object_list) - 1, 0, -1):
            new_x_coord = self.turtle_object_list[seg_num - 1].xcor()
            new_y_coord = self.turtle_object_list[seg_num - 1].ycor()
            self.turtle_object_list[seg_num].goto(new_x_coord, new_y_coord)

        self.turtle_object_list[0].forward(20)
