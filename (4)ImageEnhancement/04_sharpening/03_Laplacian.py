'''
Laplacian拉普拉斯算子
'''

import cv2
import numpy as np


def Laplacian_and_LoG(gray_img, w: int):
    '''
        Laplacian算子和LoG算子
        :param gray_img: 输入的灰度图像
        :param w: 1: 不经过高斯滤波的Laplacian算子    2:经过高斯滤波的LoG算子
        :return:
        '''

    if w == 1:  # 不经过高斯滤波降噪
        intput_img = gray_img
    if w == 2:  # 高斯滤波降噪
        gaussian = cv2.GaussianBlur(gray_img,
                                    ksize=(5, 5),  # 高斯滤波器模板大小
                                    sigmaX=0)  # 高斯核函数在x方向的高斯内核标准差
        intput_img = gaussian

    else:
        print('w只能为1或2')
    # Laplacian拉普拉斯算子   输出边缘图
    dst = cv2.Laplacian(intput_img,
                        cv2.CV_16S,
                        ksize=3)  # 计算二阶导数的滤波器孔径大小, 必须正奇数, ksize=1 => 采用3x3孔径四领域模板
    # print('dst={}\ndst_shape={}\ndst_dtype={}'.format(dst, dst.shape, dst.dtype))
    # int16转uint8
    # 在进行了 Roberts 算子处理之后，还需要调用convertScaleAbs()函数计算绝对值，并将图像转换为8位图进行显示，然后才能进行
    Laplacian = cv2.convertScaleAbs(dst)

    # dst = np.array(abs(dst), dtype='uint8')  # 计算绝对值，并将图像转换为8位图进行显示
    # print('dst={}\ndst_shape={}\ndst_dtype={}'.format(dst, dst.shape, dst.dtype))
    print('Laplacian={}\nLaplacian_shape={}\nLaplacian_dtype={}'.format(Laplacian, Laplacian.shape, Laplacian.dtype))
    return Laplacian


img = cv2.imread('../../../data/lena.jpg')
gray_img = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)

cv2.imshow('img', img)
cv2.imshow('gray_img', gray_img)
Laplacian = Laplacian_and_LoG(gray_img, 1)
cv2.imshow('Laplacian', Laplacian)
LoG = Laplacian_and_LoG(gray_img, 2)
cv2.imshow('LoG', LoG)

cv2.waitKey()
cv2.destroyAllWindows()
