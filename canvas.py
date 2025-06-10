from tkinter import *
window = Tk()


canvas = Canvas(window,height=500, width=500)
#canvas.create_line(0,0,500,500,fill ="blue")
#canvas.create_polygon(250,0,500,500,0,500,fill="yellow",outline="black",width=5)
canvas.create_arc(0,0,500,500,fill="red",extent=180,width=10)
canvas.create_arc(0,0,500,500,fill="white",extent=180,start=180,width=10)
canvas.create_arc(190,190,310,310,fill="white",extent=180,width=10)


canvas.pack()





window.mainloop()