'''
 Roberts算子
'''

import cv2
import numpy as np

img = cv2.imread('../../../data/lena.jpg', 0)


# Roberts算子
def Robert():
    # dtype不用uint8: 会把-1转化为255
    dx = [[-1, 0], [0, 1]]
    kernel_x = np.array(dx, dtype=int)
    dy = [[0, -1], [1, 0]]
    kernel_y = np.array(dy, dtype=int)
    # print(kernel_x,kernel_y)
    return kernel_x, kernel_y


# Prewitt算子
def Prewitt():
    # dtype不用uint8: 会把-1转化为255
    dy = [[-1, -1, -1], [0, 0, 0], [1, 1, 1]]
    kernel_x = np.array(dy, dtype=int)
    dx = [[1, 0, -1], [1, 0, -1], [1, 0, -1]]
    kernel_y = np.array(dx, dtype=int)
    # print(kernel_x,kernel_y)
    return kernel_x, kernel_y


# kernel_y = np.array(dy, dtype='uint8')
# ddepth: 目标图像深度（指数据类型）中间的数字代表数据类型所占用的空间（bit）.所以,深度指的是数据类型.
# CV_16S - 16位有符号整数（-32768~32767）
# kernel_x, kernel_y = Robert()
kernel_x, kernel_y = Prewitt()
x = cv2.filter2D(img, ddepth=cv2.CV_16S, kernel=kernel_x)
y = cv2.filter2D(img, ddepth=cv2.CV_16S, kernel=kernel_y)

# int16转uint8
# 在进行了 Roberts 算子处理之后，还需要调用convertScaleAbs()函数计算绝对值，并将图像转换为8位图进行显示，然后才能进行
abs_x = cv2.convertScaleAbs(x)
abs_y = cv2.convertScaleAbs(y)
Roberts = cv2.addWeighted(abs_x, 0.5,
                          abs_y, 0.5,
                          0)

cv2.imshow('gray', img)
cv2.imshow('Roberts', Roberts)
# cv2.imshow('x', x)
# cv2.imshow('y', y)
# cv2.imshow('ax', abs_x)
# cv2.imshow('ay', abs_y)
# cv2.imwrite('Roberts_CV_16S.png', Roberts)
print('写入成功')
# print(x, '\n\n',
#       y, '\n\n',
#       abs_x, '\n\n',
#       abs_y)
cv2.waitKey()
cv2.destroyAllWindows()
