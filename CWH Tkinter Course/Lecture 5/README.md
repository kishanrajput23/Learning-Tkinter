# Displaying Images Using Label | Python Tkinter GUI Tutorial In Hindi #5

We perhaps add one or more images to make our GUI more creative and presentable.  The PhotoImage() class is used to display images in labels, buttons, canvases, and text widgets. You can use the PhotoImage() class whenever you need to display an icon or an image in a Tkinter application. This being said, let’s see how to see an image using with Python in the shortest way.

# Code is described below:
    from tkinter import *
    root = Tk()
    root.geometry("500x500")
    
    #for png files
    picture = PhotoImage(file='swag.png')
    picture_label = Label(image=picture)
    picture_label.pack()
    root.mainloop()

- Importing tkinter is same as importing any other module in the Python code.Note that, the name of the module in Python 2.x is ‘Tkinter’ and in Python 3.x it is ‘tkinter’.
    
    ```from tkinter import *```

- To create a main window, tkinter offers a method ‘Tk’. To change the name of the window, you can change the className to the desired one.
    
    ```root = Tk()```

- To set the dimensions of the Tkinter window and to set the position of the main window on the user’s desktop, geometry() function is used. As in example: the width is 500 pixels and height is 500 pixels so we can write the function as geometry(500x500).
    
    ```root.geometry("500x500")```

- To display an image i.e. “swag.png” in a Tkinter application, the PhotoImage() class is used.

    ```picture = PhotoImage(file="swag.png")```

- To call the Label widget which is a child of the root widget. The keyword parameter "image" specifies the photo “swag.png” to be shown:

    ```picture_label = Label(image=picture)```

- The pack method tells Tk to fit the size of the window to the given image.
    
    ```picture_label.pack()```

- There is a method known by the name mainloop() which is used when your application is ready to run. This is an infinite loop used to run the application, wait for an event to occur and process the event as long as the window is not closed.

    ```root.mainloop()```
    
# Output: The output of the code (or the GUI window) is given below:

<img src="https://github.com/kishanrajput23/Learning-Tkinter/blob/main/CWH%20Tkinter%20Course/Lecture%205/swag_output.png" alt="">
    
**Note:**  If we need to work with other file formats (example: .jpg) the Python Imaging Library (PIL) contains classes that lets you load images in over 30 formats, and convert them to Tkinter-compatible image objects.  So in this case, we have to install pillow library (if it is not installed in the system) by writing pip install pillow in the terminal and then write the code as follows:

    from tkinter import *
    from PIL import Image, ImageTk
    root = Tk()
    root.geometry("500x500")
    
    #for jpg files
    image = Image.open("jarvis.jpg")
    photo = ImageTk.PhotoImage(image)
    pic_label = Label(image=photo)
    pic_label.pack()
    root.mainloop()

- Import Image and ImageTk from PIL library.
- Take image as a variable when the image “jarvis.jpg” will be opened.
- Take photo as another variable to store the image using PhotoImage() class.
- Call the Label() widget and pack it.
- Write the mainloop() method to run the application.

# Output: The output of the code (or the GUI window) is given below:

<img src="https://github.com/kishanrajput23/Learning-Tkinter/blob/main/CWH%20Tkinter%20Course/Lecture%205/jarvis_output.png" alt="">
