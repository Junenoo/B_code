'''
图像的镜像（翻转）
'''

import cv2

img = cv2.imread('../../../data/Linus.png')
cv2.imshow('original', img)

# 水平镜像
res0 = cv2.flip(img, 0)
cv2.imshow('Horizontal', res0)
# 垂直镜像
res1 = cv2.flip(img, 1)
cv2.imshow('Vertical', res1)
# 水平垂直镜像
res2 = cv2.flip(img, -1)
cv2.imshow('Horizontal + Vertical', res2)

cv2.waitKey()
cv2.destroyAllWindows()
