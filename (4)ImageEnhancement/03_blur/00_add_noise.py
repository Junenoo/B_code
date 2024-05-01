import numpy as np
import random
import cv2
from matplotlib import pyplot as plt
import os


def sp_noise(image, prob):
    '''
    添加椒盐噪声
    prob:噪声比例
    '''
    output = np.zeros(image.shape, np.uint8)
    thres = 1 - prob
    for i in range(image.shape[0]):
        for j in range(image.shape[1]):
            rdn = random.random()
            if rdn < prob:
                output[i][j] = 0
            elif rdn > thres:
                output[i][j] = 255
            else:
                output[i][j] = image[i][j]
    return output


def pulse_noise(image, prob):
    '''
    添加脉冲噪声
    prob:噪声比例
    '''
    output = np.zeros(image.shape, np.uint8)
    thres = 1 - prob
    for i in range(image.shape[0]):
        for j in range(image.shape[1]):
            rdn = random.random()
            if rdn < prob or rdn > thres:
                output[i][j] = random.randint(0, 256)
            else:
                output[i][j] = image[i][j]
    return output


def gasuss_noise(image, mean=0, var=0.001):
    '''
        添加高斯噪声
        mean : 均值
        var : 方差
    '''
    image = np.array(image / 255, dtype=float)
    noise = np.random.normal(mean, var ** 0.67, image.shape)
    out = image + noise
    if out.min() < 0:
        low_clip = -1.
    else:
        low_clip = 0.
    out = np.clip(out, low_clip, 1.0)
    out = np.uint8(out * 255)
    # cv.imshow("gasuss", out)
    return out


# Read image
file = '../../../data/lena.jpg'
img = cv2.imread(file)
# 添加椒盐噪声，噪声比例为 0.02
out1 = sp_noise(img, prob=0.01)
# 添加脉冲，噪声比例为 0.02
out2 = pulse_noise(img, prob=0.1)
# 添加高斯噪声，均值为0，方差为0.001
out3 = gasuss_noise(img, mean=0, var=0.06)

# 保存图像
file_path = file.rsplit('/', 1)
# cv2.imwrite(''.join(f'{file_path[0]}/noise/sp_noise_0.01_{file_path[1]}'), out1)
# cv2.imwrite(''.join(f'{file_path[0]}/noise/pulse_noise_{file_path[1]}'), out2)
cv2.imwrite(''.join(f'{file_path[0]}/noise/gasuss_noise_{file_path[1]}'), out3)
# print(f"文件写入成功：{''.join(f'{file_path[0]}/noise/sp_noise_0.01_{file_path[1]}')}")
# print(f"文件写入成功：{''.join(f'{file_path[0]}/noise/pulse_noise_{file_path[1]}')}")
print(f"文件写入成功：{''.join(f'{file_path[0]}/noise/gasuss_noise_{file_path[1]}')}")

# 显示图像
plt.figure(1)
plt.subplot(141)
plt.axis('off')  # 关闭坐标轴
plt.title('Original')
plt.imshow(cv2.cvtColor(img, cv2.COLOR_BGR2RGB))

plt.subplot(142)
plt.axis('off')
plt.title('Salt and Pepper')
plt.imshow(cv2.cvtColor(out1, cv2.COLOR_BGR2RGB))

plt.subplot(143)
plt.axis('off')
plt.title('Pulse')
plt.imshow(cv2.cvtColor(out2, cv2.COLOR_BGR2RGB))

plt.subplot(144)
plt.axis('off')
plt.title('Gaussian')
plt.imshow(cv2.cvtColor(out3, cv2.COLOR_BGR2RGB))
plt.show()
