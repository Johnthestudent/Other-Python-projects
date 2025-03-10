from tkinter import *
import os

# Creating the window for loader
# Calling the TK
disk_manager = Tk()

# creating a string of 215 space characters
space=(" ")*215

# It retrieves the screen width of the user's display
screen_width = 600
 
# It retrieves the screen height of the user's display
screen_height = 200

#Using an f-string to construct the window size in the 
#format width x height
disk_manager.geometry(f"{screen_width}x{screen_height}")
#setting the title for the window
disk_manager.title(f"{space}Disk manager")
disk_manager.configure(bg='#202020')

#------------------------------------------------- 
#size counting, the path is a parameter
def size_counter(path):
    # directory name from which to extract files with size
    #path = "\\Nightly OS 2"
    
    # Get list of all files only in the given directory
    fun = lambda x : os.path.isfile(os.path.join(path,x))
    files_list = filter(fun, os.listdir(path))
    
    # Create a list of files in directory along with the size
    size_of_file = [
        (f,os.stat(os.path.join(path, f)).st_size)
        for f in files_list
    ]

    total_size = 0
    # Iterate over list of files along with size and print them one by one.
    for f,s in size_of_file:
        #print("{} : {}MB".format(f, round(s/(1024*1024),3)))
        #print("{}MB".format(round(s/(1024*1024),3)))
        total_size += s

    #formatting the total size to MB
    total_size = total_size/(1024*1024)
    total_size = round(total_size, 2)    
    print(total_size)
    return total_size

#adding the total file size of all folders
#the parameters have to be modified based on the location of the downloaded Nightly OS 2 project
#like "C: (or any other drive)\destination folder\Nightly OS 2" (and obviously the same for the img and programs directories)
final_total_size = (size_counter("\\Nightly OS 2")+
size_counter("\\Nightly OS 2\img")+
size_counter("\\Nightly OS 2\programs"))

#used space
used_space = final_total_size / 500.0

#free space
free_space = 100.0 - used_space

#------------------------------------------------- 
#label for the final_total_size
actual_size = StringVar()
actual_size.set(str(final_total_size) + " MB" + " / " + "500" + " MB") 

label_for_size= Label(disk_manager, textvariable = actual_size)
label_for_size.config(font =("Times-New-Roman", 25), background="#202020", fg="#FFFFFF", justify="left")

label_for_size.pack()

#labels for used free space sizes
actual_used_space = StringVar()
actual_used_space.set(str(used_space) + " % space used")
actual_free_space = StringVar()
actual_free_space.set(str(free_space) + " % space free")  

label_for_actual_used_space= Label(disk_manager, textvariable = actual_used_space)
label_for_actual_used_space.config(font =("Times-New-Roman", 25), background="#202020", fg="#FFFFFF", justify="left")

label_for_actual_free_space= Label(disk_manager, textvariable = actual_free_space)
label_for_actual_free_space.config(font =("Times-New-Roman", 25), background="#202020", fg="#FFFFFF", justify="left")

label_for_actual_used_space.pack()
label_for_actual_free_space.pack()

#the window won't get opened without this
disk_manager.mainloop()