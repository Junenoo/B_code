'''
灰度非线性变化
对数变换、指数变化、幂次变换、分段函数
'''

import cv2
import numpy as np


def nonlinearTranslation(img):
    '''
    非线性变换（提高对比度）
    :param img: 原图
    :return: 幂次变换后的图
    '''
    # 变灰度图
    img = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
    # 获取高宽
    h, w = img.shape[:2]
    # 创建空图
    res = np.zeros((h, w), dtype='uint8')
    for i in range(h):
        for j in range(w):
            gray = (int(img[i, j]) ** 2) / 255
            if gray >= 255:
                gray = 255
            if gray <= 0:
                gray = 0
            res[i, j] = np.uint8(gray)
    return res


def logTranslation(img, c=42.0, b=0.0):
    '''
    对数变换（对数变换后的图像较暗区域的对比度有所提升, 扩展低灰度值,压缩高灰度值）
    应用：傅里叶频谱, 增强暗部细节
    :param img: 原图
    :param c: 尺度
    :param b: 增加亮度
    :return: 对数变换后的图像
    '''
    # 变灰度图
    # img = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
    # (DB) = f(DA) = c * loge(DA)
    gray = c * np.log(1.0 + img)
    res = np.uint8(gray + b)
    return res


def gammaTranslation(img, c=1.0, v=1.0, b=0.0):
    '''
    伽马变换（指数变换或幂次变换）: 对于对比度较低而整体亮度较高的图像效果明显
    在图像处理中，常常利用伽马变换来对过曝或者曝光不足（过暗）的灰度图利用伽马变换进行对比度调节。
    通过非线性变换，让图像中较暗的区域的灰度值得到增强，图像中灰度值过大的区域的灰度值得到降低
    经过伽马变换，图像整体的细节表现会得到增强。
    :param img: 原图
    :param v: 指数 γ>1: 拉伸灰度级较高的区域,压缩灰度级较低的区域;降低灰度级，使图像变暗
                  γ<1: 拉伸灰度级较低的区域,压缩灰度级较高的区域;提高灰度级，使图像变亮
                  γ=1: 线性变换
    :param c:
    :param b:
    :return: 伽马变换后的图像
    '''
    # 变灰度图
    img = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
    # 创建空图
    lut = np.zeros(256, dtype=np.float32)
    for i in range(256):
        lut[i] = c * np.power(i / 255, v) * 255
    gray_img = cv2.LUT(img, lut)  # 像素灰度值映射
    res = np.uint8(gray_img + b)
    return res


def piecewiselinearTranslation(img):
    '''
    突出感兴趣的目标或灰度区间，相对抑制不感兴趣的灰度区域，可采用分段线性变换。
    分段线性函数同样是点运算，基于像素的图像增强，也就是对比度拉伸。
    将不同灰度区间的灰度值经过不同的映射函数映射到另一个灰度区间的过程。
    对应的数学公式为 I_{out} = a * I_{in} + b
    a = 1,b = 0 时恒等函数,不改变图像的灰度值
    a >1,对比度增强
    0 < a < 1, 对比度减弱
    b 控制图像的亮度, b > 0 图像变亮, b < 0 图像变弱
    :param img: 原图像
    :return: 变换后的图像
    '''
    # 变灰度图
    img = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
    # 获取高宽
    h, w = img.shape[:2]
    # 创建空图
    res = np.zeros((h, w), dtype='uint8')
    # 三段函数的斜率
    r1, s1 = 80, 10
    r2, s2 = 140, 200
    k1 = s1 / r1
    k2 = (s2 - s1) / (r2 - r1)
    k3 = (255 - s2) / (255 - r2)

    for i in range(h):
        for j in range(w):
            if int(img[i, j]) < r1:
                res[i, j] = k1 * int(img[i, j])
            elif r1 <= int(img[i, j]) < r2:
                res[i, j] = k2 * int(img[i, j])
            else:
                res[i, j] = k3 * int(img[i, j])
    return res


if __name__ == '__main__':
    gamma = cv2.imread('../../../data/gamma.jpg')
    gamma02 = cv2.imread('../../../data/gamma02.jpg')
    gamma03 = cv2.imread('../../../data/gamma03.jpg')
    log = cv2.imread('../../../data/log02.jpg')
    lena = cv2.imread('../../../data/lena.jpg')
    lily = cv2.imread('../../../data/lily.png')
    pl = cv2.imread('../../../data/03.jpg')
    print(lena.shape)
    cv2.imshow('pl', pl)
    # cv2.imshow('gamma01', gamma)
    # cv2.imshow('gamma02', gamma02)
    # cv2.imshow('gamma03', gamma03)
    # cv2.imshow('log', log)
    # cv2.imshow('lena', lena)
    # cv2.imshow('lily', lily)
    # cv2.imshow('gray', cv2.cvtColor(lena, cv2.COLOR_BGR2GRAY))

    # 非线性变换
    res01 = nonlinearTranslation(lily)
    # cv2.imshow('**2/255', res01)
    # 对数变换
    res02 = logTranslation(log)
    # cv2.imshow('50log(1+)', res02)
    # 伽马变换
    res04 = gammaTranslation(gamma02, v=5)
    # cv2.imshow('gamma02_res', res04)
    res03 = gammaTranslation(gamma, v=0.5)
    # cv2.imshow('gamma01_res', res03)
    res05 = gammaTranslation(gamma03, v=0.3)
    # cv2.imshow('gamma03_res', res05)
    # 分段函数
    res06 = piecewiselinearTranslation(pl)
    # cv2.imshow('piecewise_linear01', res06)

    # print(np.power(3, 2))  # 9
    # print(np.power(2, 3))  # 8

    cv2.waitKey()
    cv2.destroyAllWindows()
