'''
直方图判断白天与黑夜
'''

import cv2
import numpy as np
import matplotlib.pyplot as plt


def func_judge(img):
    '''
    判断白天黑夜
    若低于50得1灰度值占整张画面大于等于80%则为黑夜，否则为白天
    :param img: 原图
    :return: None
    '''
    h, w = img.shape[:2]
    piexs_sum = h * w
    dark_sum = 0
    dark_prop = 0

    for i in range(h):
        for j in range(w):
            if img[i, j] < 70:
                dark_sum += 1
    dark_prop = dark_sum * 1.0 / piexs_sum
    if dark_prop < 0.75:
        print('白天')
    else:
        print('黑夜')
    print(dark_sum, piexs_sum,dark_prop )


if __name__ == '__main__':
    img = cv2.imread('../../../data/log02.jpg')
    # cv2.imshow('img', img)
    img_rgb = cv2.cvtColor(img, cv2.COLOR_BGR2RGB)
    img_gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
    # cv2.imshow('gray', img_gray)
    hist = cv2.calcHist([img_gray], channels=[0], mask=None, histSize=[256], ranges=[0, 255])

    # 判断白天黑夜
    func_judge(img_gray)

    plt.subplot(211)
    plt.title('color')
    plt.imshow(img_rgb)
    plt.subplot(212)
    plt.title('hist')
    plt.plot(hist, color='darkgray')

    plt.show()

    cv2.waitKey()
    cv2.destroyAllWindows()
