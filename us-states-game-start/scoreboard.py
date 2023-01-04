from turtle import Turtle
class ScoreBoard(Turtle):
    def __init__(self):
        super().__init__()
        self.penup()
        self.score = 0
        self.guesses_left = 60
        self.hideturtle()
        self.color("red")
        self.goto(250, 150)
        self.write(f"{self.score}/50", align="left", font=("Courier", 35, "bold"))

    def update_scoreboard(self):
        self.clear()
        self.write(f"{self.score}/50, guesses left: {self.guesses_left}", align="left", font=("Courier", 35, "bold"))

    def increase_score(self):
        self.score += 1
        self.update_scoreboard()

    def decrease_guesses_left(self):
        self.guesses_left -= 1
        self.update_scoreboard()
