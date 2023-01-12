from tkinter import *
from tkinter import messagebox
import random

BACKGROUND_COLOR = "#B1DDC6"



# ============== CREATE THE UI ===============
# create window
window = Tk()
# window.minsize(width=500, height=300)  # set a min size so it's not just as small as components
window.title("Flashy")
window.config(padx=50, pady=50)
window.configure(background=BACKGROUND_COLOR)

# create flashcard canvas
canvas = Canvas(window, bg=BACKGROUND_COLOR, height=526, width=800, highlightthickness=0, relief='ridge')
canvas.grid(row=0, column=0, columnspan=2)
card_image = PhotoImage(file="./Images/card_front.png")
card = canvas.create_image(400, 263, image=card_image)

# add text to flashcard
language_text = canvas.create_text(400, 150, text="Spanish", fill="black", font=("arial", 40, "italic"), anchor="center")
canvas.grid(row=0, column=0)

# add text to flashcard
word_text = canvas.create_text(400, 263, text="amigo", fill="black", font=("arial", 60, "bold"), anchor="center")
canvas.grid(row=0, column=0)

# create tick button
tick_image = PhotoImage(file="./Images/right.png")
tick_button = Button(window, bg=BACKGROUND_COLOR, image=tick_image, borderwidth=0)
tick_button.grid(row=1, column=0)

# create cross button
cross_image = PhotoImage(file="./Images/wrong.png")
cross_button = Button(window, bg=BACKGROUND_COLOR, image=cross_image, borderwidth=0)
cross_button.grid(row=1, column=1)


window.mainloop()