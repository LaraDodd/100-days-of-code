from question_model import QuestionMaker
from data import question_data
from quiz_brain import QuizBrain

#  initialise empty list
question_object_list = []

#  iterates through each dictionary in the list, creates a question object containing text and answer
#  adds the question object to a list
for question in question_data:
    question_object = QuestionMaker(question["question"], question["correct_answer"])
    question_object_list.append(question_object)

quiz_object = QuizBrain(question_object_list)

while quiz_object.still_has_questions():
    quiz_object.next_question()

print(f"Final score: {quiz_object.score}/{quiz_object.question_number}")
