'''
    开运算：先腐蚀后膨胀
'''

import cv2
import numpy as np

img = cv2.imread('../../../data/5.png')
cv2.imshow('img', img)

# 开运算
kernel = cv2.getStructuringElement(cv2.MORPH_RECT, (3,3))
kernel2 = np.array(((1,1,1),(1,1,1),(1,1,1)),dtype=np.uint8)
print(kernel)
res = cv2.morphologyEx(img,
                       cv2.MORPH_OPEN,
                       kernel,
                       iterations=2)
cv2.imshow('OPEN', res)
res2 = cv2.morphologyEx(img,
                       cv2.MORPH_OPEN,
                       kernel2,
                       iterations=2)
cv2.imshow('OPEN2', res2)

cv2.waitKey()
cv2.destroyAllWindows()
