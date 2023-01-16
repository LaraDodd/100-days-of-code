from tkinter import *
from tkinter import messagebox
import random

BACKGROUND_COLOR = "#B1DDC6"


# ================ PULLING DATA AND UPDATING FLASHCARD =================
def choose_word():
    with open("./Data/Spanish 500 frequency dict words - Sheet1.csv", "r") as words_file:
        words = words_file.readlines()

    word_choice = random.choice(words)
    print(word_choice)
    words_in_list = word_choice.split(",")
    return words_in_list


def update_flashcard():
    word = choose_word()
    spanish_word = word[0]
    english_word = word[1]

    canvas.itemconfig(word_text, text=spanish_word)
    flip_timer(english_word)
    return ','.join(word)


def tick_clicked():
    word = update_flashcard()
    with open("./Data/Spanish 500 frequency dict words - Sheet1.csv", "r") as words_file:
        data = words_file.read()
    new_data = data.replace(word, "")
    with open("./Data/Spanish 500 frequency dict words - Sheet1.csv", "w") as words_file:
        words_file.write(new_data)
    with open("./Data/Known words", "a") as known_words_file:
        known_words_file.write(f"{word}")


def cross_clicked():
    canvas.itemconfig(card, image=front_card_image)
    canvas.itemconfig(language_text, text="Spanish")
    update_flashcard()


def flipcard(word):
    canvas.itemconfig(card, image=back_card_image)
    canvas.itemconfig(language_text, text="English", fill="white")
    canvas.itemconfig(word_text, text=word, fill="white")


def flip_timer(word):
    window.after(3000, flipcard, word)


# ============== CREATE THE UI ===============
# create window
window = Tk()
# window.minsize(width=500, height=300)  # set a min size so it's not just as small as components
window.title("Flashy")
window.config(padx=20, pady=20)
window.configure(background=BACKGROUND_COLOR)

# create flashcard canvas
canvas = Canvas(window, bg=BACKGROUND_COLOR, height=526, width=800, highlightthickness=0, relief='ridge')
canvas.grid(row=0, column=0, columnspan=2)
front_card_image = PhotoImage(file="./Images/card_front.png")
back_card_image = PhotoImage(file="./Images/card_back.png")
card = canvas.create_image(400, 263, image=front_card_image)

# add text to flashcard
language_text = canvas.create_text(400, 150, text="Spanish", fill="black", font=("arial", 40, "italic"),
                                   anchor="center")
canvas.grid(row=0, column=0)

# add text to flashcard
word_text = canvas.create_text(400, 263, text="amigo", fill="black", font=("arial", 60, "bold"), anchor="center")
canvas.grid(row=0, column=0)

# create tick button
tick_image = PhotoImage(file="./Images/right.png")
tick_button = Button(window, bg=BACKGROUND_COLOR, image=tick_image, borderwidth=0, command=tick_clicked)
tick_button.grid(row=1, column=0)

# create cross button
cross_image = PhotoImage(file="./Images/wrong.png")
cross_button = Button(window, bg=BACKGROUND_COLOR, image=cross_image, borderwidth=0, command=cross_clicked)
cross_button.grid(row=1, column=1)



window.mainloop()
