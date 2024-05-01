'''
腐蚀:腐蚀操作时取每一个位置的矩形邻域内值的最小值作为该位置的输出灰度值。
    亮的区域面积会变小,比较暗的区域面积增大
'''

import cv2
import numpy as np

img = cv2.imread('../../../data/5.png')
cv2.imshow('img', img)

# 腐蚀
kernel = np.ones((3,3), np.uint8)  # 腐蚀核((h,w))
kernel2 = np.array(((0,1,0),(1,1,1),(0,1,0)),dtype=np.uint8)  # 腐蚀核((h,w))
print(kernel2.shape)
res = cv2.erode(img, kernel, iterations=3)
res2 = cv2.erode(img, kernel2, iterations=3)
cv2.imshow('erode', res)
cv2.imshow('cross_erode', res2)

cv2.waitKey()
cv2.destroyAllWindows()
