'''
Canny算子
'''

import cv2
import matplotlib.pyplot as plt


def Canny(gray_img, w=1):
    if w == 0:
        # 不进行高斯滤波
        input_img = gray_img
    if w == 1:
        # 高斯滤波
        gaussian = cv2.GaussianBlur(gray_img,
                                    ksize=(3,3),  # 高斯滤波器模板大小
                                    sigmaX=0)  # 高斯核函数在x方向的高斯内核标准差
        input_img = gaussian
    # Canny算子
    canny = cv2.Canny(input_img,
                      threshold1=130,  # TL>pixel => 0
                      threshold2=150)  # TH<pixel => 255

    return canny


if __name__ == '__main__':
    file = '../../../data/lena.jpg'
    img = cv2.imread(file)
    # img = cv2.resize(img,None,fx=0.3,fy=0.3)
    gray_img = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)


    canny01 = Canny(gray_img, 1)
    cv2.imshow('canny_with_gaussian', canny01)
    canny02 = Canny(gray_img, 0)
    # cv2.imshow('canny_with_non_gaussian', canny02)
    # i = file.rsplit('/', 1)[1]
    # cv2.imwrite(i, canny01)
    # cv2.imwrite(i, canny02)
    # print('写入成功')
    # 显示结果
    imgs = [gray_img, canny02, canny01]

    for i in range(len(imgs)):
        plt.subplot(1, len(imgs), i + 1)
        plt.imshow(imgs[i], 'gray')
        plt.axis('off')
    plt.show()

    cv2.waitKey()
    cv2.destroyAllWindows()
