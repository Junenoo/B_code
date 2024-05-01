'''
傅里叶变换（Numpy实现）
二维频谱中的每一个点都是一个与之一一对应的二维正弦/余弦波。
'''

import numpy as np
import cv2
import matplotlib.pyplot as plt

file = '../../../data/98.png'
img = cv2.imread(file, 0)
cv2.imshow('img', img)

'''傅里叶变换'''
# 快速傅里叶变换得到频率分布
f = np.fft.fft2(img)
# 默认结果中心是左上角
fshift = np.fft.fftshift(f)  # 转移到中心位置
# fft结果是复数 其绝对值结果是振幅    y= Asin(wx+φ)   |A|:振幅——最大值
# 取绝对值：将复数变化成实数
# 取对数：将数据变化到0-255
fimg = np.log(np.abs(fshift))
cv2.imshow('ft', fimg)

'''傅里叶逆变换'''
# ishift = np.fft.ifftshift(fshift)
# iimg = np.fft.ifft2(ishift)
# iimg = np.abs(iimg)
# 显示结果
titles = ['a) original', 'b)FT processing', 'c)inverse']
imgs = [img,
        fimg,
        # iimg
        ]

for i in range(len(imgs)):
    plt.subplot(1, len(imgs), i + 1)
    plt.title(titles[i])
    plt.imshow(imgs[i],'gray')
    plt.axis('off')
plt.show()
cv2.waitKey()
cv2.destroyAllWindows()
