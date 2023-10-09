from tkinter import *
from tkinter import messagebox  # import the message box library


def click():
    # messagebox.showinfo(title="This is an infor messagebox",
    #                     message="You are a person")

    # messagebox.showwarning(title="WARNING!",
    #                        message="You have a Virus!")

    # messagebox.showerror(title="ERROR!",
    #                      message="Something went wrong!")

    # if messagebox.askokcancel(title="Ask ok or cancel",
    #                           message="Do you want to do a thing?"):  # returns True or False
    #     print("You did a thing")
    # else:
    #     print("You have canceled a thing")

    # if messagebox.askretrycancel(title="Ask retry or cancel",
    #                             message="Do you want to retry a thing?"):  # returns True or False
    #     print("You retried a thing")
    # else:
    #    print("You have canceled a thing")

    # if messagebox.askyesno(title="Ask yes or no",
    #                        message="Do you like cake?"):  # returns True or False
    #     print("I like cake too")
    # else:
    #     print("How u don't like cake?")

    # print(answer := messagebox.askquestion(title="Ask question",
    #                                        message="Do you like pie?"))  # Returns "yes" or "no"
    # if answer == "yes":
    #     print("I like pie too")
    # else:
    #     print("Why you dont like pie?")

    print(answer := messagebox.askyesnocancel(title="Yes or no or cancel",  # Returns True, False or None
                                              message="Do you like to code?",
                                              icon="error"))  # icon = warning, info or error
    if answer:
        print("You like to code")
    elif not answer:
        print("Then why are you here?")
    else:
        print("You dodge the question")


window = Tk()

button = Button(window,
                command=click,
                text="Click me")
button.pack()

window.mainloop()
