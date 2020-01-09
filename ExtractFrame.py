import cv2
import os

vidcap = cv2.VideoCapture('Jellyfish.mp4')
path = '/Users/priteshnadiadhara/Documents/Python/EveryFrameAPainting/Frames'




# info @ 1080p video quality each image is ~ 300kb
# should write on 12th frame at 24 fps for optimal inbetweens in most cases
def extract_frames (mp4_file, frames_folder_path):
    
    success,image = mp4_file.read()
    count = 0
    success = True
    frame_count = 0
    
    # set to only have 1s of images to reduce file size 
    # currently includes frame 0, must be changed
    while success:
        cv2.imwrite(os.path.join(frames_folder_path, "frame%d.jpg" % count), image)   # save frame as JPEG file to given path
        frame_count += 1
        count += 1
        success,image = vidcap.read()
        print ('Read a new frame: ', success, frame_count)
        
        if frame_count == 11:
            success = False
    
        


extract_frames(vidcap,path)