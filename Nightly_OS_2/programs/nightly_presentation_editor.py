from tkinter import *
import shutil
import sys
import os
import cv2
from PIL import Image, ImageFilter, ImageOps, ImageChops, ImageTk, ImageEnhance

#-----------------------------------------------------------
# Creating the window for loader
# Calling the TK
presentation_editor = Tk()

# creating a string of 215 space characters
space=(" ")*215

# It retrieves the screen width of the user's display
screen_width = presentation_editor.winfo_screenwidth()
 
# It retrieves the screen height of the user's display
screen_height = presentation_editor.winfo_screenheight()

#Using an f-string to construct the window size in the 
#format width x height
presentation_editor.geometry(f"{screen_width}x{screen_height}")
#setting the title for the window
presentation_editor.title(f"{space}Nightly's Presentation Editor")
presentation_editor.configure(bg='#202020')

#-----------------------------------------------------------
first_slide_title = Label(presentation_editor, text = "Slide 1")  #title
first_slide_title.config(font =("Times-New-Roman", 50), width=8) #font family and size
first_slide_title.place(relx=0.1, rely=0.25, anchor = CENTER)

# Create a Text widget
text_widget = Text(presentation_editor, height=20, width=40)
text_widget.place(relx=0.1, rely=0.45, anchor = CENTER)

#-----------------------------------------------------------
#Adding a new slide
def add_slide2():
    #slide 2
    global new_slide_title
    global text_widget2
    new_slide_title = Label(presentation_editor, text = "Slide 2")  #title
    new_slide_title.config(font =("Times-New-Roman", 50), width=8) #font family and size
    new_slide_title.place(relx=0.3, rely=0.25, anchor = CENTER)
    text_widget2 = Text(presentation_editor, height=20, width=40)
    text_widget2.place(relx=0.3, rely=0.45, anchor = CENTER)

#removing a slide
def remove_slide2():
    new_slide_title.destroy()
    text_widget2.destroy()

#-----------------------------------------------------------
#Adding a new slide
def add_slide3():
    #slide 3
    global new_slide_title2
    global text_widget3
    new_slide_title2 = Label(presentation_editor, text = "Slide 3")  #title
    new_slide_title2.config(font =("Times-New-Roman", 50), width=8) #font family and size
    new_slide_title2.place(relx=0.5, rely=0.25, anchor = CENTER)
    text_widget3 = Text(presentation_editor, height=20, width=40)
    text_widget3.place(relx=0.5, rely=0.45, anchor = CENTER)

#removing a slide
def remove_slide3():
    new_slide_title2.destroy()
    text_widget3.destroy()

#-----------------------------------------------------------
#Adding a new slide
def add_slide4():
    #slide 4
    global new_slide_title3
    global text_widget4
    new_slide_title3 = Label(presentation_editor, text = "Slide 4")  #title
    new_slide_title3.config(font =("Times-New-Roman", 50), width=8) #font family and size
    new_slide_title3.place(relx=0.7, rely=0.25, anchor = CENTER)
    text_widget4 = Text(presentation_editor, height=20, width=40)
    text_widget4.place(relx=0.7, rely=0.45, anchor = CENTER)

#removing a slide
def remove_slide4():
    new_slide_title3.destroy()
    text_widget4.destroy()

#-----------------------------------------------------------
#button to remove second slide
buttonremove2ndSlide= Button(presentation_editor, text='Remove 2nd slide', width=15, command=remove_slide2, bg="#1f242d")
buttonremove2ndSlide.configure(font=('Arial',25,'bold'),foreground='white')
buttonremove2ndSlide.place(relx=0.3, rely=0.8, anchor = CENTER)

#-----------------------------------------------------------
#button to add third slide
buttonNewSlide3rd = Button(presentation_editor, text='Add 3rd slide', width=15, command=add_slide3, bg="#1f242d")
buttonNewSlide3rd.configure(font=('Arial',25,'bold'),foreground='white')
buttonNewSlide3rd.place(relx=0.3, rely=0.7, anchor = CENTER)

#button to remove third slide
buttonremove3rdSlide= Button(presentation_editor, text='Remove 3rd slide', width=15, command=remove_slide3, bg="#1f242d")
buttonremove3rdSlide.configure(font=('Arial',25,'bold'),foreground='white')
buttonremove3rdSlide.place(relx=0.5, rely=0.8, anchor = CENTER)

#-----------------------------------------------------------
#button to add fourth slide
buttonNewSlide4th = Button(presentation_editor, text='Add 4th slide', width=15, command=add_slide4, bg="#1f242d")
buttonNewSlide4th.configure(font=('Arial',25,'bold'),foreground='white')
buttonNewSlide4th.place(relx=0.5, rely=0.7, anchor = CENTER)

