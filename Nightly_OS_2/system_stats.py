from tkinter import *
import platform
import webbrowser

#-----------------------------------------------------------
# Creating the window for loader
# Calling the TK
system_things = Tk()

# creating a string of 215 space characters
space=(" ")*215

# It retrieves the screen width of the user's display
screen_width = 800
 
# It retrieves the screen height of the user's display
screen_height = 500

#Using an f-string to construct the window size in the 
#format width x height
system_things.geometry(f"{screen_width}x{screen_height}")
#setting the title for the window
system_things.title(f"{space}System things")
system_things.configure(bg='#202020')

#-----------------------------------------------------------
#system stats
#system name
my_system = platform.uname() 
system_name = StringVar()
system_name.set("Operating system: " + my_system.system)    #stringvar cannot be concatenated to a string, but the string concatenation can be done with the set method

#system release
system_release = StringVar()
system_release.set("Release: " + my_system.release)

#system version
system_version = StringVar()
system_version.set("Version: " + my_system.version)

#system node name
system_node = StringVar()
system_node.set("Node name: " + my_system.node)

#system machine
system_machine = StringVar()
system_machine.set("Machine: " + my_system.machine)

#system processor
system_processor = StringVar()
system_processor.set("Processor: \n" + my_system.processor)

#-----------------------------------------------------------
#setting the labels
system_name_label = Label(system_things, textvariable=system_name, bg="#202020", fg="#FFFFFF", font =("Times-New-Roman", 25))
system_name_label.pack()
system_release_label = Label(system_things, textvariable=system_release, bg="#202020", fg="#FFFFFF", font =("Times-New-Roman", 25))
system_release_label.pack()
system_version_label = Label(system_things, textvariable=system_version, bg="#202020", fg="#FFFFFF", font =("Times-New-Roman", 25))
system_version_label.pack()
system_node_label = Label(system_things, textvariable=system_node, bg="#202020", fg="#FFFFFF", font =("Times-New-Roman", 25))
system_node_label.pack()
system_machine_label = Label(system_things, textvariable=system_machine, bg="#202020", fg="#FFFFFF", font =("Times-New-Roman", 25))
system_machine_label.pack()
system_processor_label = Label(system_things, textvariable=system_processor, bg="#202020", fg="#FFFFFF", font =("Times-New-Roman", 25))
system_processor_label.pack()

#-----------------------------------------------------------
#anchor link
def link_to_open():
    webbrowser.open_new(r"https://johnthestudent.github.io/Nightly_OS/")

#link opener button
btnLink= Button(system_things, text='Nightly Prototype', width=15, command=link_to_open, bg="#1f242d")
btnLink.configure(font=('Times-New-Roman',25,'bold'),foreground='white')
btnLink.place(relx=0.5, rely=0.85, anchor = CENTER)  #center anchor is needed, alongside with the relative x and y values

#the window won't get opened without this
system_things.mainloop()

#Experimental  
#my_system = platform.uname() 
#print(f"System: {my_system.system}")
#print(f"Node Name: {my_system.node}")
#print(f"Release: {my_system.release}")
#print(f"Version: {my_system.version}")
#print(f"Machine: {my_system.machine}")
#print(f"Processor: {my_system.processor}")