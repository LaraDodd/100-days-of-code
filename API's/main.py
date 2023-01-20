from tkinter import *
import requests

#==========FUNCTIONS===========
def get_quote():
    initial_label.config(text="")
    response = requests.get(url="https://api.kanye.rest/")
    response.raise_for_status() # raise exception if error occurs
    quote_data = response.json()
    quote = quote_data["quote"]
    canvas.itemconfig(quote_text, text=quote)


#=============UI===============
window = Tk()
window.title("Kanye Says...")
window.config(padx=50, pady=50, bg="white")

#create canvas
canvas = Canvas(width=300, height=414, bg="white", highlightthickness=0)

#add background image to cnvas
background_img = PhotoImage(file="background.png")
canvas.create_image(150, 207, image=background_img)

# add quote text to canvas
quote_text = canvas.create_text(150, 207, text="...", width=250, font=("Arial", 25, "bold"),
                               fill="white")
# place canvas
canvas.grid(row=0, column=0)

#add photo to button, place button
kanye_img = PhotoImage(file="kanye.png")
kanye_button = Button(image=kanye_img, highlightthickness=0, command=get_quote, bg="white", border=0)
kanye_button.grid(row=1, column=0)

# add initial click me
initial_label = Label(text="Click my head^^^", font=("Arial", 10), fg="black", bg="white")
initial_label.grid(row=2, column=0)




window.mainloop()