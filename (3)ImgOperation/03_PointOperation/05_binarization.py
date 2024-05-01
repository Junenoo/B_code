'''
图像阈值化处理
'''

import cv2
import numpy as np


def thresh_binary(img):
    '''
    THRESH_BINARY
    大于thresh=127 => 255, 小于等于thresh=127 => 0
    :param img: 原图
    :return: 二值化图像
    '''
    # 变灰度图
    img = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
    # 二进制阈值化处理
    r, b = cv2.threshold(img, thresh=127, maxval=255, type=cv2.THRESH_BINARY)
    return b


def thresh_binary_inv(img):
    '''
    THRESH_BINARY_INV
    大于thresh=127 => 0, 小于等于thresh=127 => 255
    :param img: 原图
    :return: 二值化图像
    '''
    # 变灰度图
    img = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
    # 二进制阈值化处理
    r, b = cv2.threshold(img, thresh=127, maxval=255, type=cv2.THRESH_BINARY_INV)
    return b


def thresh_trunc(img):
    '''
    THRESH_TRUNC
    大于thresh=127 => 127, 小于等于thresh=127 => 不变
    :param img: 原图
    :return: 灰度图像
    '''
    # 变灰度图
    img = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
    # 二进制阈值化处理
    r, b = cv2.threshold(img, thresh=127, maxval=255, type=cv2.THRESH_TRUNC)  # truncation截断
    return b


def thresh_tozero(img):
    '''
    THRESH_TOZERO
    大于thresh=127 => 不变, 小于等于thresh=127 => 0
    :param img: 原图
    :return: 灰度图像
    '''
    # 变灰度图
    img = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
    # 二进制阈值化处理
    r, b = cv2.threshold(img, thresh=127, maxval=255, type=cv2.THRESH_TOZERO)
    return b


def thresh_tozero_inv(img):
    '''
    THRESH_TOZERO_INV
    大于thresh=127 => 0, 小于等于thresh=127 => 不变
    :param img: 原图
    :return: 灰度图像
    '''
    # 变灰度图
    img = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
    # 二进制阈值化处理
    r, b = cv2.threshold(img, thresh=127, maxval=255, type=cv2.THRESH_TOZERO_INV)
    return b


if __name__ == '__main__':
    lena = cv2.imread('../../../data/lena.jpg')
    cv2.imshow('lena', lena)

    print(lena.shape)

    res01 = thresh_binary(lena)
    cv2.imshow('thresh_binary', res01)
    res02 = thresh_binary_inv(lena)
    cv2.imshow('thresh_binary_inv', res02)
    res03 = thresh_trunc(lena)
    cv2.imshow('thresh_trunc', res03)
    res04 = thresh_tozero(lena)
    cv2.imshow('thresh_tozero', res04)
    res05 = thresh_tozero_inv(lena)
    cv2.imshow('thresh_tozero_inv', res05)

    cv2.waitKey()
    cv2.destroyAllWindows()
