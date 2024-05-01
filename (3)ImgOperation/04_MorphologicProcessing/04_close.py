'''
    闭运算: 先膨胀后腐蚀
'''

import cv2
import numpy as np

img = cv2.imread('../../../data/fingerprint.jpg')
cv2.imshow('img', img)

# 闭运算
kernel = cv2.getStructuringElement(cv2.MORPH_CROSS, (5,3))
print(kernel)
res = cv2.morphologyEx(img,
                       cv2.MORPH_CLOSE,
                       kernel,
                       iterations=1)
cv2.imshow('CLOSE', res)

cv2.waitKey()
cv2.destroyAllWindows()
