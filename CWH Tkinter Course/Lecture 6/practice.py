from tkinter import *

root = Tk()

root.geometry("500x400")

root.title("My Own GUI")

bottom_label = Label(text="READY", bg="black", fg="white", font="comicsansms 32 bold", borderwidth=5, relief=GROOVE)

bottom_label.pack(side=BOTTOM, fill=X)

root.mainloop()