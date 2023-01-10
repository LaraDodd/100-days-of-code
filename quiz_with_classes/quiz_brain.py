class QuizBrain:
    def __init__(self, question_list):
        self.question_number = 0
        self.question_list = question_list
        self.score = 0

    def still_has_questions(self):
        """returns a boolean value for whether there are any questions left to iterate through"""
        return len(self.question_list) > self.question_number
        # if len(self.question_list) > self.question_number:
        #     return True
        # else:
        #     return False

    def next_question(self):
        """adds to the question number counter,
        asks user to input answer to the current question
        contains check answer method with current question answer and user answer as inputs"""
        current_question = self.question_list[self.question_number]
        self.question_number += 1
        user_answer = input(f"Q{self.question_number} {current_question.timer_text} True or False? ")
        self.check_answer(user_answer, current_question.answer)

    def check_answer(self, user_answer, actual_answer):
        """compares user answer and actual answer, if equal, adds to score counter
        prints correct/wrong statements"""
        if user_answer.lower() == actual_answer.lower():
            self.score += 1
            print("Well done, that is right!!")
        else:
            print("Better luck next time...")
        print(f"The correct answer is {actual_answer}")
        print(f"Your current score is {self.score}/{self.question_number}")
        print("\n")
