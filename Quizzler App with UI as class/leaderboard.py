from tkinter.simpledialog import askstring
import pandas
from quiz_brain import QuizBrain


class Leaderboard:
    def __init__(self, quiz_object: QuizBrain):
        """Takes in quiz object and calls add to leaderboard method

        Args:
            quiz_object is an object created by the QuizBrain class which contains all quiz functionality"""
        self.quiz = quiz_object


    def add_to_leaderboard(self):
        """pop up asking user to enter name, checks for leaderboard csv, if doesn't exist, creates it and adds name
        and score. If exists, uses pandas to convert Name column in csv to list, checks if name on list, if it is,
        and current score larger than score in csv, replaces it. If name not in list, appends name and score to csv"""
        name = askstring('Name', 'What is your name?')

        try:
            leaderboard_df = pandas.read_csv("leaderboard.csv", index_col=False)
        except FileNotFoundError:
            first_row = {'Name': [name], 'Score': [self.quiz.score], }
            leaderboard_df = pandas.DataFrame.from_dict(first_row)
            leaderboard_df.to_csv("leaderboard.csv", index=False)
        else:
            name_list = leaderboard_df.Name.to_list()
            if name not in name_list:
                new_row = {'Name': name, 'Score': self.quiz.score, }
                leaderboard_df = leaderboard_df.append(new_row, ignore_index=True)
                leaderboard_df.to_csv("leaderboard.csv", index=False)

            else:
                name_row = leaderboard_df[leaderboard_df.Name == name]
                name_score = int(name_row.Score)
                if self.quiz.score > name_score:
                    leaderboard_df.loc[leaderboard_df.Name == name, "Score"] = self.quiz.score
                leaderboard_df.to_csv("leaderboard.csv", index=False)
