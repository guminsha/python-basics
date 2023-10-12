from tkinter import *


def create_window():
    # new_window = Toplevel() # Toplevel() = new window "on top" of other window, linked to a "bottom" window
    new_window = Tk()  # Tk() = New independent window
    old_window.destroy()  # close old window


old_window = Tk()

Button(old_window, text="New Window", command=create_window).pack()

old_window.mainloop()  # loops everything above this until it closes
