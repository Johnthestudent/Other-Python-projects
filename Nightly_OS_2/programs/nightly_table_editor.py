from tkinter import *
import shutil
import sys
import os
import cv2
from tkinter import ttk
import pandas as pd

#-----------------------------------------------------------
# Creating the window for loader
# Calling the TK
table_editor = Tk()

# creating a string of 215 space characters
space=(" ")*215

# It retrieves the screen width of the user's display
screen_width = table_editor.winfo_screenwidth()
 
# It retrieves the screen height of the user's display
screen_height = table_editor.winfo_screenheight()

#Using an f-string to construct the window size in the 
#format width x height
table_editor.geometry(f"{screen_width}x{screen_height}")
#setting the title for the window
table_editor.title(f"{space}Nightly's Table Editor")
table_editor.configure(bg='#202020')

#-----------------------------------------------------------
#experimental
"""
table = ttk.Treeview(table_editor, columns= ('a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i'), show='headings', height=10, selectmode='browse')
table.heading('a', text='a')
table.heading('b', text='b')
table.heading('c', text='c')
table.heading('d', text='d')
table.heading('e', text='e')
table.heading('f', text='f')
table.heading('g', text='g')
table.heading('h', text='h')
table.heading('i', text='i')

table.pack()

for i in range(10):
    emptydata = ('','','','','','','','','')
    table.insert(parent = '', index = 0, values = emptydata)
    
table.bind('<<TreeviewSelect>>', lambda event: print(table.selection()))
"""
"""
another experimental
height = 30
width = 15
for i in range(height): #Rows
    for j in range(width): #Columns
        b = Entry(table_editor, text="")
        b.grid(row=i, column=j)
"""

#-----------------------------------------------------------
#editable table
for i in range(10):
    for j in range(10):
        text = Text(table_editor, width=10, height=1, font=('Times-New-Roman',20), bg = "#FFFFFF") 
        text.grid(row=i,column=j)

#-----------------------------------------------------------
#static data having table for the functions sum, min, max, avg
data = [[10, 18, 11], [13, 15, 8], [9, 20, 3]]

#df = pd.DataFrame(data)

#0 means column based, 1 means row based
#print(df.sum(1)) 

#-----------------------------------------------------------
#variables for label text
data01 = StringVar()
data01.set(data[0][0])
data02 = StringVar()
data02.set(data[0][1])
data03 = StringVar()
data03.set(data[0][2])
data04 = StringVar()
data04.set(data[1][0])
data05 = StringVar()
data05.set(data[1][1])
data06 = StringVar()
data06.set(data[1][2])
data07 = StringVar()
data07.set(data[2][0])
data08 = StringVar()
data08.set(data[2][1])
data09 = StringVar()
data09.set(data[2][2])

#-----------------------------------------------------------
#variables for the function calculations
sumrow01 = StringVar()
sumrow02 = StringVar()
sumrow03 = StringVar()
sumcolumn01 = StringVar()
sumcolumn02 = StringVar()
sumcolumn03 = StringVar()
minrow01 = StringVar()
minrow02 = StringVar()
minrow03 = StringVar()
mincolumn01 = StringVar()
mincolumn02 = StringVar()
mincolumn03 = StringVar()
maxrow01 = StringVar()
maxrow02 = StringVar()
maxrow03 = StringVar()
maxcolumn01 = StringVar()
maxcolumn02 = StringVar()
maxcolumn03 = StringVar()
avgrow01 = StringVar()
avgrow02 = StringVar()
avgrow03 = StringVar()
avgcolumn01 = StringVar()
avgcolumn02 = StringVar()
avgcolumn03 = StringVar()

