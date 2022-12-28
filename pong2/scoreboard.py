"""this module writes the score on the screen and refreshes the score each time"""
from turtle import Turtle

# global constants
ALIGNMENT = 'center'
SCORE_FONT = ('Courier', 35, 'bold')

class Scoreboard(Turtle):
    def __init__(self):
        super().__init__()
        self.color("white")
        self.l_score = 0
        self.r_score = 0
        self.hideturtle()
        self.penup()
        self.update_scoreboard()

    def update_scoreboard(self):
        self.clear()
        self.goto(x=-100, y=200)
        self.write(f"{self.l_score}", move=False, align=ALIGNMENT, font=SCORE_FONT)
        self.goto(x=100, y=200)
        self.write(f"{self.r_score}", move=False, align=ALIGNMENT, font=SCORE_FONT)

    def l_point(self):
        self.l_score += 1
        self.update_scoreboard()

    def r_point(self):
        self.r_score += 1
        self.update_scoreboard()
