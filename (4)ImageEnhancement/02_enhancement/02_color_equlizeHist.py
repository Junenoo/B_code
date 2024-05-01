'''
直方图均衡化
'''
import cv2
import numpy as np
import matplotlib.pyplot as plt

img = cv2.imread('../../../data/lena.jpg')
# img = cv2.imread('../../../data/albums/honeymoon.jpg')
# img = cv2.resize(img, None, fx=0.5, fy=0.5)
cv2.imshow('img', img)

# 获取三通道并均衡化
# b,g,r=cv2.split(img)
b, g, r = img[:, :, 0], img[..., 1], img[..., 2]
bh = cv2.equalizeHist(b)
gh = cv2.equalizeHist(g)
rh = cv2.equalizeHist(r)

bgr = cv2.merge((bh, gh, rh))
cv2.imshow('bgr_equlized', bgr)


# b
plt.subplot(421)
plt.hist(b.ravel(), bins=256, color='b')
plt.title('b')
plt.subplot(422)
plt.hist(bh.ravel(), bins=256, color='b')
plt.title('bh')
# g
plt.subplot(423)
plt.hist(g.ravel(), 256, color='g')
plt.title('g')
plt.subplot(424)
plt.hist(gh.ravel(), 256, color='g')
plt.title('gh')
# r
plt.subplot(425)
plt.hist(r.ravel(), 256, color='r')
plt.title('r')
plt.subplot(426)
plt.hist(rh.ravel(), 256, color='r')
plt.title('rh')
# original
plt.subplot(427)
plt.hist(b.ravel(), bins=256, color='b')
plt.hist(g.ravel(), 256, color='g')
plt.hist(r.ravel(), 256, color='r')
plt.title('original')
# equlized
plt.subplot(428)
plt.hist(bh.ravel(), bins=256, color='b')
plt.hist(gh.ravel(), 256, color='g')
plt.hist(rh.ravel(), 256, color='r')
plt.title('equlized')

plt.show()
#
cv2.waitKey()
cv2.destroyAllWindows()
