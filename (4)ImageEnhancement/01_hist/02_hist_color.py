'''
图像直方图
'''
import cv2
import matplotlib.pyplot as plt

img02 = cv2.imread('../../../data/lena.jpg',0)
cv2.imshow('img_gray', img02)
img01 = cv2.imread('../../../data/lena.jpg',3)
cv2.imshow('img', img01)
# 获取bgr三通道
b, g, r = cv2.split(img01)

# 蓝色通道
plt.subplot(221)
plt.title('b')
plt.hist(b.ravel(), bins=256, facecolor='b', edgecolor='b')
# 绿色通道
plt.subplot(222)
plt.title('g')
plt.hist(g.ravel(), bins=256, facecolor='g', edgecolor='g')
# 红色通道
plt.subplot(223)
plt.title('r')
plt.hist(r.ravel(), bins=256, facecolor='r', edgecolor='r')
# 灰色
plt.subplot(224)
plt.title('gray')
plt.hist(img02.ravel(), bins=256, facecolor='gray', edgecolor='gray')

plt.xlabel('x')
plt.ylabel('y')
plt.show()


cv2.waitKey()
cv2.destroyAllWindows()
