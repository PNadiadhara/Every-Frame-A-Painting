import os
#
# osascript -e 'tell application "Finder" to set desktop picture to POSIX file "/Users/priteshnadiadhara/Documents/Python/EveryFrameAPainting/Frames/frame0.jpg"' 

# subprocess.call(['osascript'], ['-e'], ['tell application "Finder" to set desktop picture to POSIX file "/Users/priteshnadiadhara/Documents/Python/EveryFrameAPainting/Frames/frame0.jpg"'])

#subprocess.run('ls')

terminlal_output = f"osascript -e 'tell application \"Finder\" to set desktop picture to POSIX file \"/Users/priteshnadiadhara/Documents/Python/EveryFrameAPainting/Frames/frame0.jpg\"'"

os.system(terminlal_output)