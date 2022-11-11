import cv2 as cv
import numpy as np

image = cv.imread('stopSign.jpg')

cv.line(image, (0,250), (500,250), (255,0,0), 20)
cv.rectangle(image, (0,0), (100,100), (0,255,0), -1)
cv.circle(image, (250, 250), 100, (0,0,255), 3)

cv.imshow('text', image)
cv.waitKey(0)