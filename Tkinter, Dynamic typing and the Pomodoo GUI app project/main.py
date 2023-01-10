from tkinter import *
import math

# ---------------------------- GLOBAL CONSTANTS ------------------------------- #
PINK = "#e2979c"
RED = "#e7305b"
GREEN = "#9bdeac"
YELLOW = "#f7f5dd"
FONT_NAME = "Courier"
WORK_MIN = 25
SHORT_BREAK_MIN = 5
LONG_BREAK_MIN = 20
REPS = 1


# ---------------------------- TIMER RESET ------------------------------- #
def restart():
    if REPS % 2 != 0 and REPS < 8:
        minutes = WORK_MIN
        break_type_label.config(text="Work!")
    elif REPS < 8:
        minutes = SHORT_BREAK_MIN
        break_type_label.config(text="Break!")
    elif REPS == 8:
        minutes = LONG_BREAK_MIN
        break_type_label.config(text="LOOOOOOONG BREAK!")
    else:
        minutes = "00"
        break_type_label.config(text="DONE")

    add_check()
    canvas.itemconfig(text, text=f"{minutes}:00")


def reset():
    global REPS
    REPS = 1
    break_type_label.config(text="")
    canvas.itemconfig(text, text=f"00:00")
    check_label.config(text="")


def add_check():
    global REPS
    if REPS >= 8:
        check_label.config(text="✔✔✔✔")
    elif REPS > 6:
        check_label.config(text="✔✔✔")
    elif REPS > 4:
        check_label.config(text="✔✔")
    elif REPS > 2:
        check_label.config(text="✔")


# ---------------------------- TIMER ------------------------------- #
def start_timer():
    global REPS

    if REPS % 2 != 0 and REPS < 8:
        minutes = WORK_MIN
    elif REPS < 8:
        minutes = SHORT_BREAK_MIN
    elif REPS == 8:
        minutes = LONG_BREAK_MIN
    else:
        restart()

    update_time(minutes=minutes - 1, seconds=0)


# ---------------------------- COUNTDOWN ------------------------------- #
def update_time(seconds, minutes):
    if seconds < 0:
        seconds = 59

    pretty_seconds = seconds
    if seconds < 10:
        pretty_seconds = "0" + str(seconds)

    pretty_minutes = math.ceil(minutes)
    if pretty_minutes < 0:
        global REPS
        REPS += 1
        restart()

        print(REPS)

        return

    if minutes < 9:
        pretty_minutes = "0" + str(math.ceil(minutes))

    window.after(1, update_time, seconds - 1, minutes - (1 / 60))
    canvas.itemconfig(text, text=f"{pretty_minutes}:{pretty_seconds}")


# ---------------------------- UI SETUP ------------------------------- #

window = Tk()
window.title("Pomodoro Clock")
window.config(padx=100, pady=100)
window.configure(background=YELLOW)

# timer label
label = Label(fg=GREEN, text="Timer", font=("courier", 40, "bold"), bg=YELLOW)
label.config(pady=10, padx=10)
label.grid(row=0, column=1, sticky="EW")

# create canvas and add tomato image
canvas = Canvas(window, bg=YELLOW, height=224, width=200, highlightthickness=0, relief='ridge')
filename = PhotoImage(file="tomato.png")
image = canvas.create_image(100, 112, anchor="center", image=filename)
canvas.grid(row=1, column=1)

# add text
text = canvas.create_text(100, 130, text=f"00:00", fill="white", font=("courier", 25, "bold"), anchor="center")
canvas.grid(row=1, column=1)

# add buttons
# lambda allows you to call functions with parameters
start_button = Button(window, text="Start", bg="White", command=start_timer)
start_button.grid(row=2, column=0)

reset_button = Button(window, text="Reset", bg="White", command=reset)
reset_button.grid(row=2, column=2)

# add check labels
check_label = Label(window, text="", font=("courier", 20, "bold"), bg=YELLOW, fg=GREEN)
check_label.grid(row=3, column=1)

# add info label
break_type_label = Label(window, text="", font=("courier", 15, "bold"), bg=YELLOW, fg=PINK)
break_type_label.grid(row=4, column=1, sticky="EW")

window.mainloop()
