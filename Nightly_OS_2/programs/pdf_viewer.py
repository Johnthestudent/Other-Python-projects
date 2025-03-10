from pypdf import PdfReader, PdfWriter
import PyPDF2
from PyPDF2 import PdfFileReader, PdfFileWriter
import pymupdf
# Importing tkinter to make gui in python 
from tkinter import *
import fitz

# Importing tkPDFViewer to place pdf file in gui. 
# In tkPDFViewer library there is 
# a tkPDFViewer module, imported as pdf 
from tkPDFViewer import tkPDFViewer as pdf 

#-----------------------------------------------------------  
# Initializing tk 
root = Tk() 
  
# Set the width and height of our root window. 
root.geometry("1050x950") 

# giving title for the window
root.title("PDF Viewer")

#-----------------------------------------------------------  
# creating object of ShowPdf from tkPDFViewer. 
v1 = pdf.ShowPdf() 
  
# Adding pdf location and width and height. 
v2 = v1.pdf_view(root, pdf_location = r"samplepdf01.pdf", width = 100, height = 50) 
  
# Placing Pdf in the gui. 
# the buttons and the functions must be above mainloop, otherwise, they won't be displayed
v2.pack() 
root.mainloop() 