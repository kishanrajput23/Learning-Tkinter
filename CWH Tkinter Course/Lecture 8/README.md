# Frame In Tkinter | Python Tkinter GUI Tutorial In Hindi #8

- A Frame widget is a rectangular region on the screen that can be used as a foundation class to implement complex widgets. This widget is very important for the process of grouping and organizing other widgets in a friendly way. It works like a container, which is responsible for arranging the position of other widgets. We can use bg, relief, borderwidth, bd as the attributes of the Frame widget. Some important attributes are discussed below:

- **bg:** The normal background color displayed behind the label and indicator.

- **relief:** The type of the border of the frame. Its default value is set to FLAT. We can set it to any other styles, i.e., FLAT, RAISED, SUNKEN, GROOVE, RIDGE.

- **borderwidth:** TkinterLabel doesn't have any border by default. We need to assign the borderwidth option to add a border around the Label widget along with the relief option to be an option rather than flat to make visible.

- **bd:** The size of the border around the indicator. Default is 2 pixels.

# Code is described below:

```
from tkinter import *
root = Tk()
root.geometry("655x333")
f1 = Frame(root, bg="grey", borderwidth=6, relief=SUNKEN)
f1.pack(side=LEFT, fill="y")

f2 = Frame(root, borderwidth=8, bg="grey", relief=SUNKEN)
f2.pack(side=TOP, fill="x")

l = Label(f1, text="Project Tkinter - Pycharm")
l.pack( pady=142)

l = Label(f2, text="Welcome to sublime text", font="Helvetica 16 bold", fg="red", pady=22)
l.pack()

root.mainloop()
```

- Importing tkinter is the same as importing any other module in the Python code. Note that the module's name in Python 2.x is 'Tkinter', and in Python 3.x, it is 'tkinter'.

```from tkinter import *```

- To create the main window, Tkinter offers a method, 'Tk'. To change the name of the window, you can change the className to the desired one.

```root = Tk()```

- To set the dimensions of the Tkinter window and to set the position of the main window on the user's desktop, the geometry() function is used. As in the example: the width is 655 pixels, and the height is 333 pixels, so we can write the function as geometry(655x333).

```root.geometry("655x333")```

- To take Frame variable as f1 and set the attributes- bg (background color) = "grey", borderwidth(thickness of the Frame's border)=6, and relief=SUNKEN. Then the Frame f1 must be packed.

```
f1 = Frame(root, bg="grey", borderwidth=6, relief=SUNKEN)
f1.pack(side=LEFT, fill="y")
```

- In the same way, another Frame f2 is taken, and the attributes are set to the Frame.

```
f2 = Frame(root, borderwidth=8, bg="grey", relief=SUNKEN)
f2.pack(side=TOP, fill="x")
```

- To call the Label widget, which is a child of the root widget. The keyword parameter "text" specifies the text "Project Tkinter - Pycharm" to be shown, and the pack method tells Tk to fit the size of the window to the given text where pady adds extra space (i.e., 142 in this example) from the upper and lower portion of the Frame widget.

```
l = Label(f1, text="Project Tkinter - Pycharm")
l.pack( pady=142)
```

- In the same way, another label is taken, and the attributes are set to the Label.

```
l = Label(f2, text="Welcome to sublime text", font="Helvetica 16 bold", fg="red", pady=22)
l.pack()
```

- There is a method known by the name mainloop(), which is used when your application is ready to run. This is an infinite loop used to run the application, wait for an event to occur, and process the event as long as the window is not closed.

```
root.mainloop()
```


# Output: The output of the code (or the GUI window) is given below:

<img src="https://api.codewithharry.com/media/videoSeriesFiles/courseFiles/python-gui-tkinter-hindi-8/base64.png" alt="">
