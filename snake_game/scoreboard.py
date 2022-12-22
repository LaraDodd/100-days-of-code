from turtle import Turtle

# global constants
ALIGNMENT = 'center'
SCORE_FONT = ('Courier', 15, 'normal')
GAME_OVER_FONT = ('Courier', 15, 'normal')


class Scoreboard(Turtle):
    def __init__(self):
        super().__init__()
        self.score = 0
        self.goto(x=0, y=270)
        self.hideturtle()
        self.color("white")
        self.write(f"Score: {self.score}", move=False, align=ALIGNMENT, font=SCORE_FONT)

    def increase_score(self):
        self.clear()
        self.score += 1
        #  have to call self.write again otherwise it won't re-wrtie the score
        self.write(f"Score: {self.score}", move=False, align=ALIGNMENT, font=SCORE_FONT)

    def game_over(self):
        self.goto(x=0, y=0)
        self.write(f"GAME OVER", move=False, align=ALIGNMENT, font=GAME_OVER_FONT)
