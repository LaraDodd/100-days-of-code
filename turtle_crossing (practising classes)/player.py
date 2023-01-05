from turtle import Turtle

STARTING_POSITION = (0, -250)
MOVE_DISTANCE = 20
FINISH_LINE_Y = 280


class Player(Turtle):
    def __init__(self):
        """creates turtle, sets heading up, removes pen, sets initial position"""
        super().__init__()
        self.shape("turtle")
        self.setheading(90)
        self.penup()
        self.goto(STARTING_POSITION)

    def move_up(self):
        """moves turtle up by move distance"""
        self.goto(self.xcor(), self.ycor() + MOVE_DISTANCE)

    def move_down(self):
        """moves turtle down by move distance"""
        self.goto(self.xcor(), self.ycor() - MOVE_DISTANCE)

    def restart_pos(self):
        """resets turtle to starting position"""
        self.goto(STARTING_POSITION)


