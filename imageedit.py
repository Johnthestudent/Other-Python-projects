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
mains.title(f"{space}Image Editor")
mains.configure(bg='#323946')

img = Image.open("Tengelice.jpg")
img = img.resize((759, 838))
panel = Label(mains)
panel.grid(row=0, column=0, rowspan=12, padx=50, pady=50)
displayimage(img)

#reset the image
#the function ensures that the user can go back to the original image
#by undoing the previously done operations
def reset_image():
	img = Image.open("Tengelice.jpg")
	img = img.resize((759, 838))
	displayimage(img)

#reset_image button
#RESET_IMG stores the Button widget to thumbnail the image
#Inside the widget,
RESET_IMG = Button(mains, text='Reset image', width=25, command=reset_image, bg="#1f242d")
RESET_IMG.configure(font=('poppins',11,'bold'),foreground='white')
RESET_IMG.place(x=1500,y=625)

#open the image with the default image viewer
#filtered_img.show()

#save as png
#filtered_img.save("result.png", 'png')

#save as jpg
#filtered_img.save("result.jpg", 'jpg')

# function to save the image as jpg
# This function saves the image as jpg
# then updates the image
# and after that, displays the image using the 'displayimage' function
def jpg_save(): 
	img = cv2.imread("Tengelice.jpg")
	cv2.imwrite("result.jpg", new_img)
	
#jpg_save button
#btnJPG_Save stores the Button widget to thumbnail the image
#Inside the widget,
btnJPG_Save = Button(mains, text='Save as jpg', width=25, command=jpg_save, bg="#1f242d")
btnJPG_Save.configure(font=('poppins',11,'bold'),foreground='white')
btnJPG_Save.place(x=1500,y=525)
	
#save as svg
#filtered_img.save("result.svg", 'svg')

# CV cannot save to svg
# function to save the image as png
# This function saves the image as png
# then updates the image
# and after that, displays the image using the 'displayimage' function
def png_save():
	#experimental
	"""global img
	img.save("result.svg", 'svg')
	displayimage(img)"""
	
	#experimental
	"""image_folder = sys.argv[1]
	output_folder = sys.argv[2]
	
	if not os.path.exists(output_folder):
		os.makedirs(output_folder)
	
	for filename in os.listdir(image_folder):
		#img = Image.open(f"{image_folder}{filename}")
		clean_name = os.path.splitext(filename)[0]
		img.save(f"{output_folder}{clean_name}.svg", "svg")"""
	
	#experimental
	"""
	a = tkinter.PhotoImage(file="Tengelice.jpg")
	a.save("result.svg")"""
	
	#experimental
	"""global img
	savefile = filedialog.asksaveasfile(defaultextension=".svg")
	outputImage.save(savefile)"""
	
	#experimental
	"""
	file = filedialog.asksaveasfilename(intialdir = "D:/",
	filetypes=(('PNG File', '.PNG')))
	
	life = self.file + ".PNG"
	ImageGrab.grab(img).save(self.file)"""
	img = cv2.imread("Tengelice.jpg")
	cv2.imwrite("result.png", img)

#png_save button
#btnPNG_Save stores the Button widget to thumbnail the image
#Inside the widget,
btnPNG_Save = Button(mains, text='Save as png', width=25, command=png_save, bg="#1f242d")
btnPNG_Save.configure(font=('poppins',11,'bold'),foreground='white')
btnPNG_Save.place(x=1500,y=425)

#create a thumbnail
#filtered_img.thumbnail((128, 128))

# function to thumbnail the image
# This function thumbnails the image
# then updates the image
# and after that, displays the image using the 'displayimage' function
def thumbnailing():
    global img
    new_img = img.resize((128, 128))
    displayimage(new_img)

#thumbnail button
#btnThumbnail stores the Button widget to thumbnail the image
#Inside the widget,
btnThumbnail = Button(mains, text='Thumbnail', width=25, command=thumbnailing, bg="#1f242d")
btnThumbnail.configure(font=('poppins',11,'bold'),foreground='white')
btnThumbnail.place(x=1500,y=125)

#segment of an image
#filtered_img.crop((100, 100, 400, 400))

# function to crop the image
# This function crops the image
# then updates the image
# and after that, displays the image using the 'displayimage' function
def cropping():
    global img
    new_img = img.crop((100, 100, 400, 400))
    displayimage(new_img)

#crop button
#btnCrop stores the Button widget to crop the image
#Inside the widget,
btnCrop = Button(mains, text='Crop', width=25, command=cropping, bg="#1f242d")
btnCrop.configure(font=('poppins',11,'bold'),foreground='white')
btnCrop.place(x=1200,y=125)

#rotate image counter-clockwise
#filtered_img = img.rotate(90)

# function to rotate the image clockwise
# This function rotates the image clockwise
# then updates the image
# and after that, displays the image using the 'displayimage' function
def rotate_right():
    global img
    new_img = img.rotate(-90)
    displayimage(new_img)

#rotate button
#btnRotateRight stores the Button widget to rotate the image
#Inside the widget,
btnRotateRight = Button(mains, text='Rotate (clockwise)', width=25, command=rotate_right, bg="#1f242d")
btnRotateRight.configure(font=('poppins',11,'bold'),foreground='white')
btnRotateRight.place(x=1200,y=225)

#rotate image clockwise
#filtered_img = img.rotate(-90)

