'''
梯度运算: 膨胀 - 腐蚀
'''
import cv2
import numpy as np

img = cv2.imread('../../../data/85.png',0)

cv2.imshow('img', img)

# 卷积核
kernel = np.ones((3,3), dtype='uint8')
# 梯度运算
res = cv2.morphologyEx(img,
                       cv2.MORPH_GRADIENT,
                       kernel)
cv2.imshow('res', res)
cv2.waitKey()
cv2.destroyAllWindows()
