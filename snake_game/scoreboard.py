from turtle import Turtle

# global constants
ALIGNMENT = 'center'
SCORE_FONT = ('Courier', 15, 'normal')
GAME_OVER_FONT = ('Courier', 25, 'bold')


class Scoreboard(Turtle):
    def __init__(self):
        super().__init__()
        self.score = 0
        self.high_score = None
        self.find_high_score()
        self.goto(x=0, y=270)
        self.hideturtle()
        self.color("white")
        self.write(f"Score: {self.score} High Score {self.high_score}", move=False, align=ALIGNMENT, font=SCORE_FONT)

    def find_high_score(self):
        with open("score_data", "r") as scores:
            highscores = []
            for line in scores:
                highscores.append(line)

        highscores = highscores[1:]  # slice first line off

        # edits the list in place, otherwise you would have to go through every value in highscores
        # and strip it and then int() it and THEN append it to a new list
        formatted_highscores = [int(s.strip('\n')) for s in highscores]

        self.high_score = max(formatted_highscores)

    def update_scoreboard(self):
        self.clear()
        #  have to call self.write again otherwise it won't re-wrtie the score
        self.write(f"Score: {self.score} High Score {self.high_score}", move=False, align=ALIGNMENT, font=SCORE_FONT)

    def increase_score(self):
        self.score += 1
        self.update_scoreboard()

    def reset_score(self):
        """checks if score is a high score and adds score to high score variable if it is
        resets score to zero and updates scoreboard"""
        if self.score > self.high_score:
            self.high_score = self.score
            self.write_to_score_data()
        self.score = 0
        self.update_scoreboard()


    def write_to_score_data(self):
        with open("score_data", "a") as scores:
            scores.write(f"{self.high_score}")


    def game_over(self):
        self.color("gold")
        self.goto(x=0, y=0)
        self.write(f"GAME OVER", move=False, align=ALIGNMENT, font=GAME_OVER_FONT)
