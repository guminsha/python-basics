import random

FOOD_COLOR = "#FF0000"


class Food:
    def __init__(self, canvas, game_width, game_height, space_size):
        x = (random.randint(0, int(game_width / space_size) - 1) * space_size)  # (700/50) -1 * 50
        y = (random.randint(0, int(game_height / space_size) - 1) * space_size)  # (700/50) -1 * 50
        self.food_color = FOOD_COLOR
        self.coordinates = [x, y]

        canvas.create_oval(self.coordinates[0], self.coordinates[1], self.coordinates[0] + space_size,
                           self.coordinates[1] + space_size, fill=FOOD_COLOR, tags="food")
