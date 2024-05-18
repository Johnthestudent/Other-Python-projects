from pypdf import PdfReader, PdfWriter
import PyPDF2
from PyPDF2 import PdfFileReader, PdfFileWriter
import pymupdf
# Importing tkinter to make gui in python 
from tkinter import*
import fitz

# Importing tkPDFViewer to place pdf file in gui. 
# In tkPDFViewer library there is 
# an tkPDFViewer module, imported as pdf 
from tkPDFViewer import tkPDFViewer as pdf 
  
# Initializing tk 
root = Tk() 
  
# Set the width and height of our root window. 
root.geometry("1050x950") 

# giving title for the window
root.title("PDF Editor")
  
# creating object of ShowPdf from tkPDFViewer. 
v1 = pdf.ShowPdf() 
  
# Adding pdf location and width and height. 
v2 = v1.pdf_view(root, pdf_location = r"samplepdf01.pdf", width = 100, height = 50) 

# function to rotate the first page of pdf clockwise
# This function rotates the first page of pdf clockwise
# then saves the modification as a new file
# pypdf 2 edition
"""def rotate_right():
	with open('samplepdf01.pdf', 'rb') as file:
		#pdf reader object
		reader = PyPDF2.PdfReader('samplepdf01.pdf') 

		#number of pages
		#print(len(reader.pages))

		#page object
		page = reader.pages[0] 
		page.rotate(90)
		
		#writer object
		
		writer = PyPDF2.PdfWriter()
		writer.add_page(page)
		with open('result.pdf', 'wb') as new_file:
			writer.write(new_file)"""

# function to rotate the first page of pdf clockwise
# This function rotates the first page of pdf clockwise
# then saves the modification as a new file
# pymu edition			
def rotate_right():
	doc = pymupdf.open("samplepdf01.pdf") # open document
	page = doc[0] # get the 1st page of the document
	page.set_rotation(90) # rotate the page
	doc.save("rotated-page-1.pdf")
	
#rotate button
#btnRotateRight stores the Button widget to rotate the image
#Inside the widget,
btnRotateRight = Button(root, text='Rotate (clockwise)', width=20, command=rotate_right, bg="#1f242d")
btnRotateRight.configure(font=('poppins',11,'bold'),foreground='white')
btnRotateRight.place(x=200,y=840)

# function to rotate the first page of pdf counter-clockwise
# This function rotates the first page of pdf counter-clockwise
# then saves the modification as a new file
# pymu edition			
def rotate_left():
	doc = pymupdf.open("samplepdf01.pdf") # open document
	page = doc[0] # get the 1st page of the document
	page.set_rotation(-90) # rotate the page
	doc.save("rotated-page-1.pdf")
		
#rotate button
#btnRotateLeft stores the Button widget to rotate the image
#Inside the widget,
btnRotateLeft = Button(root, text='Rotate (counter-clockwise)', width=25, command=rotate_left, bg="#1f242d")
btnRotateLeft.configure(font=('poppins',11,'bold'),foreground='white')
btnRotateLeft.place(x=400,y=840)

# function to merge two pdf files
# This function merges two pdf files into one
# then saves the modification as a new file
# pymu edition	
def merge_pdf():
	doc_a = pymupdf.open("samplepdf01.pdf") # open the 1st document
	doc_b = pymupdf.open("samplepdf02.pdf") # open the 2nd document

	doc_a.insert_pdf(doc_b) # merge the docs
	doc_a.save("samplepdf03.pdf") # save the merged document with a new filename

#merge button
#btnMerge stores the Button widget to rotate the image
#Inside the widget,
btnMerge = Button(root, text='Merge two pdf-s', width=20, command=merge_pdf, bg="#1f242d")
btnMerge.configure(font=('poppins',11,'bold'),foreground='white')
btnMerge.place(x=650,y=840)

# function to add blank page
# This function adds blank page to the pdf file
# then saves the modification as a new file
# pymu edition	
def blank_page():
	doc = pymupdf.open("samplepdf01.pdf") # some new or existing PDF document
	page = doc.new_page(-1, # insertion point: end of document
						width = 595, # page dimension: A4 portrait
						height = 842)
	doc.save("doc-with-new-blank-page.pdf") # save the document

#blank page button
#btnBlankPage stores the Button widget to rotate the image
#Inside the widget,
btnBlankPage = Button(root, text='Add blank page', width=20, command=blank_page, bg="#1f242d")
btnBlankPage.configure(font=('poppins',11,'bold'),foreground='white')
btnBlankPage.place(x=515,y=885)

