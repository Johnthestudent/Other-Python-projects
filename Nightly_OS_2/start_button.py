from tkinter import *
import os

#-----------------------------------------------------------
# Creating the window for loader
# Calling the TK
start_button_root = Tk()

# creating a string of 215 space characters
space=(" ")*215

# It retrieves the screen width of the user's display
screen_width = 300
 
# It retrieves the screen height of the user's display
screen_height = 400

#Using an f-string to construct the window size in the 
#format width x height
start_button_root.geometry(f"{screen_width}x{screen_height}")
#setting the title for the window
start_button_root.title(f"{space}Start button")
start_button_root.configure(bg='#191970')

#-----------------------------------------------------------
#TicTacToe game
def tictactoegame():
    os.system("programs\\tic_tac_toe.py")

#TicTacTooe game button
btnGame = Button(start_button_root, text='Tic-Tac-Toe game', width=15, command=tictactoegame, bg="#1f242d")
btnGame.configure(font=('Times-New-Roman',20,'bold'),foreground='white')
btnGame.place(relx=0.5, rely=0.10, anchor = CENTER)  #center anchor is needed, alongside with the relative x and y values

#-----------------------------------------------------------
#System service
def systemthings():
    os.system("system_stats.py")

#System service button
btnSystem_things = Button(start_button_root, text='System', width=15, command=systemthings, bg="#1f242d")
btnSystem_things.configure(font=('Times-New-Roman',20,'bold'),foreground='white')
btnSystem_things.place(relx=0.5, rely=0.30, anchor = CENTER)  #center anchor is needed, alongside with the relative x and y values

#-----------------------------------------------------------
#Network service
def networkmanager():
    os.system("network_management.py")

#Network service button
btnNetwork = Button(start_button_root, text='Network', width=15, command=networkmanager, bg="#1f242d")
btnNetwork.configure(font=('Times-New-Roman',20,'bold'),foreground='white')
btnNetwork.place(relx=0.5, rely=0.50, anchor = CENTER)  #center anchor is needed, alongside with the relative x and y values

#-----------------------------------------------------------
#Security_management service
def securitymanager():
    os.system("security_management.py")

#Security_management button
btnSecurity = Button(start_button_root, text='Security_manager', width=15, command=securitymanager, bg="#1f242d")
btnSecurity.configure(font=('Times-New-Roman',20,'bold'),foreground='white')
btnSecurity.place(relx=0.5, rely=0.70, anchor = CENTER)  #center anchor is needed, alongside with the relative x and y values

#-----------------------------------------------------------
#Disk_management service
def diskmanager():
    os.system("disk_management.py")

#Disk_management button
btnDisk = Button(start_button_root, text='Disk_management', width=15, command=diskmanager, bg="#1f242d")
btnDisk.configure(font=('Times-New-Roman',20,'bold'),foreground='white')
btnDisk.place(relx=0.5, rely=0.90, anchor = CENTER)  #center anchor is needed, alongside with the relative x and y values

#-----------------------------------------------------------
#the window won't get opened without this
start_button_root.mainloop()