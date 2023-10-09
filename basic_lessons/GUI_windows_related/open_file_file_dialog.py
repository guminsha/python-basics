from tkinter import *
from tkinter import filedialog


def open_file():
    file_path = filedialog.askopenfilename(initialdir="C:\\Users\\Brian\\PycharmProjects\\helloWorld\\basic_lessons"
                                                      "\\GUI_windows_related\\src\\",
                                           title="Open file okay?",
                                           filetypes=(("text files", "*.txt"), ("all files", "*.*")))  # searchs first
    # for text file, and have another open for all files
    file = open(file_path, "r")
    print(file.read())
    file.close()


window = Tk()

button = Button(text="Open",
                command=open_file)
button.pack()

window.mainloop()