# function to split pdf
# This function splits pdf file so that each page will be a new pdf file
# then saves the modification as a new file
# pymu edition	
def split_pdf():
	doc = pymupdf.open("sample03.pdf") # some new or existing PDF document
	print(len(doc))
	if(len(doc) == 1):
		print("can't do it, because the number of pages is less than 2")
	else:
		with open("sample03.pdf", 'rb') as infile:

			reader = PdfReader(infile)
			writer = PdfWriter()
			writer.add_page(reader.get_page(0))
			writer2 = PdfWriter()
			writer2.add_page(reader.get_page(1))
			with open('splitted01.pdf', 'wb') as outfile:
				writer.write(outfile)
			with open('splitted02.pdf', 'wb') as outfile2:
				writer2.write(outfile2)

#split pdf button
#btnSplitPDF stores the Button widget to rotate the image
#Inside the widget,
btnSplitPDF = Button(root, text='Split pdf', width=20, command=split_pdf, bg="#1f242d")
btnSplitPDF.configure(font=('poppins',11,'bold'),foreground='white')
btnSplitPDF.place(x=720,y=885)

# function to delete page
# This function deletes page from the pdf file (only on min 2 pages long pdf files)
# then saves the modification as a new file
# pymu edition	
def delete_page():
	doc = pymupdf.open("samplepdf01.pdf") # open a document
	print(len(doc))
	if(len(doc) == 1):
		print("can't do it, because the number of pages is less than 2")
	else:
		doc.delete_page(1) # delete the last page of the document
		doc.save("test-deleted-page-one.pdf") # save the document

#delete page button
#btnDeletePage stores the Button widget to rotate the image
#Inside the widget,
btnDeletePage = Button(root, text='Delete page', width=20, command=delete_page, bg="#1f242d")
btnDeletePage.configure(font=('poppins',11,'bold'),foreground='white')
btnDeletePage.place(x=310,y=885)

# function to extract text
# This function extracts text from the pdf file
# then saves the modification as a new file
# pymu edition	
def extract_text():
	doc = pymupdf.open("samplepdf01.pdf") # open a document
	out = open("output.txt", "wb") # create a text output
	for page in doc: # iterate the document pages
		text = page.get_text().encode("utf8") # get plain text (is in UTF-8)
		out.write(text) # write text of page
		out.write(bytes((12,))) # write page delimiter (form feed 0x0C)
	out.close()

#extract page button
#btnExtractText stores the Button widget to rotate the image
#Inside the widget,
btnExtractText = Button(root, text='Extract text', width=20, command=extract_text, bg="#1f242d")
btnExtractText.configure(font=('poppins',11,'bold'),foreground='white')
btnExtractText.place(x=110,y=885)
  
# Placing Pdf in the gui. 
# the buttons and the functions must be above mainloop, otherwise, they won't be displayed
v2.pack() 
root.mainloop() 

#experimental
#with open('samplepdf01.pdf', 'rb') as file:
	#pdf reader object
	#reader = PyPDF2.PdfReader('samplepdf01.pdf') 

	#number of pages
	#print(len(reader.pages))

	#page object
	#page = reader.pages[0] 

	#extracting text from page
	#print(page.extract_text())
	
	#extracting image from page
"""
	page = reader.pages[0]
	count = 0

	for image_file_object in page.images:
		with open(str(count) + image_file_object.name, "wb") as fp:
			fp.write(image_file_object.data)
			count += 1"""
	
	#rotate pdf clockwise
	#page.rotate(-90)
	
	#rotate pdf counter-clockwise
	#page.rotate(90)
	
	#merging pdf-samplepdf01
"""
		def pdf_combiner(pdf_list):
		merger = PyPDF2.PdfFileMerger()
		for pdf in pdf_list:
			merger.append(pdf)
		merger.write('super.pdf')"""
	
	#writer object
"""	
	writer = PyPDF2.PdfWriter()
	writer.add_page(page)
	with open('result.pdf', 'wb') as new_file:
		writer.write(new_file)"""
	
	#encrypt
"""
	from PyPDF2 import PdfReader, PdfWriter

	reader = PdfReader("example.pdf")
	writer = PdfWriter()

	# Add all pages to the writer
	for page in reader.pages:
		writer.add_page(page)

	# Add a password to the new PDF
	writer.encrypt("1234")

	# Save the new PDF to a file
	with open("encrypted-pdf.pdf", "wb") as f:
		writer.write(f)"""
	
	#decrypt
"""
	from PyPDF2 import PdfReader, PdfWriter

	reader = PdfReader("encrypted-pdf.pdf")
	writer = PdfWriter()

	if reader.is_encrypted:
		reader.decrypt("1234")

	# Add all pages to the writer
	for page in reader.pages:
		writer.add_page(page)

	# Save the new PDF to a file
	with open("decrypted-pdf.pdf", "wb") as f:
		writer.write(f)
	"""
#split pdf
"""
from PyPDF2 import PdfFileReader, PdfFileWriter

with open("input.pdf", 'rb') as infile:

    reader = PdfFileReader(infile)
    writer = PdfFileWriter()
    writer.addPage(reader.getPage(0))

    with open('output.pdf', 'wb') as outfile:
        writer.write(outfile)
"""