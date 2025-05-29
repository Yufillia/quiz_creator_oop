import tkinter as tk
from tkinter import messagebox
from question import Question
from question_bank import QuestionBank

class QuizCreatorGUI:
    def __init__(self):
        self.bank = QuestionBank()

        self.root = tk.Tk()
        self.root.title("Quiz Creator GUI")

        self.setup_widgets()
        self.root.mainloop()

    def setup_widgets(self):
        tk.Label(self.root, text="Question:").grid(row=0, column=0, sticky="w")
        self.entry_question = tk.Entry(self.root, width=50)
        self.entry_question.grid(row=0, column=1)

        labels = ["Choice a:", "Choice b:", "Choice c:", "Choice d:"]
        self.entries = {}
        for i, label in enumerate(labels):
            tk.Label(self.root, text=label).grid(row=i+1, column=0, sticky="w")
            entry = tk.Entry(self.root)
            entry.grid(row=i+1, column=1)
            self.entries[chr(97+i)] = entry

        tk.Label(self.root, text="Correct Answer (a/b/c/d):").grid(row=5, column=0, sticky="w")
        self.answer_var = tk.StringVar()
        tk.Entry(self.root, textvariable=self.answer_var).grid(row=5, column=1)

        tk.Button(self.root, text="Save Question", command=self.save_question).grid(row=6, column=0, pady=10)
        tk.Button(self.root, text="❌ Exit & Save to File", command=self.save_and_exit).grid(row=6, column=1)

    def save_question(self):
        text = self.entry_question.get()
        a = self.entries['a'].get()
        b = self.entries['b'].get()
        c = self.entries['c'].get()
        d = self.entries['d'].get()
        answer = self.answer_var.get().lower()

        if not text or not all([a, b, c, d]) or answer not in ['a', 'b', 'c', 'd']:
            messagebox.showerror("Error", "Please fill all fields correctly.")
            return

        question = Question(text, a, b, c, d, answer)
        self.bank.add_question(question)

        self.entry_question.delete(0, tk.END)
        for entry in self.entries.values():
            entry.delete(0, tk.END)
        self.answer_var.set("")

        messagebox.showinfo("Saved", "Question saved!")

    def save_and_exit(self):
        self.bank.save_to_file("quiz_data.txt")
        self.root.destroy()