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

"""
img = Image.open('Tengelice.jpg')
filtered_img = img.convert('L')
filtered_img.save("result.png", 'png')
"""
#-----------------------------------------------------------
global new_img
# function to display this image
# and updating the panel widget to show this image
def displayimage(img):
    dispimage = ImageTk.PhotoImage(img)
    panel.configure(image=dispimage)
    panel.image = dispimage

# Creating the window for image editor
# Calling the TK
mains = Tk()

# creating a string of 215 space characters
space=(" ")*215
# It retrieves the screen width of the user's display
screen_width=mains.winfo_screenwidth()
 
# It retrieves the screen height of the user's display
screen_height = mains.winfo_screenheight()
 
#Using an f-string to construct the window size in the 
#format width x height
mains.geometry(f"{screen_width}x{screen_height}")
#setting the title for the window
mains.title(f"{space}Image Viewer")
mains.configure(bg='#202020')

#-----------------------------------------------------------
img = Image.open("Tengelice.png")
img = img.resize((759, 838))
panel = Label(mains)
panel.grid(row=0, column=0, rowspan=12, padx=50, pady=50)
displayimage(img)

#-----------------------------------------------------------
#showing the next image
#the function ensures that the user can go to the other image
def next_image():
	img = Image.open("main_background.png")
	img = img.resize((759, 838))
	displayimage(img)

#showing the next image button
#NEXT_IMG stores the Button widget to thumbnail the image
#Inside the widget,
NEXT_IMG = Button(mains, text='Next image', width=25, command=next_image, bg="#1f242d")
NEXT_IMG.configure(font=('poppins',11,'bold'),foreground='white')
NEXT_IMG.place(x=1500,y=625)

#-----------------------------------------------------------
#showing the previous image
#the function ensures that the user can go to the previous image
#by undoing the previously done operations
def previous_image():
	img = Image.open("Tengelice.png")
	img = img.resize((759, 838))
	displayimage(img)

#showing the previous image button
#RESET_IMG stores the Button widget to thumbnail the image
#Inside the widget,
PREVIOUS_IMG = Button(mains, text='Previous image', width=25, command=previous_image, bg="#1f242d")
PREVIOUS_IMG.configure(font=('poppins',11,'bold'),foreground='white')
PREVIOUS_IMG.place(x=1200,y=625)

#experimental purposes
#print(tkinter.TkVersion)

#the window won't get opened without this
mains.mainloop()
