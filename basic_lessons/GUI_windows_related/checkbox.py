from tkinter import *


def display():
    if x.get():
        print("You agree!")
    else:
        print("You don't agree :(")


window = Tk()

x = BooleanVar()
# x = StringVar()
# x = IntVar() # Default is 1 or 0
photo = PhotoImage(file="src/icon.png")

checkbox = Checkbutton(window,
                       text="I agree to something",
                       variable=x,
                       onvalue=True,
                       offvalue=False,
                       command=display,
                       font=("Arial", 20),
                       fg="#00FF00",
                       bg="black",
                       activeforeground="#00FF00",
                       activebackground="black",
                       padx=25,
                       pady=10,
                       image=photo,
                       compound="left")
checkbox.pack()

window.mainloop()
