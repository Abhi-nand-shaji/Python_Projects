from tkinter import *

window = Tk()
window.geometry("200x200")


def move_up(event):
    label.place(x=label.winfo_x(),y=label.winfo_y()-10)
    #canvas.move(photoimage,0,-10)

def move_down(event):
    label.place(x=label.winfo_x(),y=label.winfo_y()+10)
    # canvas.move(photoimage,0,10)

def move_left(event):
    label.place(x=label.winfo_x()-10,y=label.winfo_y())
    # canvas.move(photoimage,-10,0)

def move_right(event):
    label.place(x=label.winfo_x()+10,y=label.winfo_y())
    # canvas.move(photoimage,10,0)

window.bind("<w>",move_up)
window.bind("<s>",move_down)
window.bind("<a>",move_left)
window.bind("<d>",move_right)
window.bind("<Up>",move_up)
window.bind("<Down>",move_down)
window.bind("<Left>",move_left)
window.bind("<Right>",move_right)


#for image in canvas
#canvas = Canvas(window,width=500,height=500)
#canvas.pack()

#photoimage = canvas.create_image(0,0,image=my_image,anchor=NW)

my_image = PhotoImage(file='Avishkar.c39918b4.png')
resized_photo = my_image.subsample(20, 20)  # Adjust these values as needed

label = Label(window, image=resized_photo)
label.place(x=0, y=0)

window.mainloop()
