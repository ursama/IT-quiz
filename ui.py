from tkinter import *
from quiz_brain import QuizBrain

THEME_COLOR = "#375362"


class QuizInterface:
    def __init__(self, quiz_brain: QuizBrain):
        self.quiz = quiz_brain
        self.window = Tk()
        self.window.title("Quizzler")
        self.window.config(padx=20, pady=20, bg=THEME_COLOR)

        self.score = Label(text="Score: 0/0", bg=THEME_COLOR, fg="white")
        self.score.grid(column=1, row=0)

        self.question = Canvas(width=300, height=250, bg="white")
        self.question_text = self.question.create_text(
            150,
            125,
            width=280,
            text="question",
            font=("Arial", 20, "italic"),
            fill=THEME_COLOR
        )
        self.question.grid(column=0, row=1, columnspan=2, pady=50)

        true_img = PhotoImage(file="./images/true.png")
        self.true_button = Button(image=true_img, highlightthickness=0, command=self.true_pressed)
        self.true_button.grid(column=0, row=2)

        false_img = PhotoImage(file="./images/false.png")
        self.false_button = Button(image=false_img, highlightthickness=0, command=self.false_pressed)
        self.false_button.grid(column=1, row=2)

        self.get_next_question()

        self.window.mainloop()

    def get_next_question(self):
        self.question.config(bg="white")
        if self.quiz.still_has_questions():
            q_text = self.quiz.next_question()
            self.question.itemconfig(self.question_text, text=q_text)
            self.true_button.config(state="normal")
            self.false_button.config(state="normal")
        else:
            self.question.itemconfig(
                self.question_text,
                text=f"You've finished.\nResult: {self.quiz.score}/10"
            )

    def true_pressed(self):
        is_right = self.quiz.check_answer("true")
        self.give_feedback(is_right)

    def false_pressed(self):
        is_right = self.quiz.check_answer("false")
        self.give_feedback(is_right)

    def give_feedback(self, is_right):
        if is_right:
            self.question.config(bg="green")
        else:
            self.question.config(bg="red")
        self.true_button.config(state="disabled")
        self.false_button.config(state="disabled")
        self.score.config(text=f"Score: {self.quiz.score}/10")
        self.window.after(1000, self.get_next_question)