#button to remove fourth slide
buttonremove4thSlide= Button(presentation_editor, text='Remove 4th slide', width=15, command=remove_slide4, bg="#1f242d")
buttonremove4thSlide.configure(font=('Arial',25,'bold'),foreground='white')
buttonremove4thSlide.place(relx=0.7, rely=0.7, anchor = CENTER)

#-----------------------------------------------------------
#button to add second slide
buttonNewSlide = Button(presentation_editor, text='Add a new slide', width=15, command=add_slide2, bg="#1f242d")
buttonNewSlide.configure(font=('Arial',25,'bold'),foreground='white')
buttonNewSlide.place(relx=0.1, rely=0.7, anchor = CENTER) 

#-----------------------------------------------------------
#swim in animation
def swim_for_slide1(ymove=100):
    if ymove > 0:
        first_slide_title.place(x=0, y=ymove)
        presentation_editor.after(30, swim_for_slide1, ymove-5) # in 30 milliseconds, call this function again with y-5

#button to do swim animation on the first slide title
buttonSwim_Slide_Title1 = Button(presentation_editor, text='Slide 1 title swim in', width=15, command=swim_for_slide1, bg="#1f242d")
buttonSwim_Slide_Title1.configure(font=('Arial',25,'bold'),foreground='white')
buttonSwim_Slide_Title1.place(relx=0.9, rely=0.1, anchor = CENTER)

#-----------------------------------------------------------
#swim in animation
def swim_for_slide2(ymove=100):
    if ymove > 0:
        new_slide_title.place(x=0, y=ymove)
        presentation_editor.after(30, swim_for_slide2, ymove-5) # in 30 milliseconds, call this function again with y-5

#button to do swim animation on the second slide title
buttonSwim_Slide_Title2 = Button(presentation_editor, text='Slide 2 title swim in', width=15, command=swim_for_slide2, bg="#1f242d")
buttonSwim_Slide_Title2.configure(font=('Arial',25,'bold'),foreground='white')
buttonSwim_Slide_Title2.place(relx=0.9, rely=0.2, anchor = CENTER)

#-----------------------------------------------------------
#swim in animation
def swim_for_slide3(ymove=100):
    if ymove > 0:
        new_slide_title2.place(x=0, y=ymove)
        presentation_editor.after(30, swim_for_slide3, ymove-5) # in 30 milliseconds, call this function again with y-5

#button to do swim animation on the third slide title
buttonSwim_Slide_Title3 = Button(presentation_editor, text='Slide 3 title swim in', width=15, command=swim_for_slide3, bg="#1f242d")
buttonSwim_Slide_Title3.configure(font=('Arial',25,'bold'),foreground='white')
buttonSwim_Slide_Title3.place(relx=0.9, rely=0.3, anchor = CENTER)

#-----------------------------------------------------------
#swim in animation
def swim_for_slide4(ymove=100):
    if ymove > 0:
        new_slide_title3.place(x=0, y=ymove)
        presentation_editor.after(30, swim_for_slide4, ymove-5) # in 30 milliseconds, call this function again with y-5

#button to do swim animation on the fourth slide title
buttonSwim_Slide_Title4 = Button(presentation_editor, text='Slide 4 title swim in', width=15, command=swim_for_slide4, bg="#1f242d")
buttonSwim_Slide_Title4.configure(font=('Arial',25,'bold'),foreground='white')
buttonSwim_Slide_Title4.place(relx=0.9, rely=0.4, anchor = CENTER)

#-----------------------------------------------------------
#changing font color
#if it is dynamic that the function takes the name of the slide title, as a param, then the animation will make it disappear
def fade_font_color_slide1(j=0):
    if j < 10:
        colors = ('#202020', '#313131' ,'#414141', '#535353', '#727272' ,'#939393' ,'#bdbdbd' , '#dbdbdb', '#ececec','#f0f0f0')
        first_slide_title.config(fg=colors[j])
        first_slide_title.after(100, fade_font_color_slide1, j+1)

#-----------------------------------------------------------
#fading animation
def fade_slide1(i=0):
    #slide title original background color: f0f0f0
    if i < 10:
        colors = ('#f0f0f0', '#ececec' ,'#dbdbdb', '#bdbdbd', '#939393' ,'#727272' ,'#535353' , '#414141', '#313131','#202020')
        first_slide_title.config(bg=colors[i])
        first_slide_title.after(100, fade_slide1, i+1)
    fade_font_color_slide1()

