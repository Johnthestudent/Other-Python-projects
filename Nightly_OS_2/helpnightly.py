from tkinter import *
from tkinter import ttk
from PIL import Image, ImageFilter, ImageOps, ImageChops, ImageTk, ImageEnhance
import tkinter
import PIL
from tkinter import filedialog
import shutil
import sys
import os
import cv2

#-----------------------------------------------------------
# Creating the window for loader
# Calling the TK
helperwindow = Tk()

# creating a string of 215 space characters
space=(" ")*215
# It retrieves the screen width of the user's display
screen_width=helperwindow.winfo_screenwidth()
 
# It retrieves the screen height of the user's display
screen_height = helperwindow.winfo_screenheight()
 
#Using an f-string to construct the window size in the 
#format width x height
helperwindow.geometry(f"{screen_width}x{screen_height}")
#setting the title for the window
helperwindow.title(f"{space}Nightly OS 2 help")
helperwindow.configure(bg='#191970')

#-----------------------------------------------------------
#labels for describing Nightly OS 2
label01 = Label(helperwindow, text = "This Helper section shows how to use Nightly OS 2.")
label01.config(font =("Times-New-Roman", 23), background="#191970", fg="#FFFFFF", justify="left")
label02 = Label(helperwindow, text = "Desktop:")
label02.config(font =("Times-New-Roman", 23), background="#191970", fg="#FFFFFF", justify="left")
label03 = Label(helperwindow, text = "Use the full view button on the top right corner to show taskbar!")
label03.config(font =("Times-New-Roman", 18), background="#191970", fg="#FFFFFF", justify="left")
label04 = Label(helperwindow, text = "Click on the Start button to show its options!")
label04.config(font =("Times-New-Roman", 18), background="#191970", fg="#FFFFFF", justify="left")
label05 = Label(helperwindow, text = "Click on the PDF viewer button to view a single pdf file!")
label05.config(font =("Times-New-Roman", 18), background="#191970", fg="#FFFFFF", justify="left")
label06 = Label(helperwindow, text = "Click on the Image viewer button to view two image files! Consider this too: \n https://stackoverflow.com/questions/19838972/how-to-update-an-image-on-a-canvas")
label06.config(font =("Times-New-Roman", 18), background="#191970", fg="#FFFFFF", justify="left")
label07 = Label(helperwindow, text = "Click on the Helper if you get stuck with the usage of any component!")
label07.config(font =("Times-New-Roman", 18), background="#191970", fg="#FFFFFF", justify="left")
label08 = Label(helperwindow, text = "Click on the browser icon to start google.com!")
label08.config(font =("Times-New-Roman", 18), background="#191970", fg="#FFFFFF", justify="left")
label09 = Label(helperwindow, text = "Click on the editor icons to start either text, table or presentation editor programs!")
label09.config(font =("Times-New-Roman", 18), background="#191970", fg="#FFFFFF", justify="left")
label10 = Label(helperwindow, text = "Click on the video player icon to start viewing a video!")
label10.config(font =("Times-New-Roman", 18), background="#191970", fg="#FFFFFF", justify="left")
label11 = Label(helperwindow, text = "Start button:")
label11.config(font =("Times-New-Roman", 23), background="#191970", fg="#FFFFFF", justify="left")
label12 = Label(helperwindow, text = "Click on the Tic-Tac-Toe game button to play a tic-tac-toe game online!")
label12.config(font =("Times-New-Roman", 18), background="#191970", fg="#FFFFFF", justify="left")
label13 = Label(helperwindow, text = "Click on the System button to display some system info and to try out Nightly OS prototype!")
label13.config(font =("Times-New-Roman", 18), background="#191970", fg="#FFFFFF", justify="left")
label14 = Label(helperwindow, text = "Network button works only on laptop, because it shows available wifi networks! Security window is empty!")
label14.config(font =("Times-New-Roman", 18), background="#191970", fg="#FFFFFF", justify="left")
label15 = Label(helperwindow, text = "Disk management shows the total file size of the entire repository compared to 500 MB-s.")
label15.config(font =("Times-New-Roman", 18), background="#191970", fg="#FFFFFF", justify="left")
label16 = Label(helperwindow, text = "Text Editor:")
label16.config(font =("Times-New-Roman", 23), background="#191970", fg="#FFFFFF", justify="left")
label17 = Label(helperwindow, text = "Buttons with the font names set the font family only for the text box, not for the saved file!")
label17.config(font =("Times-New-Roman", 18), background="#191970", fg="#FFFFFF", justify="left")
label18 = Label(helperwindow, text = "Click on the Save file button to save the content of the textbox into a txt file!")
label18.config(font =("Times-New-Roman", 18), background="#191970", fg="#FFFFFF", justify="left")
label19 = Label(helperwindow, text = "Click on the Open file button to open a txt file or a simple file, which will fill the textbox!")
label19.config(font =("Times-New-Roman", 18), background="#191970", fg="#FFFFFF", justify="left")
label20 = Label(helperwindow, text = "Click on the Exit button to close the text editor!")
label20.config(font =("Times-New-Roman", 18), background="#191970", fg="#FFFFFF", justify="left")
label21 = Label(helperwindow, text = "Table Editor:")
label21.config(font =("Times-New-Roman", 23), background="#191970", fg="#FFFFFF", justify="left")
label22 = Label(helperwindow, text = "You can type in any data for the grid table.")
label22.config(font =("Times-New-Roman", 18), background="#191970", fg="#FFFFFF", justify="left")
label23 = Label(helperwindow, text = "Click on the buttons of the functions to perform a function on the cells of the other table!")
label23.config(font =("Times-New-Roman", 18), background="#191970", fg="#FFFFFF", justify="left")
label24 = Label(helperwindow, text = "Presentation Editor:")
label24.config(font =("Times-New-Roman", 23), background="#191970", fg="#FFFFFF", justify="left")
label25 = Label(helperwindow, text = "Click on the buttons of the animations (swim in, fade) to perform an animation on the slide titles!")
label25.config(font =("Times-New-Roman", 18), background="#191970", fg="#FFFFFF", justify="left")
label26 = Label(helperwindow, text = "Click on the add slide buttons to add a new slide, and on the remove slide buttons to remove a slide!")
label26.config(font =("Times-New-Roman", 18), background="#191970", fg="#FFFFFF", justify="left")
label27 = Label(helperwindow, text = "You can type in data into the text boxes (slides) and do animations on the existing slides.")
label27.config(font =("Times-New-Roman", 18), background="#191970", fg="#FFFFFF", justify="left")
label28 = Label(helperwindow, text = "Click on the X button on the top right corner of the window to close it! (for every application)")
label28.config(font =("Times-New-Roman", 18), background="#191970", fg="#FFFFFF", justify="left")

#-----------------------------------------------------------
#placing the labels onto the tkinter window
label01.pack()
label02.pack()
label03.pack(anchor='w')
label04.pack(anchor='w')
label05.pack(anchor='w')
label06.pack(anchor='w')
label07.pack(anchor='w')
label08.pack(anchor='w')
label09.pack(anchor='w')
label10.pack(anchor='w')
label11.pack()
label12.pack(anchor='w')
label13.pack(anchor='w')
label14.pack(anchor='w')
label15.pack(anchor='w')
label16.pack()
label17.pack(anchor='w')
label18.pack(anchor='w')
label19.pack(anchor='w')
label20.pack(anchor='w')
label21.pack()
label22.pack(anchor='w')
label23.pack(anchor='w')
label24.pack()
label25.pack(anchor='w')
label26.pack(anchor='w')
label27.pack(anchor='w')
label28.pack(anchor='w')

#the window won't get opened without this
helperwindow.mainloop()