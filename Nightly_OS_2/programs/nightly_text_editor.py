from tkinter import *
from tkinter import filedialog
import shutil
import sys
import os
import cv2
from tkinter import filedialog

#-----------------------------------------------------------
# Creating the window for loader
# Calling the TK
text_editor = Tk()

# creating a string of 215 space characters
space=(" ")*215

# It retrieves the screen width of the user's display
screen_width = text_editor.winfo_screenwidth()
 
# It retrieves the screen height of the user's display
screen_height = text_editor.winfo_screenheight()

#Using an f-string to construct the window size in the 
#format width x height
text_editor.geometry(f"{screen_width}x{screen_height}")
#setting the title for the window
text_editor.title(f"{space}Nightly's Text Editor")
text_editor.configure(bg='#202020')

#-----------------------------------------------------------
# Create a Text widget
text_widget = Text(text_editor, height=30, width=70)
text_widget.pack()

#-----------------------------------------------------------
#Create an Exit button.
b1= Button(text_editor, text='Exit', width=15, command=text_editor.destroy, bg="#1f242d")
b1.configure(font=('Times-New-Roman',25,'bold'),foreground='white')
b1.place(relx=0.1, rely=0.2, anchor = CENTER) 

#-----------------------------------------------------------
#Change to Arial font
def change_to_Arial():
    text_widget.configure(font=('Arial'))

buttonArial = Button(text_editor, text='Arial', width=15, command=change_to_Arial, bg="#1f242d")
buttonArial.configure(font=('Arial',25,'bold'),foreground='white')
buttonArial.place(relx=0.1, rely=0.3, anchor = CENTER) 

#-----------------------------------------------------------
#Change to Calibri font
def change_to_Calibri():
    text_widget.configure(font=('Calibri'))

buttonCalibri = Button(text_editor, text='Calibri', width=15, command=change_to_Calibri, bg="#1f242d")
buttonCalibri.configure(font=('Calibri',29,'bold'),foreground='white')
buttonCalibri.place(relx=0.1, rely=0.4, anchor = CENTER)

#-----------------------------------------------------------
#Change to Papyrus font
def change_to_Papyrus():
    text_widget.configure(font=('Papyrus'))

buttonPapyrus = Button(text_editor, text='Papyrus', width=15, command=change_to_Papyrus, bg="#1f242d")
buttonPapyrus.configure(font=('Papyrus',20,'bold'),foreground='white')
buttonPapyrus.place(relx=0.1, rely=0.5, anchor = CENTER)

#-----------------------------------------------------------
#Change to Times New Roman font
def change_to_Roman():
    text_widget.configure(font=('Times-New-Roman'))

buttonRoman = Button(text_editor, text='Roman', width=15, command=change_to_Roman, bg="#1f242d")
buttonRoman.configure(font=('Times-New-Roman',25,'bold'),foreground='white')
buttonRoman.place(relx=0.1, rely=0.6, anchor = CENTER) 

#-----------------------------------------------------------
#Load file option
#Experimental, static, it opens an already defined name having file
"""
def load_text():
    with open('sampletxt01.txt', 'r') as file:
        data = file.read()
        text_widget.insert(END, data)
"""

#main file opener, it opens random file, searching it from the OS
def open_file():
    file_path = filedialog.askopenfilename(
        title="Select a Text File", filetypes=[("Text files", "*.txt"), ("All files", "*.*")])
    if file_path:
        with open(file_path, 'r') as file:
            content = file.read()
            text_widget.delete(1.0, END)  # Clear previous content
            text_widget.insert(END, content)

# Create a button to open the file
open_button = Button(text_editor, text="Open file", command=open_file, bg="#1f242d")
open_button.configure(font=('Arial',25,'bold'),foreground='white')
open_button.place(relx=0.8, rely=0.20, anchor = CENTER)

#-----------------------------------------------------------
#save the text widget content as a text file
def save_file():
    file_name = filedialog.asksaveasfilename(defaultextension=".txt",
        title="Save Text File as (don't forget to put .txt after the file name)", filetypes=[("Text files", "*.txt"), ("All files", "*.*")])
    if file_name:
        f = open(file_name, 'w')
        contents = text_widget.get(1.0, END)
        f.write(contents)
        f.close()

# Create a button to save the file
save_button = Button(text_editor, text="Save file", command=save_file, bg="#1f242d")
save_button.configure(font=('Arial',25,'bold'),foreground='white')
save_button.place(relx=0.8, rely=0.30, anchor = CENTER)

#the window won't get opened without this
text_editor.mainloop()