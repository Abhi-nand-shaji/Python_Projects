from tkinter import *
from tkinter import messagebox #import messagebox library

window =Tk()

def click():
    #messagebox.showinfo(title='This is an info message box', message = 'You are dumb')
    #messagebox.showwarning(title='WARNING!!!', message = 'You are dumb')
    #messagebox.showerror(title='ERROR!', message='something went wrong :(')

    if messagebox.askokcancel(title='ask ok cancel', message = 'Do yu want to do the thing? '):
        print('You did a thing')
    else:
        print('You cancelled a thing')




button = Button(window,command=click,text='click me')
button.pack()










window.mainloop()
