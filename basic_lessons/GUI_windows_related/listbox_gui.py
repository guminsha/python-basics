# listbox = A listing of selectable text items within its own cantainer
from tkinter import *


def submit():
    print(f"You have ordered: {listbox.get(listbox.curselection())}")


def add():
    listbox.insert(listbox.size(), entry_box.get())
    listbox.config(height=listbox.size())


def delete():
    listbox.delete(listbox.curselection())
    listbox.config(height=listbox.size())


window = Tk()
window.columnconfigure(1, weight=1)

listbox = Listbox(window,
                  bg="#f7ffde",
                  font=("Constantia", 20),
                  width=12)
listbox.config(justify="center")
listbox.pack()

listbox.insert(1, "Pizza")
listbox.insert(2, "Pasta")
listbox.insert(3, "Garlic Bread")
listbox.insert(4, "Soup")
listbox.insert(5, "Salad")

listbox.config(height=listbox.size())

entry_box = Entry(window)
entry_box.pack()

submit_button = Button(window,
                       text="Submit",
                       command=submit)
submit_button.pack()

add_button = Button(window,
                    text="Add",
                    command=add)
add_button.pack()

delete_button = Button(window,
                    text="Delete",
                    command=delete)
delete_button.pack()

window.mainloop()
