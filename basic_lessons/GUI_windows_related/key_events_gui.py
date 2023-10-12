from tkinter import *


def do_something(event):
    label_key.config(text=event.keysym)


window = Tk()

label_key = Label(window, font=("Helvetica", 100))
label_key.pack()

window.bind("<Key>", do_something)  # Calls the function passing an event

window.mainloop()
