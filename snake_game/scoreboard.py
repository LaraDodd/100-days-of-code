from turtle import Turtle

# global constants
ALIGNMENT = 'center'
SCORE_FONT = ('Courier', 15, 'normal')
GAME_OVER_FONT = ('Courier', 25, 'bold')


class Scoreboard(Turtle):
    def __init__(self):
        super().__init__()
        self.score = 0
        self.high_score = 0
        self.goto(x=0, y=270)
        self.hideturtle()
        self.color("white")
        self.write(f"Score: {self.score}", move=False, align=ALIGNMENT, font=SCORE_FONT)

    def update_scoreboard(self):
        self.clear()
        #  have to call self.write again otherwise it won't re-wrtie the score
        self.write(f"Score: {self.score} High ScoreL {self.high_score}", move=False, align=ALIGNMENT, font=SCORE_FONT)

    def increase_score(self):
        self.score += 1
        self.update_scoreboard()


    def reset_score(self):
        if self.score > self.high_score:
            self.high_score = self.score
        self.score = 0
        self.update_scoreboard()

    def game_over(self):
        self.color("gold")
        self.goto(x=0, y=0)
        self.write(f"GAME OVER", move=False, align=ALIGNMENT, font=GAME_OVER_FONT)
