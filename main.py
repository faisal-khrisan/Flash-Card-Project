from glob import translate
from tkinter import *
import pandas as pd
import random


BACKGROUND_COLOR = "#B1DDC6"

#----------------------------------load the data -------------------------------------------

data = pd.read_csv("data/Malay  - Sheet1.csv")

random_index = random.randint(0,500)

Malay_word = data["Malay"][random_index]
English_word = data["English"][random_index]


def next_word():
    index = random.randint(0, 500)

    global Malay_word, English_word
    Malay_word = data["Malay"][index]
    English_word = data["English"][index]
    Malay_and_English_label.config(text=Malay_word)
    Malay_English.config(text="Malay")


def translated_word():
    Malay_English.config(text="English")
    Malay_and_English_label.config(text=English_word.title())





#-------------------------------------------------------------------------------------
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
button = Button(image=my_image,borderwidth=0,highlightthickness=0, height=350, width=400,command=translated_word)
button.grid(column=1, row=2, columnspan=2)

# This is just to make space to the right and move the all content to the middle
label_space2 = Entry(borderwidth=0,highlightthickness=0,bg=BACKGROUND_COLOR, width=9)
label_space2.grid(row=2,column=0)

#TODO. check and cancel buttons

# this label for spacing between the cards and buttons
label = Label(borderwidth=0,highlightthickness=0,bg=BACKGROUND_COLOR)
label.grid(row=3,column=0,columnspan=2)

right_image = PhotoImage(file="images/right.png")
right_button = Button(image=right_image,borderwidth=0,highlightthickness=0,height=60, width=60, pady=100,command=next_word)
right_button.grid(row=4,column=2)

wrong_image = PhotoImage(file="images/wrong.png")
wrong_button= Button(image=wrong_image,borderwidth=0,highlightthickness=0,height=60, width=60,pady=100,padx=50,command=next_word)
wrong_button.grid(row=4,column=1)

# labels
Malay_English = Label(text="Malay", background="white",font=("New times roman","20","italic"))
Malay_English.place(x=220,y=160)
Malay_and_English_label = Label(text=Malay_word.title(),background="white",font=("New times roman","30","bold"))
Malay_and_English_label .grid(columnspan=2, column=1,row=2)
window.mainloop()



