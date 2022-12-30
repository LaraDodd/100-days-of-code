"""contains all code regarding the score, including: writing the score, increasing the score and writing game over"""

from turtle import Turtle

FONT = ("Courier", 24, "normal")


class Scoreboard(Turtle):
    def __init__(self):
        """creates turtle, initialises score, writes score"""
        super().__init__()
        self.color("black")
        self.hideturtle()
        self.penup()
        self.score = 0
        self.goto(0, 250)
        self.write(f"Score: {self.score}", align="center", font=FONT)

    def increase_score(self):
        """clears current score, increases current score by 1, rewrites score"""
        self.clear()
        self.score += 1
        self.write(f"Score: {self.score}", align="center", font=FONT)

    def game_over(self):
        """prints game over in centre of screen"""
        self.goto(0, 0)
        self.write("GAME OVER", align="center", font=("Courier", 40, "normal"))
