import SetWallpaper
import ExtractFrame
import os
import tkinter as tk
from tkinter import filedialog, test

# root is used for "frame Work" i.e. html body
root = tk.Tk()



canvas = tk.Canvas(root, height=700, width=700, bg="#263D42")
# canvas.pack() attaches to root to allow the custom settings i.e. height, width, color
canvas.pack()

#root.mainloop used to open gui
# important note, have root.mainloop last to allow for canvas pack updates to work
root.mainloop()





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