# Our First Tkinter GUI | Python Tkinter GUI Tutorial In Hindi #2
 
Tkinter is the standard GUI library for Python. Here, we’ll start to develop our first Tkinter GUI. 
Tkinter provides a powerful object-oriented interface to the Tk GUI toolkit.

Let’s start with easy code to know the basics of Tkinter. All you need to do is perform the following steps –

- Import the Tkinter
- Create the GUI application's main window.
- Add one or more widgets to the GUI application(we’ll discuss these later more specifically)
- Enter the main event loop to take action against each event triggered by the user.

# Code is described below:

    from tkinter import *

    rahulrathva_root = Tk()

    # gui logic here

    rahulrathva_root.mainloop()

- Importing tkinter is the same as importing any other module in the Python code. Note that, the name of the module in Python 2.x is ‘Tkinter’ and in Python 3.x it is ‘tkinter’.

```from tkinter import *```

- To create the main window, tkinter offers a method ‘Tk’. To change the name of the window, you can change the className to the desired one.

```rahulrathva_root = Tk()```

- There is a method known by the name mainloop() which is used when your application is ready to run. This is an infinite loop used to run the application, wait for an event to occur and process the event as long as the window is not closed.

**Note:** There are currently 15 types of widgets in Tkinter. Button, Canvas, RadioButton, CheckButton, Menu, Frame, Label, etc. are different types of widgets used in Tkinter.

# Output: The output of the code (or the GUI window) is given beow:

<img src="https://api.codewithharry.com/media/videoSeriesFiles/courseFiles/python-gui-tkinter-hindi-2/base64.png" alt="">
