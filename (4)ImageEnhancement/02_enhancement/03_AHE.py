'''
AHE(Adaptive Histogram Equalization)
局部直方图均衡化
'''

import cv2
import numpy as np
import matplotlib.pyplot as plt

img = cv2.imread('../../../data/lena.jpg')
gray = cv2.imread('../../../data/lena.jpg', 0)
cv2.imshow('gray', gray)
# gray_img = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
# cv2.imshow('gray', gray_img)

# 局部直方图均衡化
clahe = cv2.createCLAHE(clipLimit=1,  # 对比度大小, 值越大灰度越往两边靠
                        tileGridSize=(9,9))  # 每次处理块的大小, 值越大灰度越往中间靠
# 将灰度图与局部直方图关联,把直方图均衡化应用到灰度图
res = clahe.apply(gray)
cv2.imshow('res', res)

# 直方图
plt.subplot(121)
plt.hist(gray.ravel(), bins=256, color='gray')
plt.title('gray')
plt.subplot(122)
plt.hist(res.ravel(), bins=256, color='gray')
plt.title('AHE')
plt.show()

cv2.waitKey()
cv2.destroyAllWindows()
