import os, sys, subprocess
import cv2
import ffmpeg
from addingSound import addingSound
from distortFrames import distortFrames
from createVideo import createVideo
from yt import yt




DISTORT_PERCENTAGE = 60 
SOUND_FILTER_FREQUENCY = 10 
SOUND_FILTER_MODULATION_DEPTH = 1 



path = os.path.abspath(os.path.join(sys.argv[0], os.pardir))
resultDirPath = os.path.join(path, 'result')


videoPath = './video.mp4'



videoName = os.path.basename(videoPath)
framesPath = os.path.join(resultDirPath, 'frames')
distortedFramesPath = os.path.join(resultDirPath, 'distortedFrames')

# define video variables
capture = cv2.VideoCapture(videoPath)
fps = capture.get(cv2.CAP_PROP_FPS)
nbFrames = int(capture.get(cv2.CAP_PROP_FRAME_COUNT))
videoSize = (
    int(capture.get(cv2.CAP_PROP_FRAME_WIDTH)),
    int(capture.get(cv2.CAP_PROP_FRAME_HEIGHT))
)


# create output directories
os.makedirs(resultDirPath, exist_ok=True)
os.makedirs(framesPath, exist_ok=True)
os.makedirs(distortedFramesPath, exist_ok=True)
for elem in os.listdir(framesPath):
    os.remove( os.path.join(framesPath, elem) )
for elem in os.listdir(distortedFramesPath):
    os.remove( os.path.join(distortedFramesPath, elem) )


# convert video to frames
print('Converting video into frames...')
frameNr = 0
while True:
    print(frameNr, 'to ', nbFrames, end="\r")
    success, frame = capture.read()

    if not success:
        break

    # naming the file with an appropriate number of leading zeros
    filename = f'frame_{str(frameNr).zfill(len(str(nbFrames)))}.jpg'
    cv2.imwrite(os.path.join(framesPath, filename), frame)
    frameNr += 1
capture.release()


distortFrames(framesPath, distortedFramesPath, DISTORT_PERCENTAGE, videoSize,nbFrames)
distortedVideoPath = os.path.join(resultDirPath, 'distorted_'+videoName) 
createVideo(distortedFramesPath,resultDirPath, videoName,fps, videoSize, nbFrames)
addingSound(distortedVideoPath, videoPath, SOUND_FILTER_FREQUENCY, SOUND_FILTER_MODULATION_DEPTH, resultDirPath, videoName)
os.remove(distortedVideoPath)

print('Completed!!!')
