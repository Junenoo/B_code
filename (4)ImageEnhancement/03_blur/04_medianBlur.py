'''
中值滤波
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
rgb_p = cv2.cvtColor(img02, cv2.COLOR_BGR2RGB)
rgb_g = cv2.cvtColor(img03, cv2.COLOR_BGR2RGB)

# 中值滤波
res01 = cv2.medianBlur(rgb_sp,  # 图像
                       ksize=5)  # 核大小, 必须是正奇数
res02 = cv2.medianBlur(rgb_p,  # 图像
                       ksize=5)  # 核大小, 必须是正奇数
res03 = cv2.medianBlur(rgb_g,  # 图像
                       ksize=5)  # 核大小, 必须是正奇数

plt.subplot(221)
plt.axis('off')
plt.title('sp')
plt.imshow(rgb_sp)

plt.subplot(222)
plt.axis('off')
plt.title('blur01')
plt.imshow(res01)

plt.subplot(223)
plt.axis('off')
plt.title('g')
plt.imshow(rgb_g)

plt.subplot(224)
plt.axis('off')
plt.title('blur02')
plt.imshow(res02)

# plt.show()


cv2.imshow('sp_noise_lena', img01)
cv2.imshow('pulse_noise_lena', img02)
cv2.imshow('gasuss_noise_lena', img03)
cv2.imshow('sp_noise_lena_blur', cv2.cvtColor(res01, cv2.COLOR_RGB2BGR))
cv2.imshow('pulse_noise_lena_blur', cv2.cvtColor(res02, cv2.COLOR_RGB2BGR))
cv2.imshow('gasuss_noise_lena_blur', cv2.cvtColor(res03, cv2.COLOR_RGB2BGR))

cv2.waitKey()
cv2.destroyAllWindows()
