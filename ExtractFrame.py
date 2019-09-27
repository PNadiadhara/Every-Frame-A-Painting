import cv2
import os

vidcap = cv2.VideoCapture('Jellyfish.mp4')
path = '/Users/priteshnadiadhara/Documents/Python/EveryFrameAPainting/Frames'




def extract_frames (mp4_file, frames_folder_path):
    
    success,image = mp4_file.read()
    count = 0
    success = True
    
    while success and count < 24 :
        cv2.imwrite(os.path.join(frames_folder_path, "frame%d.jpg" % count), image)   # save frame as JPEG file to given path
        success,image = vidcap.read()
        print ('Read a new frame: ', success)
        count += 1


extract_frames(vidcap,path)