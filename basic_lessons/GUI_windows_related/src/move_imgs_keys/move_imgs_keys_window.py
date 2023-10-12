from tkinter import *


def move_up(event):
    label.place(x=label.winfo_x(), y=label.winfo_y()-10)


def move_left(event):
    label.place(x=label.winfo_x()-10, y=label.winfo_y())


def move_down(event):
    label.place(x=label.winfo_x(), y=label.winfo_y()+10)


def move_right(event):
    label.place(x=label.winfo_x()+10, y=label.winfo_y())


windows = Tk()
windows.geometry("500x500")

windows.bind("<w>", move_up)
windows.bind("<a>", move_left)
windows.bind("<s>", move_down)
windows.bind("<d>", move_right)
windows.bind("<Up>", move_up)
windows.bind("<Left>", move_left)
windows.bind("<Down>", move_down)
windows.bind("<Right>", move_right)

car = PhotoImage(file="../assets/car.png")

label = Label(windows, image=car)
label.place(x=0, y=0)

windows.mainloop()
