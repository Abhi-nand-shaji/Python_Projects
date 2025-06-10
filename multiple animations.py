from tkinter import *
from Ball import *
import time

WIDTH =500
HEIGHT = 500
window = Tk()

canvas = Canvas(window,width=WIDTH,height=HEIGHT)
canvas.pack()

volley_ball = Ball(canvas,0,0,100,1,1,"white")
tennis_ball = Ball(canvas,0,0,50,4,3,"red")

while True:
    volley_ball.move()
    tennis_ball.move()
    window.update()
    time.sleep(0.01)

window.mainloop()


