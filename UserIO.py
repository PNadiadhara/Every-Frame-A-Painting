import os
import tkinter as tk
from tkinter import filedialog, test
import SetWallpaper
import ExtractFrame
import cv2

# root is used for "frame Work" i.e. html body
root = tk.Tk()
root.title('Every Frame A Painting')
filePath = ""

# TO BE Removed
vidcap = cv2.VideoCapture('Jellyfish.mp4')
path = '/Users/priteshnadiadhara/Documents/Python/EveryFrameAPainting/Frames'

height = 700
width = 700

# Colors from https://coolors.co/0b132b-1c2541-3a506b-5bc0be-6fffe9

MaastrichtBlue = "#0B132B"
YankeesBLue = "#1C2541"
Independence = "#3A506B"
SeaSerpent = "#5BC0BE"
AquaMarine = "#6FFFE9"



borderEffects = {
    "flat": tk.FLAT,
    "sunken": tk.SUNKEN,
    "raised": tk.RAISED,
    "groove": tk.GROOVE,
    "ridge": tk.RIDGE,
}

#check for save file
if os.path.isfile('save.txt'):
    with open('save.txt', 'r') as f:
        tempFile = f.read
        print(tempFile)


def addMP4():
    for widget in frame.winfo_children() :
        widget.destroy()

    filename = filedialog.askopenfilename(initialdir="/", title="Select MP4", 
    filetypes=(("MP4s", "*.mp4"), ("all files", "*.*")))
    filePath = filename
    print("this is the file path")
    print(filename)
    label = tk.Label(frame, text= filename, bg= AquaMarine)
    label.pack()


# note on .pack, .grid, and .frame can be found here https://www.tutorialspoint.com/python/python_gui_programming.htm

canvas = tk.Canvas(root, height=height, width=width, bg=MaastrichtBlue)
# canvas.pack() attaches to root to allow the custom settings i.e. height, width, color
canvas.pack()

frame = tk.Frame(canvas, bg=YankeesBLue, relief = "ridge")
# relx and rel y "distance from origin" set at top left
frame.place(relwidth = 0.8, relheight= 0.8, relx=0.1, rely=0.1)


# button note: highlightbackground is used to change button bg color on mac, on pc it's bg
#buttonFrame = tk.Frame(frame, bg=YankeesBLue, relief="ridge")
#buttonFrame.place(relwidth=0.8, relheight= 0.2, relx=0.1, rely=0.1)

selectMP4 = tk.Button(root, text = "Open MP4", padx = 10, pady = 5, fg="black", highlightbackground=SeaSerpent, relief = "sunken",command= addMP4)
selectMP4.pack()

runApp = tk.Button(root, text = "runApp", padx = 10, pady = 5, fg="black", highlightbackground=SeaSerpent, relief = "sunken",command= ExtractFrame.extract_frames(vidcap,path))
runApp.pack()

#root.mainloop used to open gui
# important note, have root.mainloop last to allow for canvas pack updates to work
root.mainloop()

# create savefile
with open('save.txt', "w") as f:
    for file in filePath:    
            f.write(file + ',')
        
        





# ask user for information regarding file path of file that needs frames extracted
# number of seconds that will be extraced from clip (note file get large quickly, make sure to restrict total number of frames made)

# create method to check if path is valid
# option to create folder to save extracted frames to if needed
# path =  os.getcwdb()


# user_selected_filepath_MP4 = input("Please provide the file path to your selected .MP4 file: ")
# user_selected_filepath_frames_folder = input("Please provide the file path to folder where frames will be saved: ")

# print( "Current path is : " + str(path))
# print(user_selected_filepath_MP4)
# print(user_selected_filepath_frames_folder)



# try: 
#     os.mkdir(user_selected_filepath_frames_folder)
# except OSError:
#     print("Creation of the directory %s has failed" % path)
# else:
#     print("Successfully created new directory")