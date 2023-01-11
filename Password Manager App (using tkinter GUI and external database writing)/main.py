from tkinter import *
import string
import random


# ================= GENERATE PASSWORD =================
def generate_password_click():
    lowers = string.ascii_lowercase
    uppers = string.ascii_uppercase
    digits = string.digits
    symbols = string.punctuation

    chars = [lowers, uppers, digits, symbols]
    password = []

    for list in chars:
        for i in range(random.randint(2, 8)):
            char_choice = random.choice(list)
            password.append(char_choice)

    random.shuffle(password)  # mix up the list of chars
    password = ''.join(password)

    password_input.insert(0, password)


# ================= STORE IN DB =================
def get_data_and_add():
    website = website_input.get()
    username = username_input.get()
    password = password_input.get()

    add(website, username, password)


def add(website, username, password):
    text_string = ' | '.join((website, username, password))

    with open("password_login_data.txt", "a") as file:
        file.write(f"{text_string}\n")


# ================= SANITY CHECKS =================


# ============== CREATE THE UI ===============
# create window
window = Tk()
window.minsize(width=500, height=250)  # set a min size so it's not just as small as components
window.title("Password Manager")
window.config(padx=30, pady=30)
window.configure(background='#fffcf7')

# creating label components
website_label = Label(text="Website:", font=("arial", 12, "normal"), bg="#fffcf7", fg="#555b6e")
website_label.grid(column=0, row=1, sticky="E")
website_label.config(padx=5, pady=5)

username_label = Label(text="Email / Username: ", font=("arial", 12, "normal"), bg="#fffcf7", fg="#555b6e")
username_label.grid(column=0, row=2, sticky="E")
username_label.config(padx=5, pady=5)

password_label = Label(text="Password: ", font=("arial", 12, "normal"), bg="#fffcf7", fg="#555b6e")
password_label.grid(column=0, row=3, sticky="E")
password_label.config(padx=5, pady=10)

# creating entry boxes
website_input = Entry(width=50, highlightcolor="#a1b5d8", highlightthickness=2, border=1)
website_input.grid(column=1, row=1, columnspan=2, sticky="EW")
website_input.focus()

username_input = Entry(width=50, highlightcolor="#a1b5d8", highlightthickness=2, border=1)
username_input.grid(column=1, row=2, columnspan=2, sticky="EW")

password_input = Entry(width=30, highlightcolor="#a1b5d8", highlightthickness=2, border=1)
password_input.grid(column=1, row=3, sticky="W")

# creating button components
add_button = Button(text="Add", bg="#c2d8b9", fg="#555b6e", command=get_data_and_add)
add_button.grid(row=4, column=1, columnspan=2, sticky="EW")

gen_pass_button = Button(text="Generate Password", bg="#c2d8b9", fg="#555b6e",
                         command=generate_password_click)  # give command when clicked
gen_pass_button.grid(row=3, column=2, sticky="E")

# create canvas and add padlock image
canvas = Canvas(window, bg="#fffcf7", height=200, width=200, highlightthickness=0, relief='ridge')
filename = PhotoImage(file="logo.png")
image = canvas.create_image(100, 100, anchor="center", image=filename)
canvas.grid(row=0, column=0, columnspan=3)

window.mainloop()
