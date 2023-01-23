from tkinter import *

def true_ticked() -> str:
    return "True"

def false_ticked() -> str:
    return "False"


THEME_COLOR = "#375362"

window = Tk()
window.title("Quizzle")
window.minsize(500, 500)
window.config(padx=50, pady=50, bg=THEME_COLOR)

canvas = Canvas(width=600, height=526, bg=THEME_COLOR, highlightthickness=0)
quiz_bg_img = PhotoImage(file="images/speech.png")
canvas_background = canvas.create_image(300, 263, image=quiz_bg_img)
card_title = canvas.create_text(300, 100, text="question 1", font=("Ariel", 25, "italic"))
canvas.grid(row=0, column=0, columnspan=2)


cross_image = PhotoImage(file="images/false.png")
wrong_button = Button(image=cross_image, highlightthickness=0)
wrong_button.config(pady=20, padx=20)
wrong_button.grid(row=1, column=0)


check_image = PhotoImage(file="images/true.png")
right_button = Button(image=check_image, highlightthickness=0)
right_button.grid(row=1, column=1)

window.mainloop()

