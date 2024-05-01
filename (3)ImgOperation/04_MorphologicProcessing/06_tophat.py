'''
顶帽运算（礼帽运算）：原图 - 开运算
'''
import cv2
import numpy as np

img = cv2.imread('../../../data/5.png',0)

cv2.imshow('img', img)

# 卷积核
kernel = np.ones((2,2), dtype='uint8')
# 梯度运算
res = cv2.morphologyEx(img,
                       cv2.MORPH_TOPHAT,
                       kernel)
cv2.imshow('res', res)
cv2.waitKey()
cv2.destroyAllWindows()
