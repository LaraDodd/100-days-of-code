from turtle import Turtle
class ScoreBoard(Turtle):
    def __init__(self):
        super().__init__()
        self.penup()
        self.score = 0
        self.guesses_left = 52
        self.hideturtle()
        self.color("DarkSlateGray")
        self.goto(125, 200)
        self.write(f"{self.score}/50", align="center", font=("Courier", 25, "bold"))

    def update_scoreboard(self):
        self.clear()
        self.color("DarkSlateGray")
        self.goto(125, 200)
        self.write(f"{self.score}/50 guesses left: {self.guesses_left}", align="center", font=("Courier", 25, "bold"))

    def increase_score(self):
        self.score += 1
        self.update_scoreboard()

    def decrease_guesses_left(self):
        self.guesses_left -= 1
        self.update_scoreboard()

    def wrong(self):
        self.goto(0, 0)
        self.color("red")
        self.write("WRONG BISH", align="center", font=("Courier", 25, "bold"))
