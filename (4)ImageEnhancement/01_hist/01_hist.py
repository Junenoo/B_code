'''
图像直方图
'''
import cv2
import matplotlib.pyplot as plt
import numpy as np

'''  plt显示直方图  '''
# img = cv2.imread('../../../data/lena.jpg',0)
# # 灰度
# plt.hist(img.ravel(), bins=256)
# plt.xlabel('x')
# plt.ylabel('y')
# plt.show()
#
# cv2.imshow('img', img)
# cv2.waitKey()
# cv2.destroyAllWindows()

'''  cv2显示直方图  图像直方图 calcHist'''
img02 = cv2.imread('../../../data/lena.jpg',0)
cv2.imshow('img_gray', img02)
img01 = cv2.imread('../../../data/lena.jpg',3)
cv2.imshow('img', img01)
mask = np.zeros(img02.shape[:2], np.uint8)
mask[100:300, 100:400] = 255
masked_img = cv2.bitwise_and(img01, img01, mask=mask)
cv2.imshow('masked_img', masked_img)
# b
plt.subplot(221)
plt.title('b')
hist_b = cv2.calcHist([img01], channels=[0],mask=mask, histSize=[256], ranges=[0, 255])
plt.plot(hist_b, color='b')
# g
plt.subplot(222)
plt.title('green')
hist_green = cv2.calcHist([img01], channels=[1],mask=mask, histSize=[256], ranges=[0, 255])
plt.plot(hist_green, color='g')
# r
plt.subplot(223)
plt.title('r')
hist_r = cv2.calcHist([img01], channels=[2],mask=mask, histSize=[256], ranges=[0, 255])
plt.plot(hist_r, color='r')
# g
plt.subplot(224)
hist_gray = cv2.calcHist([img02], channels=[0],mask=mask, histSize=[256], ranges=[0, 255])
plt.title('gray')
plt.plot(hist_gray, color='gray')
plt.show()

cv2.waitKey()
cv2.destroyAllWindows()
