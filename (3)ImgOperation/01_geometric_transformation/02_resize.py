'''
缩放变换
    （sx, sy）缩放因子
                          ((sx  0  0)
    (x1 y1 1) = (x0 y0 1)  (0  sy  0)
                           (0  0  1))
'''

import cv2
import numpy as np


def resize1(img):
    h, w = img.shape[:2]

    # 缩放1（dsize）缩放大小
    res01 = cv2.resize(img, dsize=(int(w / 2), int(h / 2)))
    res02 = cv2.resize(img, (w * 2, h * 2))
    cv2.imshow('small01', res01)
    cv2.imshow('large01', res02)
    # 缩放2（fx,fy）缩放比例
    res03 = cv2.resize(img, None, fx=0.25, fy=0.55)
    res04 = cv2.resize(img, None, fx=2, fy=1.3)
    cv2.imshow('small02', res03)
    cv2.imshow('large02', res04)


def resize2(img, scale=1.5):
    h, w = img.shape[:2]
    INTER_NEAREST = cv2.resize(img, (int(w * scale), int(h * scale)), interpolation=cv2.INTER_NEAREST)  # 最近邻插值法
    INTER_LINEAR = cv2.resize(img, (int(w * scale), int(h * scale)), interpolation=cv2.INTER_LINEAR)  # 双线性插值法
    INTER_CUBIC = cv2.resize(img, (int(w * scale), int(h * scale)), interpolation=cv2.INTER_CUBIC)  # 双三次插值法
    INTER_AREA = cv2.resize(img, (int(w * scale), int(h * scale)), interpolation=cv2.INTER_AREA)  # 区域插值法
    INTER_LANCZOS4 = cv2.resize(img, (int(w * scale), int(h * scale)), interpolation=cv2.INTER_LANCZOS4)  # 兰索斯插值法
    cv2.imshow('INTER_NEAREST', INTER_NEAREST)
    cv2.imshow('INTER_LINEAR', INTER_LINEAR)
    cv2.imshow('INTER_CUBIC', INTER_CUBIC)
    cv2.imshow('INTER_AREA', INTER_AREA)
    cv2.imshow('INTER_LANCZOS4', INTER_LANCZOS4)


if __name__ == '__main__':
    img = cv2.imread('../../../data/lena.jpg')
    cv2.imshow('img', img)
    resize1(img)
    # resize2(img)
    cv2.waitKey()
    cv2.destroyAllWindows()
