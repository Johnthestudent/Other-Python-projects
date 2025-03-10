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
import datetime
import time
import webbrowser

#------------------------------------------------- 
# Creating the window for loader
# Calling the TK
root = Tk()

# creating a string of 215 space characters
space=(" ")*215
# It retrieves the screen width of the user's display
screen_width=root.winfo_screenwidth()
 
# It retrieves the screen height of the user's display
screen_height = root.winfo_screenheight()

#Using an f-string to construct the window size in the 
#format width x height
root.geometry(f"{screen_width}x{screen_height}")
#setting the title for the window
root.title(f"{space}Nightly 2")
bg2 = PhotoImage(file = "img\main_background.png")  #PhotoImage takes file parameter

# Create Canvas 
canvas1 = Canvas(root) #if no width and height are given, then the Canvas takes the values of the Tk object window
  
canvas1.pack(fill = "both", expand = True) #expand True ensures that the image fills the entire area
  
# Display image 
canvas1.create_image( 0, 0, image = bg2,  
                     anchor = "nw") 

#------------------------------------------------- 
#x1, y1, x2, y2 - x and y start point, x and y end point
taskbar = canvas1.create_rectangle(0, 50, screen_width, 110,
                                outline = "white", fill = "#07296a",
                                width = 1)

canvas1.moveto(taskbar, 0, screen_height * 0.89)    #it moves the object to the specified position

#------------------------------------------------- 
now = datetime.datetime.now()
#actual_date = str(now.year) + ":" + str(now.month) #experimental
#print(actual_date) #experimental
my_year = str(now.year) #base value is int, but for concatenation, str type is needed
my_month = str(now.month)
my_day = str(now.day)
my_hour = str(now.hour)
my_minute = str(now.minute)

#if the int value is less than 10, then only one digit is shown
if(now.month < 10):
    my_month = "0" + str(my_month)

if(now.day < 10):
    my_day = "0" + str(my_day)

if(now.hour < 10):
    my_hour = "0" + str(my_hour)

if(now.minute < 10):
    my_minute = "0" + str(my_minute)

#presentable_date = my_year + "." + my_month + "." + my_day + "." + my_hour + ":" + my_minute   #experimental

#print(presentable_date)    #experimental

#StringVar() + set() and textvariable ensure that the text of a Label can be a variable
#presentable_date = StringVar() #experimental, static date
#presentable_date.set(my_year + "." + my_month + "." + my_day + "." + my_hour + ":" + my_minute) #experimental, static date

#strftime's special format is used
def update_time():
    current_time = time.strftime('%Y.%m.%d. %H:%M')
    label_date.config(text=current_time)
    root.after(1000, update_time)  # Update every 1000 milliseconds (1 second)

label_date = Label(root, text="")   #text has to be empty, so that it can be refilled after every second
label_date.config(font =("Times-New-Roman", 25), background="#07296a", fg="#FFFFFF")    #justify aligns the text

label_date.pack()   #first the label has to be packed, and after that can it be poisitoned
label_date.place(relx=0.9, rely=0.974, anchor = CENTER)  #center anchor is needed, alongside with the relative x and y values

update_time()

#-----------------------------------------------------------
#browser function
def open_browser():
    webbrowser.open_new(r"https://www.google.com/")

#Browser icon
button_for_browser = Button(root, text='Browser', width=10, command=open_browser, bg="#1f242d")
button_for_browser.configure(font=('Times-New-Roman',20,'bold'),foreground='white')
button_for_browser.place(relx=0.07, rely=0.26, anchor = CENTER)  #center anchor is needed, alongside with the relative x and y values

#Browser icon image
# Load the image 
iconimage = PhotoImage(file = "img\icon_image.png") #image name mustn't start with escape character first capital (like n, b, r, t, v, f)

image_label = Label(root, image=iconimage)
image_label.pack()
image_label.config(width=175, height=175, borderwidth=1, relief="solid")   #config for image label has to be after pack
image_label.place(relx=0.07, rely=0.13, anchor = CENTER)

#-----------------------------------------------------------
#text editor function
def open_text_editor():
    os.system("programs\\nightly_text_editor.py")   #double \ is needed to ensure that it won't consider the first character as an escape character

#Text Editor icon
button_for_text_editor = Button(root, text='Text Editor', width=10, command=open_text_editor, bg="#1f242d")
button_for_text_editor.configure(font=('Times-New-Roman',20,'bold'),foreground='white')
button_for_text_editor.place(relx=0.21, rely=0.26, anchor = CENTER)  #center anchor is needed, alongside with the relative x and y values    

#Text editor icon image
# Load the image 
iconimage2 = PhotoImage(file = "img\icon_image_for_text_editor.png") #image name mustn't start with escape character first capital (like n, b, r, t, v, f)

# Create a label to display the image
image_label2 = Label(root, image=iconimage2)
image_label2.pack()
image_label2.config(width=175, height=175, borderwidth=1, relief="solid")   #config for image label has to be after pack
image_label2.place(relx=0.21, rely=0.13, anchor = CENTER)

