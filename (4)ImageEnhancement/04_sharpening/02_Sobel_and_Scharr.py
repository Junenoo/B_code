'''
 Roberts算子
'''

import cv2
import numpy as np



def Sobel(img):
    '''
    Sobel算子
    :param img:
    :return:
    '''
    # ddepth: 目标图像深度（指数据类型）中间的数字代表数据类型所占用的空间（bit）.所以,深度指的是数据类型.
    # CV_16S - 16位有符号整数（-32768~32767）
    x = cv2.Sobel(img, ddepth=cv2.CV_16S, dx=1, dy=0)
    y = cv2.Sobel(img, ddepth=cv2.CV_16S, dx=0, dy=1)
    return x, y


def Scharr(img):
    '''
    Scharr算子
    :param img:
    :return:
    '''
    # ddepth: 目标图像深度（指数据类型）中间的数字代表数据类型所占用的空间（bit）.所以,深度指的是数据类型.
    # CV_16S - 16位有符号整数（-32768~32767）
    x = cv2.Scharr(img, ddepth=cv2.CV_16S, dx=1, dy=0)
    y = cv2.Scharr(img, ddepth=cv2.CV_16S, dx=0, dy=1)
    return x, y


img = cv2.imread('../../../data/lena.jpg', 0)
# int16转uint8
# 在进行了 Roberts 算子处理之后，还需要调用convertScaleAbs()函数计算绝对值，并将图像转换为8位图进行显示，然后才能进行
sobel_x, sobel_y = Sobel(img)
abs_sobel_x = cv2.convertScaleAbs(sobel_x)
abs_sobel_y = cv2.convertScaleAbs(sobel_y)
Sobel = cv2.addWeighted(abs_sobel_x, 0.5,
                        abs_sobel_y, 0.5,
                        0)
scharr_x, scharr_y = Scharr(img)
abs_scharr_x = cv2.convertScaleAbs(scharr_x)
abs_scharr_y = cv2.convertScaleAbs(scharr_y)
Scharr = cv2.addWeighted(abs_scharr_x, 0.5,
                         abs_scharr_y, 0.5,
                         0)

cv2.imshow('gray', img)
cv2.imshow('Sobel', Sobel)
cv2.imshow('Scharr', Scharr)
# cv2.imshow('x', x)
# cv2.imshow('y', y)
# cv2.imshow('ax', abs_x)
# cv2.imshow('ay', abs_y)
cv2.imwrite('Sobel_CV_16S.png', Sobel)
cv2.imwrite('Scharr_CV_16S.png', Scharr)
print('写入成功')
# print(x, '\n\n',
#       y, '\n\n',
#       abs_x, '\n\n',
#       abs_y)
cv2.waitKey()
cv2.destroyAllWindows()