#-----------------------------------------------------------
#functions for showing cell function results
#sum by row
def show_sum_rows():
    sumrow01.set(str(data[0][0] + data[0][1] + data[0][2]))
    sumrow02.set(str(data[1][0] + data[1][1] + data[1][2]))
    sumrow03.set(str(data[2][0] + data[2][1] + data[2][2]))
    global label_cellsum01 
    global label_cellsum02
    global label_cellsum03
    label_cellsum01.config(textvariable=sumrow01)
    label_cellsum02.config(textvariable=sumrow02)
    label_cellsum03.config(textvariable=sumrow03)

#sum by column
def show_sum_columns():
    sumcolumn01.set(str(data[0][0] + data[1][0] + data[2][0]))
    sumcolumn02.set(str(data[0][1] + data[1][1] + data[2][1]))
    sumcolumn03.set(str(data[0][2] + data[1][2] + data[2][2]))
    global label_cellsumcolumn01 
    global label_cellsumcolumn02
    global label_cellsumcolumn03
    label_cellsumcolumn01.config(textvariable=sumcolumn01)
    label_cellsumcolumn02.config(textvariable=sumcolumn02)
    label_cellsumcolumn03.config(textvariable=sumcolumn03)

#min by row
def show_min_rows():
    row_elements01 = [data[0][0], data[0][1], data[0][2]]
    row_elements02 = [data[1][0], data[1][1], data[1][2]]
    row_elements03 = [data[2][0], data[2][1], data[2][2]]
    min_of_row01 = min(row_elements01)
    min_of_row02 = min(row_elements02)
    min_of_row03 = min(row_elements03)
    minrow01.set(min_of_row01)
    minrow02.set(min_of_row02)
    minrow03.set(min_of_row03)
    global label_cellminrow01
    global label_cellminrow02
    global label_cellminrow03
    label_cellminrow01.config(textvariable=minrow01)
    label_cellminrow02.config(textvariable=minrow02)
    label_cellminrow03.config(textvariable=minrow03)

#min by column
def show_min_columns():
    column_elements01 = [data[0][0], data[1][0], data[2][0]]
    column_elements02 = [data[0][1], data[1][1], data[2][1]]
    column_elements03 = [data[0][2], data[1][2], data[2][2]]
    min_of_column01 = min(column_elements01)
    min_of_column02 = min(column_elements02)
    min_of_column03 = min(column_elements03)
    mincolumn01.set(min_of_column01)
    mincolumn02.set(min_of_column02)
    mincolumn03.set(min_of_column03)
    global label_cellmincolumn01
    global label_cellmincolumn02
    global label_cellmincolumn03
    label_cellmincolumn01.config(textvariable=mincolumn01)
    label_cellmincolumn02.config(textvariable=mincolumn02)
    label_cellmincolumn03.config(textvariable=mincolumn03)

#max by row
def show_max_rows():
    row_elements01 = [data[0][0], data[0][1], data[0][2]]
    row_elements02 = [data[1][0], data[1][1], data[1][2]]
    row_elements03 = [data[2][0], data[2][1], data[2][2]]
    max_of_row01 = max(row_elements01)
    max_of_row02 = max(row_elements02)
    max_of_row03 = max(row_elements03)
    maxrow01.set(max_of_row01)
    maxrow02.set(max_of_row02)
    maxrow03.set(max_of_row03)
    global label_cellmaxrow01
    global label_cellmaxrow02
    global label_cellmaxrow03
    label_cellmaxrow01.config(textvariable=maxrow01)
    label_cellmaxrow02.config(textvariable=maxrow02)
    label_cellmaxrow03.config(textvariable=maxrow03)

#max by column
def show_max_columns():
    column_elements01 = [data[0][0], data[1][0], data[2][0]]
    column_elements02 = [data[0][1], data[1][1], data[2][1]]
    column_elements03 = [data[0][2], data[1][2], data[2][2]]
    max_of_column01 = max(column_elements01)
    max_of_column02 = max(column_elements02)
    max_of_column03 = max(column_elements03)
    maxcolumn01.set(max_of_column01)
    maxcolumn02.set(max_of_column02)
    maxcolumn03.set(max_of_column03)
    global label_cellmaxcolumn01
    global label_cellmaxcolumn02
    global label_cellmaxcolumn03
    label_cellmaxcolumn01.config(textvariable=maxcolumn01)
    label_cellmaxcolumn02.config(textvariable=maxcolumn02)
    label_cellmaxcolumn03.config(textvariable=maxcolumn03)

