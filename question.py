class Question:
    def __init__(self, text, choice_a, choice_b, choice_c, choice_d, correct_answer):
        self.text = text
        self.choices = {
            "a": choice_a,
            "b": choice_b,
            "c": choice_c,
            "d": choice_d
        }
        self.correct_answer = correct_answer

    def is_correct(self, selected):
        return selected.lower() == self.correct_answer.lower()
