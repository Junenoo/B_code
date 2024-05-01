'''
高通滤波器(用于边缘提取)
图像信号中的高频分量，指的就是图像信号强度（亮度灰度）变化剧烈的地方，也就是我们常说的边缘（轮廓）
'''

import numpy as np
import cv2
import matplotlib.pyplot as plt


def ddft(im_gray):
    '''傅里叶变换'''
    # 快速傅里叶变换得到频率分布
    f = np.fft.fft2(im_gray)
    # 默认结果中心是左上角
    fshift = np.fft.fftshift(f)  # 转移到中心位置
    # fft结果是复数 其绝对值结果是振幅
    # 取绝对值：将复数变化成实数
    # 取对数：将数据变化到0-255
    fimg = np.log(np.abs(fshift))
    return fshift, fimg


def high_pass_fliter(fshift,n):
    '''高通滤波器'''
    h, w = img.shape
    ch, cw = int(h / 2), int(w / 2)
    fshift[ch - n:ch + n, cw - n:cw + n] = 0
    return fshift


def ddft_inv(fshift):
    '''傅里叶逆变换'''
    ishift = np.fft.ifftshift(fshift)
    iimg = np.fft.ifft2(ishift)
    iimg = np.abs(iimg)
    return iimg


if __name__ == '__main__':
    # file = '../../../data/lily_square.png'
    file = '../../../data/lena.jpg'
    img = cv2.imread(file, 0)

    fshift, fimg = ddft(img)
    fshift = high_pass_fliter(fshift,60)
    iimg = ddft_inv(fshift)
    _, fimg01 = ddft(iimg)

    # 显示结果
    titles = ['a) original', 'b)FT processing', 'c)inverse', 'd)FT processing after high-pass filter']
    imgs = [img,
            fimg,
            iimg,
            fimg01
            ]

    for i in range(len(imgs)):
        plt.subplot(2, len(imgs) // 2, i + 1)
        plt.title(titles[i])
        plt.imshow(imgs[i], 'gray')
        plt.axis('off')
    plt.show()
    # cv2.waitKey()
    # cv2.destroyAllWindows()
