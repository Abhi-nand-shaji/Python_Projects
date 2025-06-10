from tkinter import *

window = Tk()
window.geometry("200x200")
window.title("Abhinand's first GUI program")

#food = ["pizza", "hamburger", "hotdog"]


x = IntVar()


#for index in range(len(food)):
 #   radiobutton = Radiobutton(window,text=food[index],variable=x,value = index,padx = 25, font = "Impact")
  #  radiobutton.pack(anchor=W)
def submit():
    print("You have ordered: ")
    print(listbox.get(listbox.curselection()))

#def submit():
#    print("The temperature is: " + str(scale.get())+ "degrees C")


#scale = Scale(window,from_=0, to=100, orient=HORIZONTAL, tickinterval=10, length=1100, font=('Consas',20), resolution=5, troughcolor='#69EAFF', fg='#FF1C00',bg = '#111111')
#scale.set(((scale['from']-scale['to'])/2)+scale['to'])
#scale.pack()

#button = Button(window,text='submit',command=submit)
#button.pack()

listbox =Listbox(window,bg="#f7ffde",font=("Constantia",35),width=12,selectmode=MULTIPLE)
listbox.pack()

listbox.insert(1, "pizza")
listbox.insert(2, "pasta")
listbox.insert(3, "RCMF")
listbox.insert(4, "kanzhi")
listbox.insert(5, "popsicle")

listbox.config(height=listbox.size())

submitButton =Button(window,text="submit",command=submit)
submitButton.pack()



#def submit():
 #   username = entry.get()
  #  print("hello "+username)

#def delete():
   # entry.delete(0, END)

#def backspace():
 #entry.delete(len(entry.get())-1,END)


entry = Entry(window, font=("Arial",50), fg="#00FF00", bg="black", show="*")
#entry.insert(0,"ROOPCHAND")
entry.pack(side=LEFT)

#submit_button = Button(window,text="submit", command = submit)
#submit_button.pack(side=RIGHT)


#delete_button = Button(window,text="delete", command = delete)
#delete_button.pack(side=RIGHT)

#backspace_button = Button(window,text="backspace", command = backspace)
#backspace_button.pack(side=RIGHT)

x = IntVar()

def display():
    if x.get() == 1:
        print("You agree!")
    else:
        print("You don't agree")


check_button =Checkbutton(window, text="I agree to something", variable=x, onvalue=1, offvalue=0, command=display)
check_button.pack()

#def click():
 #   print("You clicked the button")
# Load the original photo
original_photo = PhotoImage(file='Avishkar.c39918b4.png')

# Decrease the size of the photo using subsample
resized_photo = original_photo.subsample(10, 10)  # Change the values as needed

#label = Label(window, text="Hello World", font=('Arial', 10, 'bold'), fg='red', bg='white', padx=20, pady=20,
              #image=resized_photo, compound='bottom')
#label.pack()


#button = Button(window, text="click me", command=click, font=("Comic sans", 30), fg = "#00FF00", bg="black", activeforeground="#00FF00", activebackground="black")
#button.pack()
# Set the resized photo as the icon
window.iconphoto(True, resized_photo)
window.config(background="white")

window.mainloop()
#place window on computer screen, listen for events