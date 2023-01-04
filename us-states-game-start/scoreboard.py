from turtle import Turtle
class ScoreBoard(Turtle):
    def __init__(self):
        super().__init__()
        self.penup()
        self.score = 0
        self.hideturtle()
        self.color("red")
        self.goto(300, 300)
        self.write(f"{self.score}/50", align="left", font=("Courier", 35, "bold"))

    def update_scoreboard(self):
        self.clear()
        self.write(f"{self.score}/50", align="left", font=("Courier", 35, "bold"))

    def increase_score(self):
        self.score += 1
        self.update_scoreboard()