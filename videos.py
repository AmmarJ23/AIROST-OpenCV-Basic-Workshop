import cv2 as cv
import numpy as np

# capture = cv.VideoCapture('cat.mp4')

# while True:
#     isTrue, frame_var = capture.read()
#     if isTrue:
#         cv.imshow('Video', frame_var)
#     else:
#         break
#     if cv.waitKey(20) & 0xFF==ord('q'):
#         break




outVideo = cv.VideoWriter('cat.avi', cv.VideoWriter_fourcc('M','J','P','G'), 25, (854,480))
capture = cv.VideoCapture('cat.mp4')
while True:
    isTrue, frame_var = capture.read()
    if isTrue:
        outVideo.write(frame_var)
    else:
        break
    if cv.waitKey(20) & 0xFF==ord('q'):
        break
