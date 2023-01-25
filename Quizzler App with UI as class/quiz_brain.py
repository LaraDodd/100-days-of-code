import html

class QuizBrain:
    """this module contains all code realating to the functionality of the quiz. Pulling in next question, checking if
    answer correct, check if questions left"""

    def __init__(self, q_list: list):
        """initialises score and question number as 0. Initialises question list and current question.

        Args:
            q_list = a list of question objects"""
        self.question_number = 0
        self.score = 0
        self.question_list = q_list
        self.current_question = None

    def still_has_questions(self):
        """Checks if there are questions left by comparing question number to question list length

        Returns:
            Boolean indicating whether questions left"""
        return self.question_number < len(self.question_list)

    def next_question(self) -> str:
        """finds current question by using question number as index for question list, this returns current question as
        an object. Adds 1 to question number, uses html unescape to pull the question text, from the current question
         object as readable string.

         Returns:
             Question text as a string"""
        self.current_question = self.question_list[self.question_number]
        self.question_number += 1
        q_text = html.unescape(self.current_question.text)
        return f"Q.{self.question_number}: {q_text}"


    def check_answer(self, user_answer: str) -> bool:
        """Takes in user answer as param and pulls answer attribute from current_question object. If the user_answer
        and current_question answer are the same, returns True, else returns False.

        Args:
            user_answer - answer as string (either true or false)

        Returns:
            Boolean indicating whether answer is correct
        """
        correct_answer = self.current_question.answer
        if user_answer.lower() == correct_answer.lower():
            self.score += 1
            correct_answer = True
        else:
            correct_answer = False

        return correct_answer
