from tkinter import *


def do_something(event):
    print("Mouse coordenates: " + str(event.x) + "," + str(event.y))


window = Tk()

# window.bind("<Button-1>", do_something)  # Left mouse click
# window.bind("<Button-2>", do_something)  # Scroll wheel click
# window.bind("<Button-3>", do_something)  # Right mouse click
# window.bind("<ButtonRelease>", do_something)
# window.bind("<Enter>", do_something)  # When the mouse enter window
# window.bind("<Leave>", do_something)  # When the mouse leave window
# window.bind("<Motion>", do_something)  # While mouse is moving inside window

window.mainloop()
