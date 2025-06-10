from tkinter import *
from tkinter import colorchooser #submodule

window = Tk()
window.geometry("420x420")


def click():
    color = colorchooser.askcolor()
    print(color)
    colorHex = color[1]
    print(colorHex)
    window.config(bg=colorHex)


button = Button(text='click me', command=click)
button.pack()
window.mainloop()