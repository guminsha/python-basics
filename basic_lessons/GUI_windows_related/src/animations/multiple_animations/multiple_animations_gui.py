from tkinter import *
import time
from ball import *


WIDTH = 500
HEIGHT = 500

window = Tk()
window.resizable(False, False)

canvas = Canvas(window, width=WIDTH, height=HEIGHT)
canvas.pack()

volley_ball = Ball(canvas, 0, 0, 100, 1, 2, "white")
tennis_ball = Ball(canvas, 0, 0, 50, 4, 3, "yellow")
basket_ball = Ball(canvas, 0, 0, 125, 8, 7, "orange")
bowling_ball = Ball(canvas, 0, 0, 80, 2, 3, "black")

while True:
    volley_ball.move()
    tennis_ball.move()
    basket_ball.move()
    bowling_ball.move()
    window.update()
    time.sleep(0.01)

window.mainloop()