#avg by row
def show_avg_rows():
    sumit01 = data[0][0] + data[0][1] + data[0][2]
    divideit01 = sumit01 / 3
    avgrow01.set(str(round(divideit01, 1)))
    sumit02 = data[1][0] + data[1][1] + data[1][2]
    divideit02 = sumit02 / 3
    avgrow02.set(str(round(divideit02, 1)))
    sumit03 = data[2][0] + data[2][1] + data[2][2]
    divideit03 = sumit03 / 3
    avgrow03.set(str(round(divideit03, 1)))
    global label_cellavgrow01
    global label_cellavgrow02
    global label_cellavgrow03
    label_cellavgrow01.config(textvariable=avgrow01)
    label_cellavgrow02.config(textvariable=avgrow02)
    label_cellavgrow03.config(textvariable=avgrow03)

#avg by column
def show_avg_columns():
    sumit01 = data[0][0] + data[1][0] + data[2][0]
    divideit01 = sumit01 / 3
    avgcolumn01.set(str(round(divideit01, 1)))
    sumit02 = data[0][1] + data[1][1] + data[2][1]
    divideit02 = sumit02 / 3
    avgcolumn02.set(str(round(divideit02, 1)))
    sumit03 = data[0][2] + data[1][2] + data[2][2]
    divideit03 = sumit03 / 3
    avgcolumn03.set(str(round(divideit03, 1)))
    global label_cellavgrow01
    global label_cellavgrow02
    global label_cellavgrow03
    label_cellavgcolumn01.config(textvariable=avgcolumn01)
    label_cellavgcolumn02.config(textvariable=avgcolumn02)
    label_cellavgcolumn03.config(textvariable=avgcolumn03)

#index of
def index_of_cell():
    #cell_to_search = data[0][1]
    #print("[0][1]")
    global label_index_of
    label_index_of.config(text="[0][1]")

#-----------------------------------------------------------
#labels for the static cells
label_cell01 = Label(table_editor, textvariable=data01, width=5, height=1, font=('Times-New-Roman',20))
label_cell01.place(relx=0.5, rely=0.5, anchor = CENTER)
label_cell02 = Label(table_editor, textvariable=data02, width=5, height=1, font=('Times-New-Roman',20))
label_cell02.place(relx=0.546, rely=0.5, anchor = CENTER)
label_cell03 = Label(table_editor, textvariable=data03, width=5, height=1, font=('Times-New-Roman',20))
label_cell03.place(relx=0.5915, rely=0.5, anchor = CENTER)
label_cell04 = Label(table_editor, textvariable=data04, width=5, height=1, font=('Times-New-Roman',20))
label_cell04.place(relx=0.5, rely=0.54, anchor = CENTER)
label_cell05 = Label(table_editor, textvariable=data05, width=5, height=1, font=('Times-New-Roman',20))
label_cell05.place(relx=0.546, rely=0.54, anchor = CENTER)
label_cell06 = Label(table_editor, textvariable=data06, width=5, height=1, font=('Times-New-Roman',20))
label_cell06.place(relx=0.5915, rely=0.54, anchor = CENTER)
label_cell07 = Label(table_editor, textvariable=data07, width=5, height=1, font=('Times-New-Roman',20))
label_cell07.place(relx=0.5, rely=0.579, anchor = CENTER)
label_cell08 = Label(table_editor, textvariable=data08, width=5, height=1, font=('Times-New-Roman',20))
label_cell08.place(relx=0.546, rely=0.579, anchor = CENTER)
label_cell09 = Label(table_editor, textvariable=data09, width=5, height=1, font=('Times-New-Roman',20))
label_cell09.place(relx=0.5915, rely=0.579, anchor = CENTER)

