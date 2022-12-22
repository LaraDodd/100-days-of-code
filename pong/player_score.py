from turtle import Turtle

# global constants
ALIGNMENT = 'center'
SCORE_FONT = ('Courier', 25, 'normal')
GAME_OVER_FONT = ('Courier', 25, 'bold')


class PlayerScore(Turtle):
    def __init__(self):
        super().__init__()
        self.score = 0
        self.goto(x=-100, y=270)
        self.hideturtle()
        self.color("white")
        self.write("{self.score}", move=False, align=ALIGNMENT, font=SCORE_FONT)

    def increase_score(self):
        self.clear()
        self.score += 1
        self.write("{self.score}", move=False, align=ALIGNMENT, font=SCORE_FONT)

    def game_over(self):
        self.color("gold")
        self.goto(x=0, y=0)
        self.write(f"GAME OVER", move=False, align=ALIGNMENT, font=GAME_OVER_FONT)

