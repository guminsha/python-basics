from tkinter import *
from Food import *
from Snake import *

GAME_WIDTH = 700
GAME_HEIGHT = 700
SPEED = 50
SPACE_SIZE = 50
BODY_PARTS = 3
SNAKE_COLOR = "#00FF00"
FOOD_COLOR = "#FF0000"
BACKGROUND_COLOR = "#000000"


def next_turn():
    pass


def change_direction(new_direction):
    pass


def game_over():
    pass


window = Tk()
window.title("Snake Game")
window.resizable(False, False)

score = 0
direction = "down"

label_score = Label(window, text=f"Score: {score}", font=("consolas", 40))
label_score.pack()

canvas = Canvas(window, bg=BACKGROUND_COLOR, height=GAME_HEIGHT, width=GAME_WIDTH)
canvas.pack()

window.update()

window_width = window.winfo_width()
window_height = window.winfo_height()
screen_width = window.winfo_screenwidth()
screen_height = window.winfo_screenheight()

x = int((screen_width / 2) - (window_width / 2))
y = int((screen_height / 2) - (window_height / 2))

window.geometry(f"{window_width}x{window_height}+{x}+{y}")

snake = Snake()
food = Food()

canvas.create_oval(food.coordinates[0], food.coordinates[1], food.coordinates[0] + SPACE_SIZE,
                   food.coordinates[1] + SPACE_SIZE, fill=FOOD_COLOR, tags="food")

window.mainloop()
