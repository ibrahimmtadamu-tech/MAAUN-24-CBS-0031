from datetime import datetime

class Question:
    def __init__(self, question, options, answer):
        self.question = question
        self.options = options
        self.answer = answer

    def check_answer(self, user_answer):
        return user_answer == self.answer


class Result:
    def __init__(self, score):
        self.score = score
        self.time = datetime.now()

    def get_result(self):
        return f"Score: {self.score} | Submitted at {self.time}"