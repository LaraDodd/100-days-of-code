class Question:
    """Creates a question object which contains question text and question answer"""

    def __init__(self, q_text: str, q_answer: str) -> None:
        """Takes in q_text and q_answer and creates question object with these parameters

        Args:
            q_text - string containing question text
            q_answer - string containing question answer"""
        self.text = q_text
        self.answer = q_answer