#-----------------------------------------------------------
#labels for the function result cells
#sum based on row
label_cellsumrow = Label(table_editor, text="SUM", width=5, height=1, font=('Times-New-Roman',20))
label_cellsumrow.place(relx=0.638, rely=0.46, anchor = CENTER)
label_cellsum01 = Label(table_editor, textvariable="", width=5, height=1, font=('Times-New-Roman',20))
label_cellsum01.place(relx=0.638, rely=0.5, anchor = CENTER)
label_cellsum02 = Label(table_editor, textvariable="", width=5, height=1, font=('Times-New-Roman',20))
label_cellsum02.place(relx=0.638, rely=0.54, anchor = CENTER)
label_cellsum03 = Label(table_editor, textvariable="", width=5, height=1, font=('Times-New-Roman',20))
label_cellsum03.place(relx=0.638, rely=0.579, anchor = CENTER)

#row based sum shower button
btn_Show_SUM_ROW = Button(table_editor, text='Show SUM ROW', width=15, command=show_sum_rows, bg="#1f242d")
btn_Show_SUM_ROW.configure(font=('Times-New-Roman',20,'bold'),foreground='white')
btn_Show_SUM_ROW.place(relx=0.3, rely=0.5, anchor = CENTER)  #center anchor is needed, alongside with the relative x and y values

#-----------------------------------------------------------
#sum based on column
label_cellsumcolumn = Label(table_editor, text="SUM", width=5, height=1, font=('Times-New-Roman',20))
label_cellsumcolumn.place(relx=0.453, rely=0.62, anchor = CENTER)
label_cellsumcolumn01 = Label(table_editor, textvariable=sumcolumn01, width=5, height=1, font=('Times-New-Roman',20))
label_cellsumcolumn01.place(relx=0.5, rely=0.62, anchor = CENTER)
label_cellsumcolumn02 = Label(table_editor, textvariable=sumcolumn02, width=5, height=1, font=('Times-New-Roman',20))
label_cellsumcolumn02.place(relx=0.546, rely=0.62, anchor = CENTER)
label_cellsumcolumn03 = Label(table_editor, textvariable=sumcolumn03, width=5, height=1, font=('Times-New-Roman',20))
label_cellsumcolumn03.place(relx=0.5915, rely=0.62, anchor = CENTER)

#column based sum shower button
btn_Show_SUM_COLUMN = Button(table_editor, text='Show SUM COL', width=15, command=show_sum_columns, bg="#1f242d")
btn_Show_SUM_COLUMN.configure(font=('Times-New-Roman',20,'bold'),foreground='white')
btn_Show_SUM_COLUMN.place(relx=0.3, rely=0.58, anchor = CENTER)  #center anchor is needed, alongside with the relative x and y values

#-----------------------------------------------------------
#labels for the function result cells
#min based on row
label_cellminrow = Label(table_editor, text="MIN", width=5, height=1, font=('Times-New-Roman',20))
label_cellminrow.place(relx=0.684, rely=0.46, anchor = CENTER)
label_cellminrow01 = Label(table_editor, textvariable="", width=5, height=1, font=('Times-New-Roman',20))
label_cellminrow01.place(relx=0.684, rely=0.5, anchor = CENTER)
label_cellminrow02 = Label(table_editor, textvariable="", width=5, height=1, font=('Times-New-Roman',20))
label_cellminrow02.place(relx=0.684, rely=0.54, anchor = CENTER)
label_cellminrow03 = Label(table_editor, textvariable="", width=5, height=1, font=('Times-New-Roman',20))
label_cellminrow03.place(relx=0.684, rely=0.579, anchor = CENTER)

