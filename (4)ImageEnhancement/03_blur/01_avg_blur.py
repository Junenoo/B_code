'''
均值滤波
'''

import cv2
import matplotlib.pyplot as plt

# 椒盐噪声
img01 = cv2.imread('../../../data/noise/sp_noise_lena.jpg')
# 脉冲噪声
img02 = cv2.imread('../../../data/noise/pulse_noise_lena.jpg')
# 高斯噪声
img03 = cv2.imread('../../../data/noise/gasuss_noise_lena.jpg')

rgb_sp = cv2.cvtColor(img01, cv2.COLOR_BGR2RGB)
rgb_pu = cv2.cvtColor(img02, cv2.COLOR_BGR2RGB)
rgb_g = cv2.cvtColor(img03, cv2.COLOR_BGR2RGB)

# 均值滤波
res01 = cv2.blur(rgb_sp,  # 图像
                 ksize=(7,7))  # 核大小
res02 = cv2.blur(rgb_pu,  # 图像
                 ksize=(7,7))  # 核大小
res03 = cv2.blur(rgb_g,  # 图像
                 ksize=(7,7))  # 核大小

plt.subplot(321)
plt.axis('off')
plt.title('sp')
plt.imshow(rgb_sp, 'gray')
plt.subplot(322)
plt.axis('off')
plt.title('blur01')
plt.imshow(res01, 'gray')

plt.subplot(323)
plt.axis('off')
plt.title('pu')
plt.imshow(rgb_pu, 'gray')
plt.subplot(324)
plt.axis('off')
plt.title('blur02')
plt.imshow(res02, 'gray')

plt.subplot(325)
plt.axis('off')
plt.title('g')
plt.imshow(rgb_g, 'gray')
plt.subplot(326)
plt.axis('off')
plt.title('blur03')
plt.imshow(res03, 'gray')

plt.show()
