from tkinter import *
import time

WIDTH = 500
HEIGHT = 500
xVelocity = 1
yVelocity = 1

window = Tk()
canvas = Canvas(window, width=WIDTH, height=HEIGHT)
canvas.pack()

photo_background = PhotoImage(file='img.png')
my_image = canvas.create_image(0, 0, image=photo_background, anchor=NW)


photo_image = PhotoImage(file='img_1.png')
my_image = canvas.create_image(0, 0, image=photo_image, anchor=NW)
image_width = photo_image.width()
image_height = photo_image.height()

while True:
    coordinates = canvas.coords(my_image)
    if (coordinates[0] >= WIDTH - image_width or coordinates[0] < 0):
        xVelocity = -xVelocity
    if (coordinates[1] >= HEIGHT - image_height or coordinates[1] < 0):
        yVelocity = -yVelocity
    canvas.move(my_image, xVelocity, yVelocity)
    window.update()  # Invoke the update function with parentheses
    time.sleep(0.01)

window.mainloop()





