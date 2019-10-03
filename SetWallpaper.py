import os

# osascript -e 'tell application "Finder" to set desktop picture to POSIX file "/Users/priteshnadiadhara/Documents/Python/EveryFrameAPainting/Frames/frame0.jpg"' 

path_to_image_file = '/Users/priteshnadiadhara/Documents/Python/EveryFrameAPainting/Frames/frame0.jpg'

# terminal_output = f"osascript -e 'tell application \"Finder\" to set desktop picture to POSIX file \"{path_to_image_file}\"'"
# os.system(terminal_output) 

def set_wallpaper(filePath):
    terminal_output = f"osascript -e 'tell application \"Finder\" to set desktop picture to POSIX file \"{filePath}\"'"
    os.system(terminal_output) 


set_wallpaper(path_to_image_file)