#row based min shower button
btn_Show_MIN_ROW = Button(table_editor, text='Show MIN ROW', width=15, command=show_min_rows, bg="#1f242d")
btn_Show_MIN_ROW.configure(font=('Times-New-Roman',20,'bold'),foreground='white')
btn_Show_MIN_ROW.place(relx=0.1, rely=0.66, anchor = CENTER)  #center anchor is needed, alongside with the relative x and y values

#-----------------------------------------------------------
#min based on column
label_cellmincolumn = Label(table_editor, text="MIN", width=5, height=1, font=('Times-New-Roman',20))
label_cellmincolumn.place(relx=0.453, rely=0.66, anchor = CENTER)
label_cellmincolumn01 = Label(table_editor, textvariable="", width=5, height=1, font=('Times-New-Roman',20))
label_cellmincolumn01.place(relx=0.5, rely=0.66, anchor = CENTER)
label_cellmincolumn02 = Label(table_editor, textvariable="", width=5, height=1, font=('Times-New-Roman',20))
label_cellmincolumn02.place(relx=0.546, rely=0.66, anchor = CENTER)
label_cellmincolumn03 = Label(table_editor, textvariable="", width=5, height=1, font=('Times-New-Roman',20))
label_cellmincolumn03.place(relx=0.5915, rely=0.66, anchor = CENTER)

#column based min shower button
btn_Show_MIN_COLUMN = Button(table_editor, text='Show MIN COL', width=15, command=show_min_columns, bg="#1f242d")
btn_Show_MIN_COLUMN.configure(font=('Times-New-Roman',20,'bold'),foreground='white')
btn_Show_MIN_COLUMN.place(relx=0.3, rely=0.66, anchor = CENTER)  #center anchor is needed, alongside with the relative x and y values

#-----------------------------------------------------------
#labels for the function result cells
#max based on row
label_cellmaxrow = Label(table_editor, text="MAX", width=5, height=1, font=('Times-New-Roman',20))
label_cellmaxrow.place(relx=0.7295, rely=0.46, anchor = CENTER)
label_cellmaxrow01 = Label(table_editor, textvariable="", width=5, height=1, font=('Times-New-Roman',20))
label_cellmaxrow01.place(relx=0.7295, rely=0.5, anchor = CENTER)
label_cellmaxrow02 = Label(table_editor, textvariable="", width=5, height=1, font=('Times-New-Roman',20))
label_cellmaxrow02.place(relx=0.7295, rely=0.54, anchor = CENTER)
label_cellmaxrow03 = Label(table_editor, textvariable="", width=5, height=1, font=('Times-New-Roman',20))
label_cellmaxrow03.place(relx=0.7295, rely=0.579, anchor = CENTER)

#row based max shower button
btn_Show_MAX_ROW = Button(table_editor, text='Show MAX ROW', width=15, command=show_max_rows, bg="#1f242d")
btn_Show_MAX_ROW.configure(font=('Times-New-Roman',20,'bold'),foreground='white')
btn_Show_MAX_ROW.place(relx=0.1, rely=0.74, anchor = CENTER)  #center anchor is needed, alongside with the relative x and y values

#-----------------------------------------------------------
#max based on column
label_cellmaxcolumn = Label(table_editor, text="MAX", width=5, height=1, font=('Times-New-Roman',20))
label_cellmaxcolumn.place(relx=0.453, rely=0.699, anchor = CENTER)
label_cellmaxcolumn01 = Label(table_editor, textvariable="", width=5, height=1, font=('Times-New-Roman',20))
label_cellmaxcolumn01.place(relx=0.5, rely=0.699, anchor = CENTER)
label_cellmaxcolumn02 = Label(table_editor, textvariable="", width=5, height=1, font=('Times-New-Roman',20))
label_cellmaxcolumn02.place(relx=0.546, rely=0.699, anchor = CENTER)
label_cellmaxcolumn03 = Label(table_editor, textvariable="", width=5, height=1, font=('Times-New-Roman',20))
label_cellmaxcolumn03.place(relx=0.5915, rely=0.699, anchor = CENTER)

