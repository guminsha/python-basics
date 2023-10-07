from tkinter import *


# entry widget = textbox that accepts a single line of user input

def submit():
    username = entry.get()
    print(f"Hello {username}!")
    entry.config(state=DISABLED)


def delete():
    entry.delete(0, END)


def backspace():
    entry.delete(len(entry.get()) - 1, END)


window = Tk()

entry = Entry(window,
              font=("Arial", 30),
              fg="#00FF00",
              bg="black",
              show="*")

# entry.insert(0, "Spongebob")
# entry.config(show="*")
# entry.config(state=DISABLE)

entry.pack(side=LEFT)

submit_button = Button(window,
                       text="Submit",
                       font=("Arial", 10),
                       relief=RAISED,
                       bd=5,
                       command=submit)
submit_button.pack(side=RIGHT)

delete_button = Button(window,
                       text="Delete",
                       font=("Arial", 10),
                       relief=RAISED,
                       bd=5,
                       command=delete)
delete_button.pack(side=RIGHT)

backspace_button = Button(window,
                          text="backspace",
                          font=("Arial", 10),
                          relief=RAISED,
                          bd=5,
                          command=backspace)
backspace_button.pack(side=RIGHT)

window.mainloop()
