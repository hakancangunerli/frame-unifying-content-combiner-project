import os, sys, subprocess
from tkinter import Tk, filedialog as fd
import cv2
import ffmpeg



def addingSound(distortedVideoPath, videoPath, SOUND_FILTER_FREQUENCY, SOUND_FILTER_MODULATION_DEPTH, resultDirPath, videoName):
    print("Adding distorted sound...")
    video = ffmpeg.input(distortedVideoPath).video
    audio = ffmpeg.input(videoPath).audio.filter(
    "vibrato",
    f=SOUND_FILTER_FREQUENCY,
    d=SOUND_FILTER_MODULATION_DEPTH
    )
    resultVideoPath = os.path.join(resultDirPath, 'result_'+videoName)
    (
    ffmpeg
    .concat(video, audio, v=1, a=1) 
    .output(resultVideoPath)
    .run()
    )
    