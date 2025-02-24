from tkinter import *

BACKGROUND_COLOR = "#B1DDC6"


#Setting the window

window = Tk()
window.title("Flash Cards")
window.geometry("600x800")
window.maxsize(600, 800)
window.config(padx=50, pady=50, bg=BACKGROUND_COLOR)

#TODO. Setting the image background card

# Welcoming label

welcome = Label(text="Welcome to Flash Card", font=("Times New Roman", 20, "bold italic"), bg=BACKGROUND_COLOR)
welcome.grid(row=0, column=1, columnspan=2)

# to make space
label_space1= Label(borderwidth=0,highlightthickness=0,bg=BACKGROUND_COLOR)
label_space1.grid(row=1,column=0,columnspan=2)


my_image = PhotoImage(file="images/card_front.png")
button = Button(image=my_image,borderwidth=0,highlightthickness=0, height=350, width=400,)
button.grid(column=1, row=2, columnspan=2)

# This is just to make space to the right and move the all content to the middle
label_space2 = Entry(borderwidth=0,highlightthickness=0,bg=BACKGROUND_COLOR, width=9)
label_space2.grid(row=2,column=0)

#TODO. check and cancel buttons

# this label for spacing between the cards and buttons
label = Label(borderwidth=0,highlightthickness=0,bg=BACKGROUND_COLOR)
label.grid(row=3,column=0,columnspan=2)

right_image = PhotoImage(file="images/right.png")
right_button = Button(image=right_image,borderwidth=0,highlightthickness=0,height=60, width=60, pady=100)
right_button.grid(row=4,column=2)

wrong_image = PhotoImage(file="images/wrong.png")
wrong_button= Button(image=wrong_image,borderwidth=0,highlightthickness=0,height=60, width=60,pady=100,padx=50)
wrong_button.grid(row=4,column=1)



window.mainloop()
