import cv2

img03 = cv2.imread('../../data/3.png')
img04 = cv2.imread('../../data/4.png')

cv2.imshow('img03', img03)
cv2.imshow('img04', img04)

sub01 = cv2.subtract(img03, img04)
cv2.imshow('img03 - img04', sub01)

sub02 = cv2.subtract(img04, img03)
cv2.imshow('img04 - img03', sub02)

cv2.waitKey()
cv2.destroyAllWindows()
