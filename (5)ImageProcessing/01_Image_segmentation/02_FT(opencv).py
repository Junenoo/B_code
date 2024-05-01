'''
傅里叶变换（opencv实现）
1，图像经过二维傅里叶的变换后，其变换稀疏矩阵具有如下性质：若交换矩阵原点设在中心，其频谱能量集中分布在变换稀疏矩阵的中心附近。
  若所用的二维傅里叶变换矩阵的云巅设在左上角，那么图像信号能量将集中在系数矩阵的四个角上。
  这是由二维傅里叶变换本身性质决定的。同时也表明一股图像能量集中低频区域。
2，图像灰度变化缓慢的区域，对应它变换后的低频分量部分；图像灰度呈阶跃变化的区域，对应变换后的高频分量部分。
  除颗粒噪音外，图像细节的边缘，轮廓处都是灰度变换突变区域，他们都具有变换后的高频分量特征。
'''

import numpy as np
import cv2
import matplotlib.pyplot as plt

file = '../../../data/98.png'
img = cv2.imread(file, 0)
# cv2.imshow('img',img)

'''傅里叶变换'''
# 快速傅里叶变换, 返回实部和虚部
dft = cv2.dft(np.float32(img),
              flags=cv2.DFT_COMPLEX_OUTPUT)
# 默认结果中心是四个角
dft_shift = np.fft.fftshift(dft)  # 把频谱低频左上角转移到中心位置
# 将傅里叶变换的双通道转换为0-255区间
# cv2.magnitude(x,y) x: 实部, y: 虚部
mag = cv2.magnitude(dft_shift[:, :, 0],
                    dft_shift[:, :, 1])
result1 = 20 * np.log(mag)

'''傅里叶逆变换'''
ishift = np.fft.ifftshift(dft_shift)
iimg = cv2.idft(ishift)
result2 = cv2.magnitude(iimg[:, :, 0],
                        iimg[:, :, 1])

# 显示结果
titles = ['a) original',
          'b)FT processing',
          'c)inverse'
          ]
imgs = [img,
        result1,
        result2
        ]

for i in range(len(imgs)):
    plt.subplot(1, len(imgs), i + 1)
    plt.title(titles[i])
    plt.imshow(imgs[i],'gray')
    plt.axis('off')

plt.show()
# cv2.waitKey()
# cv2.destroyAllWindows()
