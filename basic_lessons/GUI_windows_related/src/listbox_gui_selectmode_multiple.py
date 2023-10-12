# listbox = A listing of selectable text items within its own cantainer
from tkinter import *


def submit():
    food = []

    for index in listbox.curselection():
        food.insert(index, listbox.get(index))
    # print(f"You have ordered: {food}")

    for index in food:
        print(index)


def add():
    listbox.insert(listbox.size(), entry_box.get())
    listbox.config(height=listbox.size())


def delete():
    for index in reversed(listbox.curselection()):  # the index changes if starts normally (index 2 becomes 1 after
        listbox.delete(index)  # first delete)
    listbox.config(height=listbox.size())


window = Tk()
window.columnconfigure(1, weight=1)

listbox = Listbox(window,
                  bg="#f7ffde",
                  font=("Constantia", 20),
                  width=12,
                  selectmode=MULTIPLE)
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
