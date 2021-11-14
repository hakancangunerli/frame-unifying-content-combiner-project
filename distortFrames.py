import os, sys, subprocess
from tkinter import Tk, filedialog as fd
import cv2
import ffmpeg


def distortFrames(framesPath, distortedFramesPath, DISTORT_PERCENTAGE, videoSize,nbFrames):
    print('Distorting frames...')
    for i, elem in enumerate(os.listdir(framesPath), start=1):
        print(f'{i}/{nbFrames}', end="\r")
        curFramePath = os.path.join(framesPath, elem)
        resFramePath = os.path.join(distortedFramesPath, elem)
        cmd = f"magick {curFramePath}\
        -liquid-rescale {100-DISTORT_PERCENTAGE}x{100-DISTORT_PERCENTAGE}%!\
        -resize {videoSize[0]}x{videoSize[1]}\! {resFramePath}"
        exitCode, cmdOutput = subprocess.getstatusoutput(cmd)