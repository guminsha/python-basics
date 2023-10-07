from tkinter import *


def submit():
    print(f"The temperature is: {scale.get()}ºC")


window = Tk()
window.title("Slide")

hot_image = PhotoImage(file="src\\fire.png")
hot_label = Label(image=hot_image)
hot_label.pack()


scale = Scale(window,
              from_=100,
              to=0,
              length=400,
              orient=VERTICAL,  # or HORIZONTAL
              font=("Arial", 18),
              tickinterval=10,  # adds numeric indicators for value
              # showvalue=False,  # hide current value
              resolution=5,  # increment of slider
              troughcolor="#69EAFF",
              fg="#FF1C00",
              bg="#111111")
# scale.set(50)
scale.set((scale["from"] - scale["to"])/2+scale["to"]) # fancy way to make it always appears in the middle

scale.pack()

cold_image = PhotoImage(file="src\\ice.png")
cold_label = Label(image=cold_image)
cold_label.pack()

button = Button(window,
                text="Submit",
                command=submit)
button.pack()

window.mainloop()
