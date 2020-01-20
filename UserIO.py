import SetWallpaper
import ExtractFrame
import os
import tkinter as tk
from tkinter import filedialog, test

# root is used for "frame Work" i.e. html body
root = tk.Tk()
filePath = []

#check for save file
if os.path.isfile('save.txt'):
    with open('save.txt', 'r') as f:
        tempFile = f.read
        print(tempFile)


def addMP4():
    for widget in frame.winfo_children() :
        widget.destroy()

    filename = filedialog.askopenfilename(initialdir="/", title= "Select MP4", 
    filetypes=(("MP4s", "*.mp4"), ("all files", "*.*")))
    filePath.append(filename)
    print(filename)
    for file in filePath:
        label = tk.Label(frame, text = file, bg= "gray")
        label.pack()




canvas = tk.Canvas(root, height=700, width=700, bg="#263D42")
# canvas.pack() attaches to root to allow the custom settings i.e. height, width, color
canvas.pack()

frame = tk.Frame(root, bg="white")
# relx and rel y "distance from origin" set at top left
frame.place(relwidth = 0.8, relheight= 0.8, relx=0.1, rely=0.1)
#root.mainloop used to open gui
# important note, have root.mainloop last to allow for canvas pack updates to work

# button note: highlightbackground is used to change button bg color on mac, on pc it's bg

selectMP4 = tk.Button(root, text = "Open MP4", padx = 10, pady = 5, fg="black", highlightbackground="#263D42",command = addMP4).pack()
#selectMP4.pack()

runApp = tk.Button(root, text = "runApp", padx = 10, pady = 5, fg="white", highlightbackground="#263D42")
runApp.pack()

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