# function to rotate the image counter-clockwise
# This function rotates the image counter-clockwise
# then updates the image
# and after that, displays the image using the 'displayimage' function
def rotate_left():
    global img
    new_img = img.rotate(90)
    displayimage(new_img)

#rotate button
#btnRotateLeft stores the Button widget to rotate the image
#Inside the widget,
btnRotateLeft = Button(mains, text='Rotate (counter-clockwise)', width=25, command=rotate_left, bg="#1f242d")
btnRotateLeft.configure(font=('poppins',11,'bold'),foreground='white')
btnRotateLeft.place(x=1200,y=325)

#transform image into grayscale mode
#filtered_img = img.convert('L')

# function to change the image mode to Grayscale
# This function turns the image to Grayscale
# then updates the image
# and after that, displays the image using the 'displayimage' function
def Grayscalemode():
    global img
    new_img = img.convert('L')
    displayimage(new_img)

#Grayscale button
#btnGrayscale stores the Button widget to blur the image
btnGrayscale = Button(mains, text='Grayscale', width=25, command=Grayscalemode, bg="#1f242d")
btnGrayscale.configure(font=('poppins',11,'bold'),foreground='white')
btnGrayscale.place(x=1500,y=325)

#convert the image into RGB mode
#filtered_img = img.convert('RGB')

# function to change the image mode to RGB
# This function turns the image to RGB
# then updates the image
# and after that, displays the image using the 'displayimage' function
def RGBmode():
    global img
    new_img = img.convert('RGB')
    displayimage(new_img)

#RGB button
#btnRGB stores the Button widget to blur the image
btnRGB = Button(mains, text='RGB', width=25, command=RGBmode, bg="#1f242d")
btnRGB.configure(font=('poppins',11,'bold'),foreground='white')
btnRGB.place(x=1500,y=225)

#blur the image
#filtered_img = img.filter(ImageFilter.BLUR)

# function to Blur the image 
# This function applies a blur filter to the image
# then updates the image
# and after that, displays the image using the 'displayimage' function
def blur():
    global img
    new_img = img.filter(ImageFilter.BLUR)
    displayimage(new_img)

#Blur button
#btnBlur stores the Button widget to blur the image
btnBlur = Button(mains, text='Blur', width=25, command=blur, bg="#1f242d")
btnBlur.configure(font=('poppins',11,'bold'),foreground='white')
btnBlur.place(x=1200,y=425)

#contour the image
#filtered_img = img.filter(ImageFilter.CONTOUR)

# function to Contour the image 
# This function applies a contour filter to the image
# then updates the image
# and after that, displays the image using the 'displayimage' function
def contour():
    global img
    new_img = img.filter(ImageFilter.CONTOUR)
    displayimage(new_img)

#Contour button
#btnContour stores the Button widget to contour the image
btnContour = Button(mains, text='Contour', width=25, command=contour, bg="#1f242d")
btnContour.configure(font=('poppins',11,'bold'),foreground='white')
btnContour.place(x=1200,y=525)

#sharpen the image
#filtered_img = img.filter(ImageFilter.SHARPEN)

# function to Sharpen the image 
# This function applies a sharpen filter to the image
# then updates the image
# and after that, displays the image using the 'displayimage' function
def sharpen():
    global img
    new_img = img.filter(ImageFilter.SHARPEN)
    displayimage(new_img)

#Sharpen button
#btnSharpen stores the Button widget to sharpen the image
btnSharpen = Button(mains, text='Sharpen', width=25, command=sharpen, bg="#1f242d")
btnSharpen.configure(font=('poppins',11,'bold'),foreground='white')
btnSharpen.place(x=1200,y=625)

#invert the image
#filtered_img = PIL.ImageOps.invert(img)

# function to Invert the image 
# This function applies an invert filter to the image
# then updates the image
# and after that, displays the image using the 'displayimage' function
def invert():
    global img
    new_img = PIL.ImageOps.invert(img)
    displayimage(new_img)

#Invert button
#btnInvert stores the Button widget to invert the image
btnInvert = Button(mains, text='Invert', width=25, command=invert, bg="#1f242d")
btnInvert.configure(font=('poppins',11,'bold'),foreground='white')
btnInvert.place(x=1200,y=725)

#mirror the image
#filtered_img = PIL.ImageOps.mirror(img)

# function to Mirror the image 
# This function mirrors the image
# then updates the image
# and after that, displays the image using the 'displayimage' function
def mirror():
    global img
    new_img = PIL.ImageOps.mirror(img)
    displayimage(new_img)

#Mirror button
#btnMirror stores the Button widget to mirror the image
btnMirror = Button(mains, text='Mirror', width=25, command=mirror, bg="#1f242d")
btnMirror.configure(font=('poppins',11,'bold'),foreground='white')
btnMirror.place(x=1200,y=825)

#flip the image
#filtered_img = PIL.ImageOps.flip(img)

# function to Flip the image 
# This function flips the image
# then updates the image
# and after that, displays the image using the 'displayimage' function
def flip():
    global img
    new_img = PIL.ImageOps.flip(img)
    displayimage(new_img)

#Flip button
#btnFlip stores the Button widget to flip the image
btnFlip = Button(mains, text='Flip', width=25, command=flip, bg="#1f242d")
btnFlip.configure(font=('poppins',11,'bold'),foreground='white')
btnFlip.place(x=1200,y=925)

#experimental purposes
#print(tkinter.TkVersion)

#the window won't get opened without this
mains.mainloop()
