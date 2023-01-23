import pandas
class Scoreboard:
    def __init__(self):
        self.get_highscore()

    def get_highscore(self):
        try:
            leaderboard_df = pandas.read_csv("leaderboard.csv")
            self.highscore = leaderboard_df.Score.astype(int).max()
        except FileNotFoundError:
            self.highscore = 0