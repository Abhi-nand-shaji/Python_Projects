from tkinter import *
from tkinter import filedialog

window = Tk()

def saveFile():
    file = filedialog.asksaveasfile(defaultextension='.txt', filetypes=[("Textf file",".txt"),("HTML file",".html"),("All files",".*")])

    if file is None:
        return
    filetext = str(text.get(1.0,END))
    file.write(filetext)
    file.close()


button = Button(text='save',command=saveFile)
button.pack()
text = Text(window)
text.pack()
window.mainloop()
