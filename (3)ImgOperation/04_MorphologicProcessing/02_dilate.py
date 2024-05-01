'''
    膨胀:图像中较亮的物体尺寸会变大，较暗的物体尺寸会减小
'''

import cv2
import numpy as np

img = cv2.imread('../../../data/9.png')
cv2.imshow('img', img)

# 膨胀
# kernel = np.ones((7,7), np.uint8)  # 膨胀核
kernel = np.ones((7,7), np.uint8)  # 膨胀核
res = cv2.dilate(img, kernel, iterations=1)
cv2.imshow('dilate', res)

cv2.waitKey()
cv2.destroyAllWindows()
