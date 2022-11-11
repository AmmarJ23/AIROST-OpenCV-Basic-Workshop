import cv2 as cv
import numpy as np

img_var = cv.imread('stopSign.jpg')
cv.imshow('Stop sign', img_var)

#cv.imwrite('stopSignPNG.png', img_var)
imgResized = cv.resize(img_var, [800,800], cv.INTER_CUBIC)

cv.imshow('resized', imgResized)

#croppedIMG = img_var[40:350, 100:400]
#cv.imshow('cropped', croppedIMG)

imgDimensions = (img_var.shape[1], img_var.shape[0])#1=width, 0=height
# M = np.float32([[1,0,20],[0,1,30]])
# dst = cv.warpAffine(img_var, M, imgDimensions)

#cv.imshow('Translated', dst)

M = cv.getRotationMatrix2D((img_var.shape[1]//2, img_var.shape[0]//2),45,1)
dst = cv.warpAffine(img_var, M, imgDimensions)
cv.imshow('Rotation', dst)


cv.waitKey(0)