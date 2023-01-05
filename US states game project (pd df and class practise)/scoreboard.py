from turtle import Turtle
import pandas
class ScoreBoard(Turtle):
    def __init__(self):
        super().__init__()
        self.penup()
        self.score = 0
        self.highscore = None
        self.get_highscore()
        self.guesses_left = 6
        self.hideturtle()
        self.color("DarkSlateGray")
        self.goto(125, 250)
        self.write(f"{self.score}/50 Highscore: {self.highscore}/50", align="center", font=("Courier", 25, "bold"))

    def update_scoreboard(self):
        self.clear()
        self.color("DarkSlateGray")
        self.goto(125, 200)
        self.write(f"Score: {self.score}/50 Highscore: {self.highscore}/50  \nguesses left: {self.guesses_left}",
                   align="center", font=("Courier", 25, "bold"))

    def increase_score(self):
        self.score += 1
        self.update_scoreboard()

    def decrease_guesses_left(self):
        self.guesses_left -= 1
        self.update_scoreboard()

    def wrong(self):
        self.goto(0, 0)
        self.color("red")
        self.write("WRONG", align="center", font=("Courier", 25, "bold"))

    def get_highscore(self):
        leaderboard_df = pandas.read_csv("leaderboard.csv")
        self.highscore = leaderboard_df.Score.astype(int).max()


