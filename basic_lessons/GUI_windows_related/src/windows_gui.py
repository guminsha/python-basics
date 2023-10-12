from tkinter import *

# widgets = GUI elements: buttons, textboxes, labels, images
# windows = serves as container to hold or contain these widgets

window = Tk()  # instantiate an instance of a window
window.geometry("1280x720")
window.title("First GUI program")

icon = PhotoImage(file="assets/icon.png")  # between Tk() and mainloop()
window.iconphoto(True, icon)

window.config(background="#4734ed")  # or color's name

window.mainloop()  # place window on computer screen, listen for events
