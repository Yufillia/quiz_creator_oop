import tkinter as tk
from tkinter import messagebox
import random
from question_bank import QuestionBank

class QuizRunnerGUI:
    def __init__(self):
        self.bank = QuestionBank()
        self.bank.load_from_file("quiz_data.txt")
        self.remaining = self.bank.questions.copy()

        self.root = tk.Tk()
        self.root.title("Quiz Program")

        self.current_question = None
        self.var = tk.StringVar(value="")

        self.setup_widgets()
        self.load_new_question()
        self.root.mainloop()

    def setup_widgets(self):
        self.question_label = tk.Label(self.root, text="", wraplength=400, font=("Arial", 14), justify="left")
        self.question_label.pack(pady=20)

        self.rb_buttons = {}
        for choice in ['a', 'b', 'c', 'd']:
            btn = tk.Radiobutton(self.root, text="", variable=self.var, value=choice, font=("Arial", 12))
            btn.pack(anchor="w", padx=20)
            self.rb_buttons[choice] = btn

        tk.Button(self.root, text="Submit Answer", command=self.check_answer).pack(pady=10)
        tk.Button(self.root, text="Next Question", command=self.load_new_question).pack(pady=5)
        tk.Button(self.root, text="Exit", command=self.root.destroy).pack(pady=5)

    def load_new_question(self):
        if not self.remaining:
            messagebox.showinfo("Quiz Finished", "You've answered all questions!")
            self.root.destroy()
            return

        self.current_question = random.choice(self.remaining)
        self.remaining.remove(self.current_question)

        self.question_label.config(text=self.current_question.text)
        self.var.set("")

        for key, btn in self.rb_buttons.items():
            btn.config(text=f"{key}) {self.current_question.choices[key]}")

    def check_answer(self):
        selected = self.var.get()
        if selected == "":
            messagebox.showwarning("No Answer", "Please select an answer.")
            return

        if selected == self.current_question.answer:
            messagebox.showinfo("Result", "Correct!")
        else:
            correct = self.current_question.answer
            messagebox.showinfo("Result", f"Wrong! Correct answer is: {correct}.")