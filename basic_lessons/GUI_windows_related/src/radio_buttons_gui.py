# radio button = similar to checkbox, but you can only select one from a group

from tkinter import *

food = ["Pizza", "Hamburger", "Hotdog"]


def order():
    if x.get() == 0:
        print("Your ordered a Pizza")
    elif x.get() == 1:
        print("Your ordered a Hamburger")
    elif x.get() == 2:
        print("Your ordered a Hotdog")
    else:
        print("How?")


window = Tk()
window.title("Radio Buttons")

pizza_image = PhotoImage(file="assets/pizza.png")
hamburger_image = PhotoImage(file="assets/hamburger.png")
hotdog_image = PhotoImage(file="assets/hotdog.png")

food_images = [pizza_image, hamburger_image, hotdog_image]

x = IntVar()

for index in range(len(food)):
    radio_button = Radiobutton(window,
                               text=food[index],  # adds text to radiobutton
                               variable=x,  # groups radiobutton together if they share the same variable
                               value=index,  # assigns each radio button a different value
                               padx=25,  # adds padding on x-axis
                               font=("Impact", 20),  # changes font
                               image=food_images[index],  # adds image to radiobutton
                               compound="left",
                               indicatoron=False,  # changes "radio" to push buttons
                               width=300,
                               command=order)  # set command of radiobutton to function
    radio_button.pack(anchor=W)

window.mainloop()