#column based max shower button
btn_Show_MAX_COLUMN = Button(table_editor, text='Show MAX COL', width=15, command=show_max_columns, bg="#1f242d")
btn_Show_MAX_COLUMN.configure(font=('Times-New-Roman',20,'bold'),foreground='white')
btn_Show_MAX_COLUMN.place(relx=0.3, rely=0.74, anchor = CENTER)  #center anchor is needed, alongside with the relative x and y values

#-----------------------------------------------------------
#labels for the function result cells
#avg based on row
label_cellavgrow = Label(table_editor, text="AVG", width=5, height=1, font=('Times-New-Roman',20))
label_cellavgrow.place(relx=0.7755, rely=0.46, anchor = CENTER)
label_cellavgrow01 = Label(table_editor, textvariable="", width=5, height=1, font=('Times-New-Roman',20))
label_cellavgrow01.place(relx=0.7755, rely=0.5, anchor = CENTER)
label_cellavgrow02 = Label(table_editor, textvariable="", width=5, height=1, font=('Times-New-Roman',20))
label_cellavgrow02.place(relx=0.7755, rely=0.54, anchor = CENTER)
label_cellavgrow03 = Label(table_editor, textvariable="", width=5, height=1, font=('Times-New-Roman',20))
label_cellavgrow03.place(relx=0.7755, rely=0.579, anchor = CENTER)

#row based avg shower button
btn_Show_AVG_ROW = Button(table_editor, text='Show AVG ROW', width=15, command=show_avg_rows, bg="#1f242d")
btn_Show_AVG_ROW.configure(font=('Times-New-Roman',20,'bold'),foreground='white')
btn_Show_AVG_ROW.place(relx=0.1, rely=0.5, anchor = CENTER)  #center anchor is needed, alongside with the relative x and y values

#-----------------------------------------------------------
#avg based on column
label_cellavgcolumn = Label(table_editor, text="AVG", width=5, height=1, font=('Times-New-Roman',20))
label_cellavgcolumn.place(relx=0.453, rely=0.738, anchor = CENTER)
label_cellavgcolumn01 = Label(table_editor, textvariable="", width=5, height=1, font=('Times-New-Roman',20))
label_cellavgcolumn01.place(relx=0.5, rely=0.738, anchor = CENTER)
label_cellavgcolumn02 = Label(table_editor, textvariable="", width=5, height=1, font=('Times-New-Roman',20))
label_cellavgcolumn02.place(relx=0.546, rely=0.738, anchor = CENTER)
label_cellavgcolumn03 = Label(table_editor, textvariable="", width=5, height=1, font=('Times-New-Roman',20))
label_cellavgcolumn03.place(relx=0.5915, rely=0.738, anchor = CENTER)

#column based avg shower button
btn_Show_AVG_COLUMN = Button(table_editor, text='Show AVG COL', width=15, command=show_avg_columns, bg="#1f242d")
btn_Show_AVG_COLUMN.configure(font=('Times-New-Roman',20,'bold'),foreground='white')
btn_Show_AVG_COLUMN.place(relx=0.1, rely=0.58, anchor = CENTER)  #center anchor is needed, alongside with the relative x and y values

#-----------------------------------------------------------
#index of
label_index_of = Label(table_editor, text="", width=5, height=1, font=('Times-New-Roman',20))
label_index_of.place(relx=0.7, rely=0.65, anchor = CENTER)

#index of shower button
btn_Show_INDEX_OF = Button(table_editor, text='Index of 18', width=15, command=index_of_cell, bg="#1f242d")
btn_Show_INDEX_OF.configure(font=('Times-New-Roman',20,'bold'),foreground='white')
btn_Show_INDEX_OF.place(relx=0.7, rely=0.7, anchor = CENTER)  #center anchor is needed, alongside with the relative x and y values

#the window won't get opened without this
table_editor.mainloop()