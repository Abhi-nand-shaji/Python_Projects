from tkinter import *

def drag_start(event):
    widget = event.widget
    widget.startX = event.x
    widget.startY = event.y

def drag_motion(event):
    widget = event.widget
    x = widget.winfo_x() - label.startX + event.x
    y = widget.winfo_y() - label.startY + event.y
    widget.place(x=x, y=y)

window = Tk()

label = Label(window, bg="red", width=10, height=5)
label.place(x=0, y=0)

label2 = Label(window, bg="blue", width=10, height=5)
label2.place(x=100, y=100)

label.bind("<Button-1>", drag_start)  # Added closing angle bracket
label.bind("<B1-Motion>", drag_motion)  # Added closing angle bracket

label2.bind("<Button-1>", drag_start)  # Added closing angle bracket
label2.bind("<B1-Motion>", drag_motion)  # Added closing angle bracket

window.mainloop()



