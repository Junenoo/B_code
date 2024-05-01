'''
    颜色转化
'''

import cv2
import numpy as np
import matplotlib.pyplot as plt

# img = cv2.imread('../../../data/lena.jpg')
img = cv2.imread('../../../data/albums/artpop.jpg')
# img = cv2.resize(img,None,fx=0.3,fy=0.3)
transcolor_list = [cv2.COLOR_BGR2RGB,
                   cv2.COLOR_BGR2GRAY,
                   cv2.COLOR_BGR2HSV,
                   cv2.COLOR_BGR2YCrCb,
                   cv2.COLOR_BGR2XYZ,
                   cv2.COLOR_BGR2LAB,
                   cv2.COLOR_BGR2YUV,
                   cv2.COLOR_BGR2HLS]
name_list = ['cv2.COLOR_BGR2RGB',
             'cv2.COLOR_BGR2GRAY',
             'cv2.COLOR_BGR2HSV',
             'cv2.COLOR_BGR2YCrCb',
             'cv2.COLOR_BGR2XYZ',
             'cv2.COLOR_BGR2LAB',
             'cv2.COLOR_BGR2YUV',
             'cv2.COLOR_BGR2HLS']
cv2.imshow('origin', img)
k = 0
for i in transcolor_list:
    transcolor = cv2.cvtColor(img, i)
    cv2.imshow(name_list[k], transcolor)
    k += 1

plt.show()
cv2.waitKey()
cv2.destroyAllWindows()
