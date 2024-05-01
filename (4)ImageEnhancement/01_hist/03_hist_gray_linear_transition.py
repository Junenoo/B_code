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
import matplotlib.pyplot as plt


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
    gray_img = cv2.cvtColor(lena, cv2.COLOR_BGR2GRAY)
    cv2.imshow('gray', gray_img)


    # α=1, b!=0
    res01 = brightness(lena, b=50)
    cv2.imshow('+50', res01)
    res02 = brightness(lena, b=-50)
    cv2.imshow('-50', res02)

    # α>0, α!=1, b=0
    res03 = brightness(lena, a=2)
    cv2.imshow('*2', res03)
    res04 = brightness(lena, a=0.5)
    cv2.imshow('/2', res04)


    # α=-1, b=255, 反色
    res05 = brightness(lena,a=-1,b=255)
    cv2.imshow('255-', res05)

    # 灰度直方图
    plt.subplot(231)
    plt.title('gray_0')
    plt.hist(gray_img.ravel(), bins=256)

    plt.subplot(232)
    plt.title('gray_+50')
    plt.hist(res01.ravel(), bins=256)
    plt.ylim([0, 3001])
    # plt.yticks([i for i in range(0,3001,500)])

    plt.subplot(233)
    plt.title('gray_-50')
    plt.hist(res02.ravel(), bins=256)
    plt.ylim([0, 3001])

    plt.subplot(234)
    plt.title('gray_*2')
    plt.hist(res03.ravel(), bins=256)
    # plt.ylim([0,3001])
    # plt.yticks([i for i in range(0, 2500, 500)])

    plt.subplot(235)
    plt.title('gray_/2')
    plt.hist(res04.ravel(), bins=256)

    plt.subplot(236)
    plt.title('gray_-')
    plt.hist(res05.ravel(), bins=256)
    plt.show()


    cv2.waitKey()
    cv2.destroyAllWindows()
