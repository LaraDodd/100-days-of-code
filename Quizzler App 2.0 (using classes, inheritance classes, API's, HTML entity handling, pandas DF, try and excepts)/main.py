from question_model import Question
from data import question_data
from quiz_brain import QuizBrain
from ui import QuizInterface

# create list of question objects using Question class from question model module
question_bank = []
for question in question_data:
    question_text = question["question"]
    question_answer = question["correct_answer"]
    new_question = Question(question_text, question_answer)
    question_bank.append(new_question)

# create quiz object from QuizBrain class with list of question objects as input
quiz = QuizBrain(question_bank)

# create quiz ui object from QuizInterface class with quiz object as input
quiz_ui = QuizInterface(quiz)
