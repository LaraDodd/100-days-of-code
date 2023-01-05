import pandas
leaderboard_df = pandas.read_csv("leaderboard.csv")
print(leaderboard_df)
highscore = leaderboard_df.Score.astype(int).max()
print(highscore)
