from turtle import Turtle

# global constants
ALIGNMENT = 'center'
SCORE_FONT = ('Courier', 25, 'bold')
GAME_OVER_FONT = ('Courier', 25, 'bold')


class PlayerScore(Turtle):
    def __init__(self):
        super().__init__()
        self.score = 0
        self.goto(x=-100, y=250)
        self.hideturtle()
        self.color("white")
        self.write(f"{self.score}", move=False, align=ALIGNMENT, font=SCORE_FONT)


    def increase_score(self):
        self.clear()
        self.score += 1
        self.write(f"{self.score}", move=False, align=ALIGNMENT, font=SCORE_FONT)

    def win(self):
        self.color("gold")
        self.goto(x=0, y=0)
        self.write(f"YOU WIN", move=False, align=ALIGNMENT, font=GAME_OVER_FONT)

