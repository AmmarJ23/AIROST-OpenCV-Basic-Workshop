import cv2 as cv
import numpy as np

capture = cv.VideoCapture(1, cv.CAP_DSHOW)
capture.set(cv.CAP_PROP_FPS, 30)

lowerVal = np.array([20,150,50])
upperVal = np.array([40,255,255])

while True:
    isTrue, frame = capture.read()

    if isTrue:
        cv.imshow('Video', frame)
        frameHSV = cv.cvtColor(frame, cv.COLOR_BGR2HSV)
        cv.imshow('VideoHSV', frameHSV)

        mask = cv.inRange(frameHSV, lowerVal, upperVal)
        cv.imshow('masked_video', mask)

    else:
        break

    if cv.waitKey(20) & 0xFF == ord('q'):
        break