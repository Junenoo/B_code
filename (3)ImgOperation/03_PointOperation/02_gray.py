'''
灰度化处理
'''
import cv2
import numpy as np

img = cv2.imread('../../../data/opencv.png')
gray = cv2.imread('../../../data/opencv.png',0)
cv2.imshow('color', img)
cv2.imshow('gray', gray)
h, w = img.shape[:2]

# 创建空图
grayimg01 = np.zeros((h, w, 3), dtype='uint8')
grayimg02 = np.zeros((h, w, 3), dtype='uint8')
grayimg03 = np.zeros((h, w, 3), dtype='uint8')


# 1.最大灰度处理
def max_gray(img, i, j):
    return max(img[i, j][0], img[i, j][1], img[i, j][2])


# 2.平均灰度处理
def mean_gray(img, i, j):
    return np.mean([int(img[i, j][0]), int(img[i, j][1]), int(img[i, j][2])])


# # 3.加权平均灰度处理b
# def weight_mean_gray_b(img, i, j):
#     return int(img[i, j][0]) * 1 + int(img[i, j][1]) * 0 + int(img[i, j][2]) * 0
# # 3.加权平均灰度处理g
# def weight_mean_gray_g(img, i, j):
#     return int(img[i, j][0]) * 0 + int(img[i, j][1]) * 1 + int(img[i, j][2]) * 0
# # 3.加权平均灰度处理r
# def weight_mean_gray_r(img, i, j):
#     return int(img[i, j][0]) * 0 + int(img[i, j][1]) * 0 + int(img[i, j][2]) * 1
# 3.加权平均灰度处理
def weight_mean_gray(img, i, j):
    #          img[i, j][0]:R            img[i, j][1]:G             img[i, j][2]:B
    return int(img[i, j][0]) * 0.3 + int(img[i, j][1]) * 0.59 + int(img[i, j][2]) * 0.11


for i in range(h):
    for j in range(w):
        grayimg01[i, j] = np.uint8(max_gray(img, i, j))
        grayimg02[i, j] = np.uint8(mean_gray(img, i, j))
        grayimg03[i, j] = np.uint8(weight_mean_gray(img, i, j))

cv2.imshow('max', grayimg01)
cv2.imshow('mean', grayimg02)
cv2.imshow('wight_mean', grayimg03)

cv2.waitKey()
cv2.destroyAllWindows()
