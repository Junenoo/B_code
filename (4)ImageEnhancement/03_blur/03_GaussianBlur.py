'''
高斯滤波
'''

import cv2
import matplotlib.pyplot as plt

# 椒盐噪声
img01 = cv2.imread('../../../data/noise/sp_noise_lena.jpg')
# 高斯噪声
img02 = cv2.imread('../../../data/noise/gasuss_noise_lily_square.png')

rgb_sp = cv2.cvtColor(img01, cv2.COLOR_BGR2RGB)
rgb_g = cv2.cvtColor(img02, cv2.COLOR_BGR2RGB)

# 高斯滤波
res01 = cv2.GaussianBlur(rgb_sp,  # 图像
                         ksize=(21, 21),  # 核大小, 必须是正奇数
                         sigmaX=0)  # 水平方向上的标准差为0
res02 = cv2.GaussianBlur(rgb_g,  # 图像
                         ksize=(3,3),  # 核大小, 必须是正奇数
                         sigmaX=0)  # 水平方向上的标准差为0

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

plt.show()


# cv2.imshow('img', img02)
# cv2.imshow('g01', cv2.cvtColor(res01, cv2.COLOR_RGB2BGR))
# cv2.imshow('g10', cv2.cvtColor(res02, cv2.COLOR_RGB2BGR))

cv2.waitKey()
cv2.destroyAllWindows()
