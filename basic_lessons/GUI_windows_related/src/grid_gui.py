from tkinter import *

# grid() = geometry manager that organizes widgets in table-like structures in a parent

window = Tk()
title_label = Label(window, text="Enter your info:", font=("Arial", 20)).grid(row=0, column=0, columnspan=2)

first_name_label = Label(window, text="First name: ", width=20, bg="red").grid(row=1, column=0)
first_name_entry = Entry(window).grid(row=1, column=1)

last_name_label = Label(window, text="Last name: ", bg="green").grid(row=2, column=0)
last_name_entry = Entry(window).grid(row=2, column=1)

email_label = Label(window, text="E-mail: ", width=30, bg="blue").grid(row=3, column=0)
email_entry = Entry(window).grid(row=3, column=1)

submit_button = Button(window, text="Submit").grid(row=4, column=0, columnspan=2)  # columnspan takes both column and
# merge into one


window.mainloop()
