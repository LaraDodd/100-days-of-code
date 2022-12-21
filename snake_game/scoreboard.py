from turtle import Turtle


class Scoreboard(Turtle):
    def __init__(self):
        super().__init__()
        self.score = 0
        self.goto(x=0, y=270)
        self.hideturtle()
        self.color("white")
        self.write(f"Score: {self.score}", move=False, align='center', font=('Arial', 20, 'normal'))


    def add(self):
        self.clear()
        self.score += 1
        #  have to call self.write again otherwise it won't re-wrtie the score
        self.write(f"Score: {self.score}", move=False, align='center', font=('Arial', 20, 'normal'))