#-----------------------------------------------------------
#table editor function
def open_table_editor():
    os.system("programs\\nightly_table_editor.py")   #double \ is needed to ensure that it won't consider the first character as an escape character

#Table Editor icon
button_for_table_editor = Button(root, text='Table Editor', width=10, command=open_table_editor, bg="#1f242d")
button_for_table_editor.configure(font=('Times-New-Roman',20,'bold'),foreground='white')
button_for_table_editor.place(relx=0.35, rely=0.26, anchor = CENTER)  #center anchor is needed, alongside with the relative x and y values    

#Table editor icon image
# Load the image 
iconimage3 = PhotoImage(file = "img\icon_image_for_table_editor.png") #image name mustn't start with escape character first capital (like n, b, r, t, v, f)

# Create a label to display the image
image_label3 = Label(root, image=iconimage3)
image_label3.pack()
image_label3.config(width=175, height=175, borderwidth=1, relief="solid")   #config for image label has to be after pack
image_label3.place(relx=0.35, rely=0.13, anchor = CENTER)

#-----------------------------------------------------------
#presentation editor function
def open_presentation_editor():
    os.system("programs\\nightly_presentation_editor.py")   #double \ is needed to ensure that it won't consider the first character as an escape character

#Presentation Editor icon
button_for_presentation_editor = Button(root, text='Presentation Editor', width=15, command=open_presentation_editor, bg="#1f242d")
button_for_presentation_editor.configure(font=('Times-New-Roman',20,'bold'),foreground='white')
button_for_presentation_editor.place(relx=0.49, rely=0.26, anchor = CENTER)  #center anchor is needed, alongside with the relative x and y values        

#Presentation editor icon image
# Load the image 
iconimage4 = PhotoImage(file = "img\icon_image_for_presentation_editor.png") #image name mustn't start with escape character first capital (like n, b, r, t, v, f)

# Create a label to display the image
image_label4 = Label(root, image=iconimage4)
image_label4.pack()
image_label4.config(width=175, height=175, borderwidth=1, relief="solid")   #config for image label has to be after pack
image_label4.place(relx=0.49, rely=0.13, anchor = CENTER)

#-----------------------------------------------------------
#video player function
def open_video_player():
    os.system("programs\\nightly_video_player.py")   #double \ is needed to ensure that it won't consider the first character as an escape character

#Presentation Editor icon
button_for_video_player = Button(root, text='Video player', width=10, command=open_video_player, bg="#1f242d")
button_for_video_player.configure(font=('Times-New-Roman',20,'bold'),foreground='white')
button_for_video_player.place(relx=0.63, rely=0.26, anchor = CENTER)  #center anchor is needed, alongside with the relative x and y values        

#Presentation editor icon image
# Load the image 
iconimage5 = PhotoImage(file = "img\icon_image_for_video_player.png") #image name mustn't start with escape character first capital (like n, b, r, t, v, f)

# Create a label to display the image
image_label5 = Label(root, image=iconimage5)
image_label5.pack()
image_label5.config(width=175, height=175, borderwidth=1, relief="solid")   #config for image label has to be after pack
image_label5.place(relx=0.63, rely=0.13, anchor = CENTER)

#-----------------------------------------------------------
#start menu function
def open_start_menu():
    os.system('start_button.py')

#Start button
btnStarter = Button(root, text='Start', width=10, command=open_start_menu, bg="#1f242d")
btnStarter.configure(font=('Times-New-Roman',20,'bold'),foreground='white')
btnStarter.place(relx=0.05, rely=0.974, anchor = CENTER)  #center anchor is needed, alongside with the relative x and y values

#-----------------------------------------------------------
#image viewer function
def open_image_viewer():
    os.system("programs\image_viewer.py")   #double \ is needed to ensure that it won't consider the first character as an escape character

#Image viewer button
btnPDFViewer = Button(root, text='Image viewer', width=12, command=open_image_viewer, bg="#1f242d")
btnPDFViewer.configure(font=('Times-New-Roman',20,'bold'),foreground='white')
btnPDFViewer.place(relx=0.18, rely=0.974, anchor = CENTER)  #center anchor is needed, alongside with the relative x and y values

#-----------------------------------------------------------
#PDF viewer function
def open_pdf_viewer():
    os.system("programs\pdf_viewer.py")   #double \ is needed to ensure that it won't consider the first character as an escape character

#PDF viewer button
btnImageViewer = Button(root, text='PDF viewer', width=12, command=open_pdf_viewer, bg="#1f242d")
btnImageViewer.configure(font=('Times-New-Roman',20,'bold'),foreground='white')
btnImageViewer.place(relx=0.3, rely=0.974, anchor = CENTER)  #center anchor is needed, alongside with the relative x and y values

#-----------------------------------------------------------
#Help shower function
def help_nightly_os():
    os.system("helpnightly.py")

#Help shower button
btnHelper = Button(root, text='Help', width=12, command=help_nightly_os, bg="#1f242d")
btnHelper.configure(font=('Times-New-Roman',20,'bold'),foreground='white')
btnHelper.place(relx=0.44, rely=0.974, anchor = CENTER)  #center anchor is needed, alongside with the relative x and y values

#the window won't get opened without this
root.mainloop()