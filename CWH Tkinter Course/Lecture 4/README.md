# Label, Geometry, Maxsize & Minsize | Python Tkinter GUI Tutorial In Hindi #4
 

**Label():** A Label is a Tkinter Widget class, which is used to display text or an image. The label is a widget that the user just views but does not interact with.

**Geometry():** This method is used to set the dimensions of the Tkinter window and is used to set the position of the main window on the user’s desktop.

**Minsize():** This method is used to set the minimum size of the Tkinter window. Using this method user can set the window’s initialized size to its minimum size, and still be able to maximize and scale the window larger.

**Maxsize():** This method is used to set the maximum size of the Tkinter window i.e. maximum size a window can be expanded. Users will still be able to shrink the size of the window to the minimum possible.

# Code is described below:
    from tkinter import *
    imaginary_tech_root = Tk()
    
    # Width x Height
    imaginary_tech_root.geometry("644x434")
    
    # width, height
    imaginary_tech_root.minsize(300,100)
    
    # width, height
    imaginary_tech_root.maxsize(1200, 988)
    
    shakaib = Label(text="Shakaib is a good boy and this is his GUI")
    shakaib.pack()
    
    imaginary_tech_root.mainloop()
    
- Importing tkinter is the same as importing any other module in the Python code. Note that, the name of the module in Python 2.x is ‘Tkinter’ and in Python 3.x it is ‘tkinter’.

        from tkinter import *

- To create the main window, tkinter offers a method ‘Tk’. To change the name of the window, you can change the className to the desired one.

        imaginary_tech_root = Tk()

- To set the dimensions of the Tkinter window and to set the position of the main window on the user’s desktop, geometry() function is used. As in example: the width is 644 pixels and the height is 434 pixels so we can write the function as geometry(644x434).

        imaginary_tech_root.geometry("644x434")

- To set the minimum size of the Tkinter window we use minsize() function and to set the maximum size of the Tkinter window we use maxsize() As in the example: minsize(300,100) depicts the minimum width and height of the Tkinter window must be 300 pixels and 100 pixels respectively. In the same way, maxsize(1200,988) depicts the maximum width, and the height of the Tkinter window must be 1200 pixels and 988 pixels respectively. 

**Note:** We have to put a comma between width and height, unlike geometry() function.

    imaginary_tech_root.minsize(300,100)
    imaginary_tech_root.maxsize(1200, 988)

- To call the Label widget which is a child of the root widget. The keyword parameter "text" specifies the text “Shakaib is a good boy and this is his GUI” to be shown:

        shakaib = Label(text="Shakaib is a good boy and this is his GUI")

- The pack method tells Tk to fit the size of the window to the given text.

        shakaib.pack()

- There is a method known by the name mainloop() which is used when your application is ready to run. This is an infinite loop used to run the application, wait for an event to occur, and process the event as long as the window is not closed.

        imaginary_tech_root.mainloop()
        
# Output: The output of the code (or the GUI window) is given beow:

<img src="https://api.codewithharry.com/media/videoSeriesFiles/courseFiles/python-gui-tkinter-hindi-4/base64.png" alt="">
