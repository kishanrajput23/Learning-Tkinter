# Attributes Of Label & Pack | Python Tkinter GUI Tutorial In Hindi #6
 
**Attributes:** A set of properties of a widget that defines its visual appearance on the computer screen and how it responds to user events. Here we’ll discuss about the attributes of Label and Pack.

**1. Attributes of Label:** The Label widget is a standard Tkinter widget used to display a text or image on the screen.  There are a lot of attributes of Label widget. Some important attributes are discussed below:
- **bg:** The normal background color displayed behind the label and indicator.
- **fg:** This option specifies the color of the text (foreground color). If you are displaying a bitmap, this is the color that will appear at the position of the 1-bits in the bitmap.
- **padx:** Extra space added to the left and right of the text within the widget. Default is 1.
- **pady:** Extra space added above and below the text within the widget. Default is 1.
- **relief:** Specifies the appearance of a decorative border around the label. There are five types of reliefs, such that FLAT, RAISED, SUNKEN, GROOVE, RIDGE. The default is FLAT.
- **font:** If you are displaying text in this label (with the text or textvariable option), the font option specifies the style, size and other characteristics (i.e. bold, italic etc.) of the font and in this style the text will be displayed.
- **text:** To display one or more lines of text in a label widget, set this option to a string containing the text. Internal newlines (“\n”) will force a line break.
- **justify:** Specifies how multiple lines of text will be aligned with respect to each other: LEFT for flush left, CENTER for centered (the default), or RIGHT for right-justified.
- **height:** The vertical dimension of the new frame.
- **width:** The horizontal dimension of the new frame. If this option is not set, the label will be sized to fit its contents.

**2. Attributes of Pack:** The Pack geometry manager packs widgets in rows or columns. We can use options like fill, expand, and side to control this geometry manager.
- **fill:** Determines whether widget fills any extra space allocated to it by the packer, or keeps its own minimal dimensions: NONE (default), X (fill only horizontally), Y (fill only vertically), or BOTH (fill both horizontally and vertically).
- **side:** Determines which side of the parent widget packs against: TOP, BOTTOM, LEFT, or RIGHT. The default is TOP.
- **anchor:** Anchors are used to define where text is positioned relative to a reference point. The anchor attributes are: n, s, e, w, center, nw, sw, ne and se. The default is center.

# Code is described below (using attributes of Label & Pack):

```from tkinter import *

root = Tk()

root.geometry("500x500")

root.title("My GUI with Harry")

# Important Label Options
# text - adds the text
# bd - background
# fg - foreground
# font - sets the font
# 1. font=("comicsansms", 19, "bold")
# 2. font="comicsansms 19 bold"

# padx - x padding
# pady - y padding
# relief - border styling - SUNKEN, RAISED, GROOVE, RIDGE

title_label = Label(text ='''
Abdul Rashid Salim Salman Khan is an Indian 
\nfilm actor, producer, occasional playback singer and television personality. In a film career spanning 
\nalmost thirty years, Khan has received numerous awards, including two National Film Awards as a film 
\nproducer, and two Filmfare Awards for acting. He has a significant following in Asia and the Indian 
\ndiaspora worldwide, and is cited in the media as one of the most commercially successful actors of Indian 
\ncinema. According to the Forbes 2018 list of Top-Paid 100 Celebrity Entertainers in world, Khan was 
\nthe highest ranked Indian with 82nd rank with earnings of $37.7 million.''', bg ="red", fg="yellow", padx=13, pady=94, font="comicsansms 10 bold", borderwidth=5, relief=GROOVE)

# title_label.pack()

# Important Pack options
# anchor = nw
# side = top, bottom, left, right
# fill
# padx
# pady

# title_label.pack(side=BOTTOM, anchor ="sw", fill=X)
title_label.pack(side=LEFT, fill=Y, padx=34, pady=34)
root.mainloop()
```

# Output: The output of the code (or the GUI window) is given below:

<img src="https://github.com/kishanrajput23/Learning-Tkinter/blob/main/CWH%20Tkinter%20Course/Lecture%206/label%20options%20output.png" alt="">

# Do It Yourself 🤔

**Question.** You have to make a GUI window of 500x400 then just you have to add a small strip at the bottom of your GUI window with "READY" text on it.

# Solution of DIY 😀

<img src="https://github.com/kishanrajput23/Learning-Tkinter/blob/main/CWH%20Tkinter%20Course/Lecture%206/practice%20output.png" alt="">
