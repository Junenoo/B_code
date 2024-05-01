'''
低通滤波器(用于模糊处理)
图像信号中的低频分量，指的就是图像强度（亮度灰度）变换平缓的地方，也就是大片色块，变化不那么明显的地方。
'''

import numpy as np
import cv2
import matplotlib.pyplot as plt


# cv2.imshow('img',img)

def ddft(im_gray):
    '''
    傅里叶变换
    '''
    # 快速傅里叶变换, 返回实部和虚部
    dft = cv2.dft(np.float32(im_gray),
                  flags=cv2.DFT_COMPLEX_OUTPUT)
    # 默认结果中心是左上角
    dft_shift = np.fft.fftshift(dft)  # 把频谱低频左上角转移到中心位置
    # 将傅里叶变换的双通道转换为0-255区间
    # cv2.magnitude(x,y) x: 实部, y: 虚部
    mag = cv2.magnitude(dft_shift[:, :, 0],
                        dft_shift[:, :, 1])
    result1 = 20 * np.log(mag)
    return dft_shift, result1


def low_pass_filter(dft_shift, n):
    '''低通滤波器'''
    h, w = img.shape
    ch, cw = int(h / 2), int(w / 2)
    mask = np.zeros((h, w, 2), dtype=int)
    mask[ch - n: ch + n, cw - n: cw + n] = 1
    '''掩模图像和频谱图像的乘积'''
    f = dft_shift * mask
    '''傅里叶逆变换'''
    ishift = np.fft.ifftshift(f)
    iimg = cv2.idft(ishift)
    result2 = cv2.magnitude(iimg[:, :, 0],
                            iimg[:, :, 1])
    return result2


if __name__ == '__main__':
    file = '../../../data/lily_square.png'
    img = cv2.imread(file, 0)

    # 傅里叶变换
    dft_shift, result1 = ddft(img)

    # 低通滤波器
    result2 = low_pass_filter(dft_shift, 10)

    # 傅里叶变换
    _, result3 = ddft(result2)

    # 显示结果
    titles = ['a) original', 'b)FT processing', 'c)inverse', 'd)FT processing after low-pass filter']
    imgs = [img,
            result1,
            result2,
            result3
            ]

    for i in range(len(imgs)):
        plt.subplot(2, len(imgs) // 2, i + 1)
        plt.title(titles[i])
        plt.imshow(imgs[i], 'gray')
        plt.axis('off')

    plt.show()
    # cv2.waitKey()
    # cv2.destroyAllWindows()
