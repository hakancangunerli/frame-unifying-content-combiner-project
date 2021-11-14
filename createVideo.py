import os, sys, subprocess
from tkinter import Tk, filedialog as fd
import cv2
import ffmpeg


def createVideo(distortedFramesPath,resultDirPath, videoName,fps, videoSize, nbFrames):
    print('Creating video...')
    img_array = [cv2.imread(os.path.join(distortedFramesPath, elem)) for elem in sorted(os.listdir(distortedFramesPath))]
    distortedVideoPath = os.path.join(resultDirPath, 'distorted_'+videoName)
    out = cv2.VideoWriter(distortedVideoPath, cv2.VideoWriter_fourcc(*'mp4v'), fps, videoSize)

    for i in range(len(img_array)):
        print(f'{i}/{nbFrames}', end="\r")
        out.write(img_array[i])
    out.release()