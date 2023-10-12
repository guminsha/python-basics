from tkinter import *

# label = an area widget that holds text and/or an image within a window

window = Tk()

photo = PhotoImage(file="assets/bg.png")  # location

window.geometry("1340x860")  # need to search about auto resize
window.title("Label studies")

label = Label(window,
              text="Hello World",
              font=("Arial", 40, "bold"),
              fg="#00FF00",
              bg="black",
              relief=RAISED,
              bd=10,
              padx=20,
              pady=20,
              image=photo,
              compound="top",
              )  # color related = hexvalue/name, relief = RAISED, SUNKEN...
label.pack()
label.place(x=0, y=0)

window.mainloop()
