from tkinter import *

window = Tk()

canvas = Canvas(window, height=500, width=500)

# canvas.create_line(0, 0, 500, 500, fill="blue", width=5)
# canvas.create_line(0, 500, 500, 0, fill="red", width=5)
# canvas.create_rectangle(50, 50, 250, 250, fill="purple")
# canvas.create_polygon(250, 0, 500, 500, 0, 500, fill="yellow", outline="black", width=5)  # x=horizontal, y=vertical
# points = [250, 0, 500, 500, 0, 500]
# canvas.create_polygon(points, fill="yellow", outline="black", width=5)
# canvas.create_arc(0, 0, 500, 500, fill="green", style=PIESLICE, start=270, extent=180)  # style = CHORD, PIESLICE, ARC

canvas.create_arc(0, 0, 500, 500, fill="red", start=0, extent=180, width=10)
canvas.create_arc(0, 0, 500, 500, fill="white", start=180, extent=180, width=10)
canvas.create_line(0, 250, 500, 250, width=30)
canvas.create_oval(190, 190, 310, 310, fill="black", width=10)
canvas.create_oval(200, 200, 300, 300, fill="white", width=10)


canvas.pack()

window.mainloop()
