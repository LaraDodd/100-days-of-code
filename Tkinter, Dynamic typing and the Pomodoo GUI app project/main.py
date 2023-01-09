from tkinter import *
import time

# ---------------------------- GLOBAL CONSTANTS ------------------------------- #
PINK = "#e2979c"
RED = "#e7305b"
GREEN = "#9bdeac"
YELLOW = "#f7f5dd"
FONT_NAME = "Courier"
WORK_MIN = 25
SHORT_BREAK_MIN = 5
LONG_BREAK_MIN = 20


# ---------------------------- TIMER RESET ------------------------------- #
def reset_button():
    min = 25


# clear canvas and update

# ---------------------------- TIMER MECHANISM ------------------------------- #




def update_time(seconds):
    print(seconds)
    window.after(1000, update_time, seconds-1)


    # canvas.delete()
    # canvas.create_text(100, 130, text=f"{str(minutes)}:{str(seconds)}", fill="white", font=("courier", 25, "bold"),
    #                    anchor="center")





# ---------------------------- COUNTDOWN MECHANISM ------------------------------- #
def update_checks():
    checks = 1
    check_label.config(text=checks)


# ---------------------------- UI SETUP ------------------------------- #

window = Tk()
window.title("Pomodoro Clock")
window.config(padx=100, pady=100)
window.configure(background=YELLOW)

#timer label
label = Label(fg=GREEN, text="Timer", font=("courier", 40, "bold"), bg=YELLOW)
label.config(pady=10, padx=10)
label.grid(row=0, column=1, sticky="EW")

# create canvas and add tomato image
canvas = Canvas(window, bg=YELLOW, height=224, width=200, highlightthickness=0, relief='ridge')
filename = PhotoImage(file="tomato.png")
image = canvas.create_image(100, 112, anchor="center", image=filename)
canvas.grid(row=1, column=1)

# add text
sec = "00"
min = "00"
text = canvas.create_text(100, 130, text=f"{min}:{sec}", fill="white", font=("courier", 25, "bold"), anchor="center")
canvas.grid(row=1, column=1)

# add buttons
start_button = Button(window, text="Start", bg="White")
start_button.grid(row=2, column=0)

reset_button = Button(window, text="Reset", bg="White")
reset_button.grid(row=2, column=2)

#add check labels
check_label = Label(window, text="✔", font=("courier", 20, "bold"), bg=YELLOW, fg=GREEN)
check_label.grid(row=3, column=1)




window.mainloop()



update_time(seconds)





