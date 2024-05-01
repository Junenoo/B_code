import cv2
import numpy as np

img01 = cv2.imread('roberts_CV_8U.png')
img02 = cv2.imread('roberts_CV_16U.png')
img03 = cv2.imread('roberts_CV_32F.png')
img04 = cv2.imread('roberts_CV_64F.png')
cv2.imshow('roberts_CV_8U', img01)
cv2.imshow('roberts_CV_16U', img02)
cv2.imshow('roberts_CV_32F', img03)
cv2.imshow('roberts_CV_64F', img04)
cv2.waitKey()
cv2.destroyAllWindows()