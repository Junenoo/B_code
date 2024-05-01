'''
黑帽运算: 原图 - 闭运算
'''
import cv2
import numpy as np

img = cv2.imread('../../../data/9.png', 0)

cv2.imshow('img', img)

# 卷积核
kernel = cv2.getStructuringElement(cv2.MORPH_CROSS, (2,2))
# 梯度运算
res = cv2.morphologyEx(img,
                       cv2.MORPH_BLACKHAT,
                       kernel)
cv2.imshow('res', res)
cv2.waitKey()
cv2.destroyAllWindows()
