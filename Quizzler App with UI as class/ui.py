THEME_COLOR = "#375362"
from tkinter import *
from quiz_brain import QuizBrain

class QuizInterface():
    def __init__(self, quiz_object: QuizBrain):
        self.quiz = quiz_object


        self.window = Tk()
        self.window.title("Quizzle")
        self.window.minsize(500, 400)
        self.window.config(padx=20, pady=20, bg=THEME_COLOR)

        self.canvas = Canvas(width=600, height=500, bg=THEME_COLOR, highlightthickness=0)
        quiz_bg_img = PhotoImage(file="images/speech.png")
        self.canvas_background = self.canvas.create_image(300, 263, image=quiz_bg_img)
        self.quiz_text = self.canvas.create_text(300,
                                                 200,
                                                 text="",
                                                 font=("Ariel", 20, "italic"),
                                                 width=350)
        self.canvas.grid(row=1, column=0, columnspan=2)

        cross_image = PhotoImage(file="images/false.png")
        wrong_button = Button(image=cross_image, highlightthickness=0, command=self.false_selected) # , command=false_ticked
        wrong_button.grid(row=2, column=0)

        check_image = PhotoImage(file="images/true.png")
        right_button = Button(image=check_image, highlightthickness=0, command=self.true_selected) # , command=true_ticked
        right_button.grid(row=2, column=1)

        self.get_next_question()

        #you can't call specific attributes from a passed in class, you can only call functions from it


        self.window.mainloop()

    # call next question from quiz brain. This returns the question as a string
    def get_next_question(self):
        q_text = self.quiz.next_question()
        self.canvas.itemconfig(tagOrId=self.quiz_text, text=q_text)

    def false_selected(self):
        q_text = self.quiz.next_question()
        self.canvas.itemconfig(tagOrId=self.quiz_text, text=q_text)
        is_correct = self.quiz.check_answer(user_answer="false")
        if is_correct:
            self.flash_green()
        else:
            self.flash_red()

    def true_selected(self):
        q_text = self.quiz.next_question()
        self.canvas.itemconfig(tagOrId=self.quiz_text, text=q_text)
        is_correct = self.quiz.check_answer(user_answer="true")
        if is_correct:
            self.flash_green()
        else:
            self.flash_red()

    def go_blue(self):
        self.canvas.config(bg=THEME_COLOR)
        self.window.config(bg=THEME_COLOR)

    def flash_green(self):
        self.canvas.config(bg="green")
        self.window.config(bg="green")
        self.window.after(100, self.go_blue)

    def flash_red(self):
        self.canvas.config(bg="red")
        self.window.config(bg="red")
        self.window.after(100, self.go_blue)





