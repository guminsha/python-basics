from tkinter import *

count = 0


def click():
    global count
    count += 1
    print(f"You clicked {count} times")


window = Tk()

photo = PhotoImage(file="assets/icon.png")

button = Button(window,
                text="Click here!",
                command=click,
                font=("Comic Sans", 30),
                fg="#00FF00",
                bg="black",
                activeforeground="#00FF00",
                activebackground="black",
                state=ACTIVE,
                image=photo,
                compound="bottom")
button.pack()

window.mainloop()
