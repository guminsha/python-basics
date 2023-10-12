from tkinter import *
from tkinter import filedialog


def save_file():
    file = filedialog.asksaveasfile(initialdir="C:\\Users\\Brian\\PycharmProjects\\helloWorld\\basic_lessons"
                                               "\\GUI_windows_related\\src\\",
                                    defaultextension=".txt",
                                    filetypes=[
                                        ("Text file", ".txt"),
                                        ("HTML file", ".html"),
                                        ("All files", ".*")
                                    ])
    if file is None:  # avoid exception
        return
    # file_text = str(text_area.get("1.0", END))
    file_text = input("Enter some text i guess: ")
    file.write(file_text)
    file.close()


window = Tk()

button = Button(text="Save",
                command=save_file)
button.pack()

text_area = Text(window)
text_area.pack()

window.mainloop()
