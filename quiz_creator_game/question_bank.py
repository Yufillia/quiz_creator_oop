from question import Question

class QuestionBank:
    def __init__(self):
        self.questions = []

    def add_question(self, question):
        self.questions.append(question)

    def save_to_file(self, filename):
        with open(filename, "w", encoding="utf-8") as file:
            for q in self.questions:
                file.write(f"Question: {q.text}\n")
                file.write(f"a) {q.choices['a']}\n")
                file.write(f"b) {q.choices['b']}\n")
                file.write(f"c) {q.choices['c']}\n")
                file.write(f"d) {q.choices['d']}\n")
                file.write(f"Answer: {q.correct_answer}\n")
                file.write("---\n")

    def load_from_file(self, filename):
        self.questions.clear()
        try:
            with open(filename, "r", encoding="utf-8") as file:
                blocks = file.read().strip().split("---\n")
                for block in blocks:
                    lines = block.strip().split("\n")
                    if len(lines) < 6:
                        continue
                    question = Question(
                        lines[0].replace("Question: ", ""),
                        lines[1].replace("a) ", ""),
                        lines[2].replace("b) ", ""),
                        lines[3].replace("c) ", ""),
                        lines[4].replace("d) ", ""),
                        lines[5].replace("Answer: ", "").strip()
                    )
                    self.questions.append(question)
        except FileNotFoundError:
            pass
