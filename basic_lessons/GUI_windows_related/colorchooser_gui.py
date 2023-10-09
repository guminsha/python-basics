from tkinter import *
from tkinter import colorchooser  # this is a submodule


def click():
    color = colorchooser.askcolor()  # assign color to a variable
    color_hex = color[1]            # assigns element at index 1 to a variable
    window.config(bg=str(color_hex))  # don't need to typecast but... yellow error


window = Tk()
window.geometry("420x420")

button = Button(text="Click me",
                command=click)
button.pack()

window.mainloop()
