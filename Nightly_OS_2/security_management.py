from tkinter import *

#-----------------------------------------------------------
# Creating the window for loader
# Calling the TK
security_manager = Tk()

# creating a string of 215 space characters
space=(" ")*215

# It retrieves the screen width of the user's display
screen_width = 800
 
# It retrieves the screen height of the user's display
screen_height = 500

#Using an f-string to construct the window size in the 
#format width x height
security_manager.geometry(f"{screen_width}x{screen_height}")
#setting the title for the window
security_manager.title(f"{space}Security manager")
security_manager.configure(bg='#191970')

#the window won't get opened without this
security_manager.mainloop()