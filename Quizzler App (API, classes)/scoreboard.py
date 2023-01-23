import pandas
class Scoreboard:
    def __init__(self):
        self.leader = None
        self.highscore = None
        self.get_highscore()

    def get_highscore(self):
        try:
            leaderboard_df = pandas.read_csv("leaderboard.csv")
        except FileNotFoundError:
            self.highscore = 0
        else:
            self.highscore = leaderboard_df.Score.astype(int).max()
            self.leader = leaderboard_df.query(f"Score=={self.highscore}").Name.item()
