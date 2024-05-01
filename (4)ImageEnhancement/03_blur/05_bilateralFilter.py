'''
双边滤波
'''

import cv2
import matplotlib.pyplot as plt

# 椒盐噪声
img01 = cv2.imread('../../../data/noise/sp_noise_0.01_lena.jpg')
# 脉冲噪声
img02 = cv2.imread('../../../data/noise/pulse_noise_lena.jpg')
# 高斯噪声
img03 = cv2.imread('../../../data/noise/gasuss_noise_lena.jpg')

rgb_sp = cv2.cvtColor(img01, cv2.COLOR_BGR2RGB)
rgb_p = cv2.cvtColor(img02, cv2.COLOR_BGR2RGB)
rgb_g = cv2.cvtColor(img03, cv2.COLOR_BGR2RGB)

# 双边滤波
res01 = cv2.bilateralFilter(rgb_sp,  # 图像
                            d=5,  # 过滤期间使用的每个像素邻域的直径
                            sigmaColor=200,  # 颜色空间的而标准方差
                            sigmaSpace=200)  # 坐标空间的而标准方差
res02 = cv2.bilateralFilter(rgb_p,  # 图像
                            d=100,  # 过滤期间使用的每个像素邻域的直径
                            sigmaColor=100,  # 颜色空间的而标准方差
                            sigmaSpace=100)  # 坐标空间的而标准方差
res03 = cv2.bilateralFilter(rgb_g,  # 图像
                            d=50,  # 过滤期间使用的每个像素邻域的直径
                            sigmaColor=50,  # 颜色空间的而标准方差
                            sigmaSpace=50)  # 坐标空间的而标准方差

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


cv2.imshow('img1', img01)
cv2.imshow('img2', img02)
cv2.imshow('img3', img03)
cv2.imshow('m01', cv2.cvtColor(res01, cv2.COLOR_RGB2BGR))
cv2.imshow('m02', cv2.cvtColor(res02, cv2.COLOR_RGB2BGR))
cv2.imshow('m03', cv2.cvtColor(res03, cv2.COLOR_RGB2BGR))

cv2.waitKey()
cv2.destroyAllWindows()
