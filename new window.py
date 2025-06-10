from tkinter import *


def create_window():
    new_window = Tk()
    #new_window = Toplevel()

    old_window.destroy()  #close old window


old_window = Tk()

Button(old_window,text="create new window", command=create_window).pack()

old_window.mainloop()