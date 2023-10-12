from tkinter import *
import time
import random

#  Kinda buggy but works... or sorta

WIDTH = 1200
HEIGHT = 800
x_velocity = random.randint(1, 5)
y_velocity = random.randint(1, 5)

window = Tk()

alien = PhotoImage(file="assets/alien.png")
space = PhotoImage(file="assets/cartoon_space.png")

canvas = Canvas(window, width=WIDTH, height=HEIGHT)
canvas.pack()

space_image = canvas.create_image(0, 0, image=space, anchor=NW)
alien_image = canvas.create_image(0, 0, image=alien, anchor=NW)

image_width = alien.width()
image_height = alien.height()

while True:
    coordinates = canvas.coords(alien_image)
    # print(coordinates)
    if coordinates[0] > (WIDTH-(image_width-5)) or coordinates[0] < 0:
        if x_velocity > 0:
            x_velocity = -(random.randint(1, 5))
            print(f"x = {x_velocity}")
        elif x_velocity < 0:
            x_velocity = random.randint(1, 5)
            print(f"x = {x_velocity}")
    if coordinates[1] > (HEIGHT-(image_height-5)) or coordinates[1] < 0:
        if y_velocity > 0:
            y_velocity = -(random.randint(1, 5))
            print(f"y = {y_velocity}")
        elif y_velocity < 0:
            y_velocity = random.randint(1, 5)
            print(f"y = {y_velocity}")
    canvas.move(alien_image, x_velocity, y_velocity)
    window.update()
    time.sleep(0.01)

window.mainloop()
