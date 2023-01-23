class QuizBrain:

    def __init__(self, q_list):
        self.question_number = 0
        self.score = 0
        self.question_list = q_list
        self.current_question = self.question_list[0]

    def still_has_questions(self) -> bool:
        return self.question_number < len(self.question_list)

    def next_question(self, user_answer):
        self.current_question = self.question_list[self.question_number]
        self.question_number += 1
        self.answer_correct(user_answer)

    def answer_correct(self, user_answer):
        correct_answer = self.current_question.answer
        if user_answer.lower() == correct_answer.lower():
            self.score += 1
            print(f"{self.question_number} {self.current_question.text}, answer is {correct_answer}, well done")

        else:
            print(f"{self.question_number} {self.current_question.text}, answer is {correct_answer}, unlucky!")

    def score(self):
        print(f"Your current score is: {self.score}/{self.question_number}")
        print("\n")
