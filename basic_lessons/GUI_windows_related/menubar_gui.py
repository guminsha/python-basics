from tkinter import *
from tkinter import filedialog


def open_file():
    file = filedialog.askopenfilename(initialdir="C:\\Users\\Brian\\PycharmProjects\\helloWorld\\basic_lessons"
                                                 "\\GUI_windows_related\\src\\",
                                      title="Open file okay?",
                                      filetypes=(("text files", "*.txt"), ("all files", "*.*")))
    file = open(file, "r")
    text_field.insert("1.0", file.read())
    file.close()


def save_file():
    file = filedialog.asksaveasfile(initialdir="C:\\Users\\Brian\\PycharmProjects\\helloWorld\\basic_lessons"
                                               "\\GUI_windows_related\\src\\",
                                    defaultextension=".txt",
                                    filetypes=[
                                        ("Text file", ".txt"),
                                        ("HTML file", ".html"),
                                        ("All files", ".*")
                                    ])  # open save, right dir, set default .txt but have other options (html and all)
    file_text = str(text_field.get("1.0", END))  # gets text
    if file is None:  # avoid exception
        return
    file.write(file_text)
    file.close()


def cut():
    print("You cut some text")


def copy():
    print("You copied some text")


def paste():
    print("You pasted some text")


window = Tk()

open_image = PhotoImage(file="src\\folder.png")
save_image = PhotoImage(file="src\\flopdisk.png")
exit_image = PhotoImage(file="src\\exit.png")

menu_bar = Menu(window)
window.config(menu=menu_bar)

file_menu = Menu(menu_bar, tearoff=0, font=("MV Boli", 15))  # tearoff = annoying line
menu_bar.add_cascade(label="File", menu=file_menu)
file_menu.add_command(label="Open", command=open_file, image=open_image, compound="left")
file_menu.add_command(label="Save", command=save_file, image=save_image, compound="left")
file_menu.add_separator()
file_menu.add_command(label="Exit", command=quit, image=exit_image, compound="left")

edit_menu = Menu(menu_bar, tearoff=0, font=("MV Boli", 15))
menu_bar.add_cascade(label="Edit", menu=edit_menu)
edit_menu.add_command(label="Cut", command=cut)
edit_menu.add_command(label="Copy", command=copy)
edit_menu.add_command(label="Paste", command=paste)

text_field = Text(window,
                  bg="light yellow",
                  font=("Ink Free", 25),
                  height=8,
                  width=20,
                  padx=20,
                  pady=20,
                  fg="purple"
                  )
text_field.pack()

window.mainloop()
