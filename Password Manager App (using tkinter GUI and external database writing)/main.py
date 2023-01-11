from tkinter import *

#============== CREATE THE UI ===============
# create window
window = Tk()
window.minsize(width=500, height=250)  # set a min size so it's not just as small as components
window.title("Password Manager")
window.config(padx=30, pady=30)
window.configure(background='#fffcf7')

# creating label components
website_label = Label(text="Website:", font=("arial", 12, "normal"), bg="#fffcf7", fg="#738290")
website_label.grid(column=0, row=1, sticky="E")
website_label.config(padx=5, pady=5)

username_label = Label(text="Email/Username: ", font=("arial", 12, "normal"), bg="#fffcf7", fg="#738290")
username_label.grid(column=0, row=2, sticky="E")
username_label.config(padx=5, pady=5)

password_label = Label(text="Password: ", font=("arial", 12, "normal"), bg="#fffcf7", fg="#738290")
password_label.grid(column=0, row=3, sticky="E")
password_label.config(padx=5, pady=5)

# creating entry boxes
website_input = Entry(width=50, highlightcolor="#a1b5d8", highlightthickness=2, border=1)
website_input.grid(column=1, row=1)

username_input = Entry(width=50, highlightcolor="#a1b5d8", highlightthickness=2, border=1)
username_input.grid(column=1, row=2)

password_input = Entry(width=25, highlightcolor="#a1b5d8", highlightthickness=2, border=1)
password_input.grid(column=1, row=3, sticky="W")

# creating button component
add_button = Button(text="Add", bg="#c2d8b9", fg="#738290")  # give command when clicked
add_button.grid(row=4, column=1, columnspan=2, sticky="EW")

# create canvas and add padlock image
canvas = Canvas(window, bg="#fffcf7", height=200, width=190, highlightthickness=0, relief='ridge')
filename = PhotoImage(file="logo.png")
image = canvas.create_image(100, 112, anchor="center", image=filename)
canvas.grid(row=0, column=0, columnspan=2)











window.mainloop()
