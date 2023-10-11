from tkinter import *
from tkinter.ttk import *
import time


# def start():
#     tasks = 10
#     x = 0
#     while x < tasks:
#         time.sleep(1)
#         bar["value"] += 10
#         x += 1
#         percent.set(str(int((x/tasks) * 100))+"%")
#         task.set(str(x)+"/"+str(tasks)+" tasks completed")
#         window.update_idletasks()


def start():
    gigabytes = 3249
    download = 0
    speed = 10
    while download < gigabytes:
        time.sleep(0.05)
        bar["value"] += (speed/gigabytes)*100
        download += speed
        percent.set(str(int((download/gigabytes) * 100))+"%")
        task.set(str(download)+"/"+str(gigabytes)+" GB completed")
        window.update_idletasks()


window = Tk()

percent = StringVar()
task = StringVar()

bar = Progressbar(window, orient=VERTICAL, length=300)
bar.pack(padx=15, pady=10)

percent_label = Label(window, textvariable=percent).pack()
task_label = Label(window, textvariable=task).pack()

button = Button(window, text="Download", command=start).pack()

window.mainloop()
