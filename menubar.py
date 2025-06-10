from tkinter import *

window = Tk()
def openFile():
    print("File has been opened")


def saveFile():
    print("File has been saved")


menubar = Menu(window)

window.config(menu=menubar)

fileMenu = Menu(menubar,tearoff = 0)
menubar.add_cascade(label="File",menu=fileMenu)
fileMenu.add_command(label="Open", command = openFile)
fileMenu.add_command(label="Save", command = saveFile)
fileMenu.add_separator()
fileMenu.add_command(label="Exit", command = quit)

editMenu = Menu(menubar, tearoff=0)
menubar.add_cascade(label="Edit",menu=editMenu)


window,mainloop()