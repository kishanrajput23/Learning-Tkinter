from tkinter import *
from PIL import Image, ImageTk

root = Tk()

root.geometry("500x500")

string = "Welcome to Rajput World"

intro = Label(text=string)
intro.pack()

#for png files
picture = PhotoImage(file='swag.png')
picture_label = Label(image=picture)
picture_label.pack()

#for jpg files
image = Image.open("jarvis.jpg")
photo = ImageTk.PhotoImage(image)
pic_label = Label(image=photo)
pic_label.pack()

root.maxsize(1500, 1500)

root.minsize(50,50)

root.mainloop()