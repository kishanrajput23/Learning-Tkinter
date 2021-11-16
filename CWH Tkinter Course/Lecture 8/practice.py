from tkinter import *

root = Tk()

root.geometry('500x500')

left_frame = Frame(root, bg="black", borderwidth=8, relief=SUNKEN)
left_frame.pack(side=LEFT, fill="y")

left_label = Label(left_frame, text="Explorer")
left_label.pack()

right_frame = Frame(root, bg="black", borderwidth=10, relief=SUNKEN)
right_frame.pack(side=RIGHT, fill="y")

right_label = Label(right_frame, text="Code Review")
right_label.pack()

top_frame = Frame(root, bg="black", borderwidth=10, relief=SUNKEN)
top_frame.pack(side=TOP, fill="x")

top_label = Label(top_frame, text="Welcome To Visual Studio Code")
top_label.pack()

bottom_frame = Frame(root, bg="black", borderwidth=10, relief=SUNKEN)
bottom_frame.pack(side=BOTTOM, fill="x")

bottom_label = Label(bottom_frame, text="Compilation...")
bottom_label.pack()

root.mainloop()