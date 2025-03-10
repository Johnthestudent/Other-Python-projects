from tkinter import *
import shutil
import sys
import os
import cv2
import subprocess

#-----------------------------------------------------------
# Creating the window for loader
# Calling the TK
network_manager = Tk()

# creating a string of 215 space characters
space=(" ")*215

# It retrieves the screen width of the user's display
screen_width = 800
 
# It retrieves the screen height of the user's display
screen_height = 500

#Using an f-string to construct the window size in the 
#format width x height
network_manager.geometry(f"{screen_width}x{screen_height}")
#setting the title for the window
network_manager.title(f"{space}Network manager")
network_manager.configure(bg='#202020')

#-----------------------------------------------------------
try:
    # using the check_output() for having the network term retrieval 
    devices = subprocess.check_output(['netsh','wlan','show','network']) 

    # decode it to strings 
    devices = devices.decode('ascii') 
    devices= devices.replace("\r","") 

    networks_to_show = StringVar()
    networks_to_show.set(devices)

    label_devices= Label(network_manager, textvariable=networks_to_show)   #text has to be empty, so that it can be refilled after every second
    label_devices.config(font =("Times-New-Roman", 25), background="#202020", fg="#FFFFFF")    #justify aligns the text

    label_devices.pack()   #first the label has to be packed, and after that can it be poisitoned
    label_devices.place(relx=0.5, rely=0.5, anchor = CENTER)  #center anchor is needed, alongside with the relative x and y values
except:
    label_devices= Label(network_manager, text="There was an error!")   #text has to be empty, so that it can be refilled after every second
    label_devices.config(font =("Times-New-Roman", 25), background="#202020", fg="#FFFFFF")    #justify aligns the text

    label_devices.pack()   #first the label has to be packed, and after that can it be poisitoned
    label_devices.place(relx=0.5, rely=0.5, anchor = CENTER)  #center anchor is needed, alongside with the relative x and y values

#the window won't get opened without this
network_manager.mainloop()