from tkinter import *


def button_clicked():
    m_input = input.get()
    km = round(float(m_input) * 1.6, 2)
    l3.config(text=km)


# create window
window = Tk()
# window.minsize(width=500, height=500)  # set a min size so it's not just as small as components
window.title("Km to Mile converter")
window.config(padx=30, pady=30)

# creating label component
mile_l = Label(text="miles", font=("arial", 10))
mile_l.grid(column=2, row=0)  # have to give the components a position in order for them to appear on the window
mile_l.config(pady=10, padx=10)

# create entry box component
input = Entry(width=10)
input.grid(column=0, row=0, columnspan=2, sticky="EW")

# creating label component
l2 = Label(text="is equal to", font=("arial", 10))
l2.grid(column=0, row=1)  # have to give the components a position in order for them to appear on the window
l2.config(pady=10, padx=10)

# creating label component
l3 = Label(text="0", font=("arial", 10))
l3.grid(column=1, row=1)  # have to give the components a position in order for them to appear on the window
l3.config(pady=10, padx=10)

# creating label component
l4 = Label(text="km", font=("arial", 10))
l4.grid(column=2, row=1)  # have to give the components a position in order for them to appear on the window
l4.config(pady=10, padx=10)

# creating button component
button = Button(text="convert", command=button_clicked)  # give command when clicked
button.grid(column=0, row=3, columnspan=3, sticky="EW")

window.mainloop()
