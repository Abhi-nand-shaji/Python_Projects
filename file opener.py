from tkinter import *
from tkinter import filedialog
window = Tk()


def openfile():
    #filepath = filedialog.askopenfilename(initialdir="my file address", title="Open file", filetypes=(("text files","*.txt"),("all files","*.*)))
    filepath = filedialog.askopenfilename()
    print(filepath)
    file = open(filepath, 'r')
    print(file.read())
    file.close()

button = Button(text ="Open", command = openfile)
button.pack()

window.mainloop()

