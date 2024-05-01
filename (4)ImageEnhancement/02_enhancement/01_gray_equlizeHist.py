'''
直方图均衡化
'''
import cv2
import numpy as np
import matplotlib.pyplot as plt

img = cv2.imread('../../../data/lena.jpg')
cv2.imshow('img', img)

gray_img = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
cv2.imshow('gray', gray_img)

# 直方图均衡化
res = cv2.equalizeHist(gray_img)
cv2.imshow('equalized', res)

plt.subplot(121)
plt.hist(gray_img.ravel(), bins=256)
plt.title('original')
plt.subplot(122)
plt.hist(res.ravel(), 256)
plt.title('equalized')
plt.show()

cv2.waitKey()
cv2.destroyAllWindows()
