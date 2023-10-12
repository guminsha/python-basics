from tkinter import *
import time
import random

WIDTH = 1200
HEIGHT = 800
x_velocity = random.randint(1, 5)
y_velocity = random.randint(1, 5)

window = Tk()
window.resizable(False, False)

alien = PhotoImage(file="assets/alien.png")
space = PhotoImage(file="assets/cartoon_space.png")

canvas = Canvas(window, width=WIDTH, height=HEIGHT)
canvas.pack()

space_image = canvas.create_image(0, 0, image=space, anchor=NW)
alien_image = canvas.create_image(0, 0, image=alien, anchor=NW)

image_width = alien.width()
image_height = alien.height()

label_coordinates = Label(canvas, font=("DS-Digital", 15))
label_coordinates.place(x=1000, y=50)
label_speed = Label(canvas, font=("DS-Digital", 15))
label_speed.place(x=950, y=80)

while True:
    coordinates = canvas.coords(alien_image)
    label_coordinates.config(text=f"X: {int(coordinates[0])} Y: {int(coordinates[1])}")
    label_speed.config(text=f"Speed X: {x_velocity} Speed Y: {y_velocity}")

    if coordinates[0] > (WIDTH-(image_width-5)):
        x_velocity = -(random.randint(1, 5))
    if coordinates[0] < 0:
        x_velocity = random.randint(1, 5)
    if coordinates[1] > (HEIGHT-(image_height-5)):
        y_velocity = -(random.randint(1, 5))
    if coordinates[1] < 0:
        y_velocity = random.randint(1, 5)
    canvas.move(alien_image, x_velocity, y_velocity)
    window.update()
    time.sleep(0.01)

window.mainloop()
