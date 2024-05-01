# import cv2
# import numpy as np
#
# img = cv2.imread('../../data/lena.jpg')
# face = np.ones((150, 150, 3))
#
# cv2.imshow('img', img)
#
# # 显示ROI区域（ROI: 感兴趣区域）
# face = img[100:250, 100:250]
# cv2.imshow('face', face)
#
# cv2.waitKey()
# cv2.destroyAllWindows()

import cv2
import numpy as np

lena = cv2.imread('../../data/lena.jpg')
lily = cv2.imread('../../data/lily_square.png')
face = np.zeros((150, 150, 3), dtype='uint8')
# print(lena,lily,face)

# 显示ROI区域（ROI: 感兴趣区域）
face = lena[170:320, 150:300]  # 选取150*150大小

lily[70:220, 30:180] = face# 接入lily图

cv2.imshow('face', face)
cv2.imshow('lily', lily)

# lena[100:250, 100:250] = 0
cv2.imshow('img', lena)

cv2.waitKey()
cv2.destroyAllWindows()
