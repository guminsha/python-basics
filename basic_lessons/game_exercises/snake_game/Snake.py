SNAKE_COLOR = "#00FF00"
BODY_PARTS = 3


class Snake:
    def __init__(self, canvas, space_size):
        self.body_size = BODY_PARTS
        self.coordinates = []
        self.squares = []
        self.snake_color = SNAKE_COLOR

        for i in range(0, BODY_PARTS):
            self.coordinates.append([0, 0])

        for x, y in self.coordinates:
            square = canvas.create_rectangle(x, y, x + space_size, y + space_size,
                                             fill=SNAKE_COLOR, tags="snake")
            self.squares.append(square)
