'''
方框滤波
'''

import cv2
import matplotlib.pyplot as plt

# 椒盐噪声
img01 = cv2.imread('../../../data/noise/sp_noise_lena.jpg')

rgb_sp = cv2.cvtColor(img01, cv2.COLOR_BGR2RGB)

# 方框滤波
res01 = cv2.boxFilter(rgb_sp,  # 图像
                      ddepth=-1,  # 与原图通道一致
                      ksize=(2,2),  # 核大小
                      normalize=0)  # 不归一化（周围像素值和）
res02 = cv2.boxFilter(rgb_sp,  # 图像
                      ddepth=-1,  # 与原图通道一致
                      ksize=(2,2),  # 核大小
                      normalize=1)  # 归一化(均值滤波)

plt.subplot(131)
plt.axis('off')
plt.title('sp')
plt.imshow(rgb_sp)
plt.subplot(132)
plt.axis('off')
plt.title('non-normalize(box)')
plt.imshow(res01)
plt.subplot(133)
plt.axis('off')
plt.title('normalize(avg)')
plt.imshow(res02)

plt.show()
