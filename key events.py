from tkinter import *

window = Tk()
def doSomething(event):
    #print("You did a thing")
    print("You pressed: "+ event.keysym)
    label.config(text=event.keysym)

#window.bind("<q>",doSomething) #Here what we give in <> will decide. If I click the one in <> it will run one in <>
window.bind("<Key>", doSomething)

label = Label(window,font=("Helvetica",100))
label.pack()

window.mainloop()
