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
mains.title(f"{space}Nightly OS 2 loader")
mains.configure(bg='#191970')

#-----------------------------------------------------------
# Create label
#firstLabelsize = int(screen_width / 60)    #experimental size section
l = Label(mains, text = "Welcome to Nightly OS 2")  #title
l.config(font =("Times-New-Roman", 50)) #font family and size
l.config(background="#191970")  #background of the text object
l.config(fg="#FFFFFF")  #color of the text with fg

l2 = Label(mains, text = "- This OS imitator software has basic tools.")
l2.config(font =("Times-New-Roman", 25), background="#191970", fg="#FFFFFF", justify="left")    #justify aligns the text
#l2.config(background="#191970")    #if the user doesn't want to have all attributes in one line
#l2.config(fg="#FFFFFF")

l3 = Label(mains, text = "- Built for educational and possibly for commercial purposes.\n- Click on the Start Nightly button to start it!")
l3.config(font =("Times-New-Roman", 25), background="#191970", fg="#FFFFFF", justify="left") 

l4 = Label(mains, text = "\nFeatures of Nightly OS 2")  #title
l4.config(font =("Times-New-Roman", 50)) #font family and size
l4.config(background="#191970")  #background of the text object
l4.config(fg="#FFFFFF")  #color of the text with fg

l5 = Label(mains, text = "- Desktop with Start button and date shower")
l5.config(font =("Times-New-Roman", 25), background="#191970", fg="#FFFFFF", justify="left")
l6 = Label(mains, text = "- Icons which start the programs related to them")
l6.config(font =("Times-New-Roman", 25), background="#191970", fg="#FFFFFF", justify="left")
l7 = Label(mains, text = "- Text editor")
l7.config(font =("Times-New-Roman", 25), background="#191970", fg="#FFFFFF", justify="left")
l8 = Label(mains, text = "- Table editor")
l8.config(font =("Times-New-Roman", 25), background="#191970", fg="#FFFFFF", justify="left")
l9 = Label(mains, text = "- Presentation editor")
l9.config(font =("Times-New-Roman", 25), background="#191970", fg="#FFFFFF", justify="left")
l10 = Label(mains, text = "- Tictactoe game")
l10.config(font =("Times-New-Roman", 25), background="#191970", fg="#FFFFFF", justify="left")
l11 = Label(mains, text = "- Image viewer")
l11.config(font =("Times-New-Roman", 25), background="#191970", fg="#FFFFFF", justify="left")
l12 = Label(mains, text = "- PDF viewer")
l12.config(font =("Times-New-Roman", 25), background="#191970", fg="#FFFFFF", justify="left")
l13 = Label(mains, text = "- Video player")
l13.config(font =("Times-New-Roman", 25), background="#191970", fg="#FFFFFF", justify="left")
l14 = Label(mains, text = "- Browser")
l14.config(font =("Times-New-Roman", 25), background="#191970", fg="#FFFFFF", justify="left")
l15 = Label(mains, text = "- File manager")
l15.config(font =("Times-New-Roman", 25), background="#191970", fg="#FFFFFF", justify="left")

#-----------------------------------------------------------
#starter button
def start_the_OS():
    print("Loading Nightly")
    mains.destroy()
    os.system('desktop.py')    

screen_width = mains.winfo_screenwidth()    #helper variable for the screen width
screen_height = mains.winfo_screenheight()  #helper variable for the screen height
btnStarter = Button(mains, text='Start Nightly', width=15, command=start_the_OS, bg="#1f242d")
btnStarter.configure(font=('Times-New-Roman',25,'bold'),foreground='white')
#btnStarter.place(x = (screen_width * 0.35), y = (screen_height - 200))  #experimental positioning  
btnStarter.place(relx=0.5, rely=0.85, anchor = CENTER)  #center anchor is needed, alongside with the relative x and y values

#-----------------------------------------------------------
l.pack()    #without anchor and justify, text goes for center alignment
l2.pack(anchor="w") #anchor w is needed for aligning the text
l3.pack(anchor="w")
l4.pack()
l5.pack(anchor="w")
l6.pack(anchor="w")
l7.pack(anchor="w")
l8.pack(anchor="w")
l9.pack(anchor="w")
l10.pack(anchor="w")
l11.pack(anchor="w")
l12.pack(anchor="w")
l13.pack(anchor="w")
l14.pack(anchor="w")
l15.pack(anchor="w")

#the window won't get opened without this
mains.mainloop()