#button to do fade animation on the first slide title
buttonFade_Slide_Title1 = Button(presentation_editor, text='Slide 1 title fade', width=15, command=fade_slide1, bg="#1f242d")
buttonFade_Slide_Title1.configure(font=('Arial',25,'bold'),foreground='white')
buttonFade_Slide_Title1.place(relx=0.9, rely=0.5, anchor = CENTER)

#-----------------------------------------------------------
#changing font color
#if it is dynamic that the function takes the name of the slide title, as a param, then the animation will make it disappear
def fade_font_color_slide2(j=0):
    if j < 10:
        colors = ('#202020', '#313131' ,'#414141', '#535353', '#727272' ,'#939393' ,'#bdbdbd' , '#dbdbdb', '#ececec','#f0f0f0')
        new_slide_title.config(fg=colors[j])
        new_slide_title.after(100, fade_font_color_slide2, j+1)

#-----------------------------------------------------------
#fading animation
def fade_slide2(i=0):
    #slide title original background color: f0f0f0
    if i < 10:
        colors = ('#f0f0f0', '#ececec' ,'#dbdbdb', '#bdbdbd', '#939393' ,'#727272' ,'#535353' , '#414141', '#313131','#202020')
        new_slide_title.config(bg=colors[i])
        new_slide_title.after(100, fade_slide2, i+1)
    fade_font_color_slide2()

#button to do fade animation on the first slide title
buttonFade_Slide_Title2 = Button(presentation_editor, text='Slide 2 title fade', width=15, command=fade_slide2, bg="#1f242d")
buttonFade_Slide_Title2.configure(font=('Arial',25,'bold'),foreground='white')
buttonFade_Slide_Title2.place(relx=0.9, rely=0.6, anchor = CENTER)

#-----------------------------------------------------------
#changing font color
#if it is dynamic that the function takes the name of the slide title, as a param, then the animation will make it disappear
def fade_font_color_slide3(j=0):
    if j < 10:
        colors = ('#202020', '#313131' ,'#414141', '#535353', '#727272' ,'#939393' ,'#bdbdbd' , '#dbdbdb', '#ececec','#f0f0f0')
        new_slide_title2.config(fg=colors[j])
        new_slide_title2.after(100, fade_font_color_slide3, j+1)

#-----------------------------------------------------------
#fading animation
def fade_slide3(i=0):
    #slide title original background color: f0f0f0
    if i < 10:
        colors = ('#f0f0f0', '#ececec' ,'#dbdbdb', '#bdbdbd', '#939393' ,'#727272' ,'#535353' , '#414141', '#313131','#202020')
        new_slide_title2.config(bg=colors[i])
        new_slide_title2.after(100, fade_slide3, i+1)
    fade_font_color_slide3()

#button to do fade animation on the first slide title
buttonFade_Slide_Title3 = Button(presentation_editor, text='Slide 3 title fade', width=15, command=fade_slide3, bg="#1f242d")
buttonFade_Slide_Title3.configure(font=('Arial',25,'bold'),foreground='white')
buttonFade_Slide_Title3.place(relx=0.9, rely=0.7, anchor = CENTER)

#-----------------------------------------------------------
#changing font color
#if it is dynamic that the function takes the name of the slide title, as a param, then the animation will make it disappear
def fade_font_color_slide4(j=0):
    if j < 10:
        colors = ('#202020', '#313131' ,'#414141', '#535353', '#727272' ,'#939393' ,'#bdbdbd' , '#dbdbdb', '#ececec','#f0f0f0')
        new_slide_title3.config(fg=colors[j])
        new_slide_title3.after(100, fade_font_color_slide4, j+1)
        
#-----------------------------------------------------------
#fading animation
def fade_slide4(i=0):
    #slide title original background color: f0f0f0
    if i < 10:
        colors = ('#f0f0f0', '#ececec' ,'#dbdbdb', '#bdbdbd', '#939393' ,'#727272' ,'#535353' , '#414141', '#313131','#202020')
        new_slide_title3.config(bg=colors[i])
        new_slide_title3.after(100, fade_slide4, i+1)
    fade_font_color_slide4()

#button to do fade animation on the first slide title
buttonFade_Slide_Title4 = Button(presentation_editor, text='Slide 4 title fade', width=15, command=fade_slide4, bg="#1f242d")
buttonFade_Slide_Title4.configure(font=('Arial',25,'bold'),foreground='white')
buttonFade_Slide_Title4.place(relx=0.9, rely=0.8, anchor = CENTER) 

#the window won't get opened without this
presentation_editor.mainloop()