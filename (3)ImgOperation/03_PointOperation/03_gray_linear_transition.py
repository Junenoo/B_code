'''
灰度线性变化
(DB) = f(DA) = α (DA) + b
α=1, b=0 原图
α=-1, b=0 取反
α=1, b!=0 亮度增加(b>0) 亮度降低(b<0)
α>0, α!=1, b=0 对比度增加(α>1)   对比度降低(α<1)
α=-1, b=0 取反

'''

import cv2
import numpy as np


def brightness(img, a=1.0, b=0.0):
    '''
    灰度线性变化  (DB) = f(DA) = α (DA) + b
    :param img: 原图
    :param a: 斜率
    :param b: 截距
    :return: 线性变化后的灰度图
    '''
    # 变灰度图
    img = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
    # 获取高宽
    h, w = img.shape[:2]
    # 创建空图
    res = np.zeros((h, w), dtype='uint8')
    for i in range(h):
        for j in range(w):
            # (DB) = f(DA) = α (DA) + b
            gray = a * int(img[i, j]) + b
            if gray >= 255:
                gray = 255
            if gray <= 0:
                gray = 0
            res[i, j] = np.uint8(gray)
    return res


if __name__ == '__main__':
    lena = cv2.imread('../../../data/lena.jpg')
    print(lena.shape)
    cv2.imshow('lena', lena)
    cv2.imshow('gray', cv2.cvtColor(lena, cv2.COLOR_BGR2GRAY))

    # α=1, b!=0（改变亮度）
    res01 = brightness(lena, b=50)
    # cv2.imshow('+50', res01)
    res02 = brightness(lena, b=-50)
    # cv2.imshow('-50', res02)

    # α>0, α!=1, b=0（改变对比度）
    res03 = brightness(lena, a=2)
    # cv2.imshow('*2', res03)
    res04 = brightness(lena, a=0.5)
    # cv2.imshow('/2', res04)

    # α=-1, b=255, 反色
    res05 = brightness(lena,a=-1,b=255)
    cv2.imshow('255-', res05)

    cv2.waitKey()
    cv2.destroyAllWindows()
