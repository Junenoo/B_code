'''
Canny算子
'''

import cv2
import numpy as np
import matplotlib.pyplot as plt


def Canny(im, im_gray):
    #  1. 模糊
    im_blur = cv2.GaussianBlur(im_gray, (3,3), 0)
    #  2. 膨胀
    k = np.ones((3,3), np.uint8)  #  膨胀核
    im_dilate = cv2.dilate(im_blur, k)
    # cv2.imshow('dilate', im_dilate)

    #  边沿提取
    im_canny = cv2.Canny(im_dilate, 60, 240)  # 60,240需要自己调
    # cv2.imshow('Canny', im_canny)
    #
    #  提取轮廓(图像，轮廓数据，轮廓层级关系)
    img, cnts, hie = cv2.findContours(im_canny,
                                      cv2.RETR_LIST, # 所有轮廓
                                      cv2.CHAIN_APPROX_NONE)  # 存储轮廓所有的点

    # #  筛选、过滤小轮廓
    new_cnts = []  #  存放筛选后的轮廓
    for c in cnts:  #  遍历所有轮廓
        area = cv2.contourArea(c)  # 计算面积
        cir_len = cv2.arcLength(c, True) # 计算周长
        # print('周长：', cir_len)
        # print('面积：', area)
        if cir_len >= 1000:  #  留下
            new_cnts.append(c)
    #
    #  对轮廓排序
    new_cnts = sorted(new_cnts,
                      key=cv2.contourArea,  # 排序依据：面积
                      reverse=True)  # 倒序排列
    # print(new_cnts)
    new_cnts = new_cnts[1:2]  # 取出面积第二大的轮廓
    # print(new_cnts)
    # #  绘制轮廓
    red = (0, 0, 255)
    img_cnt = cv2.drawContours(im,  # 原图上操作
                               new_cnts,  # 轮廓信息
                               -1,  # 所有轮廓
                               red, 2)  # 轮廓颜色、粗细

    min_x, min_y = new_cnts[0][0][0][0], new_cnts[0][0][0][1]
    max_x, max_y = min_x, min_y
    #  遍历每个点，找出四个边沿坐标
    for cnt in new_cnts[0]:
        # print(cnt)
        x = cnt[0][0]
        y = cnt[0][1]

        if min_x >= x:
            min_x = x
        if min_y >= y:
            min_y = y
        if max_x <= x:
            max_x = x
        if max_y <= y:
            max_y = y
    #  中线
    center_y = int((min_y + max_y) / 2)
    #  cv2.line(im, (min_x,center_y),(min_x,center_y),red,2)
    #  上中线
    center_up_y = int((min_y + center_y) / 2)
    cv2.line(im, (min_x, center_up_y), (max_x, center_up_y), red, 2)
    #  下中线
    center_down_y = int((center_y + max_y) / 2)
    cv2.line(im, (min_x, center_down_y), (max_x, center_down_y), red, 2)
    cv2.imshow('im_lines', im)
    print('lines: ',min_x, center_up_y, center_down_y)

    #  求药丸轮廓上下中线交点
    cross_up = set()
    cross_down = set()

    for cnt in new_cnts[0]:
        x, y = cnt[0][0], cnt[0][1]
        if y == center_up_y:
            cross_up.add((x, y))  # 等于上中线y坐标，与上中线交点
        if y == center_down_y:
            cross_down.add((x, y))  # 等于下中线y坐标，与下中线交点
    cross_up = list(cross_up)
    cross_down = list(cross_down)

    #  绘制交点
    for p in cross_up:
        cv2.circle(im, (p[0], p[1]), 8, red, 2)  # 交点画小圆圈
    for p in cross_down:
        cv2.circle(im, (p[0], p[1]), 8, red, 2)  # 交点画小圆圈
    cv2.imshow('im_circle', im)


    return im_canny


if __name__ == '__main__':
    file = 'normal_1.png' #normal_1.png / unbalance1.png / unbalance2.png  #'../../../data/pic3.png'
    img = cv2.imread(file)
    gray_img = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)

    im_canny = Canny(img, gray_img)

    # 显示结果
    img = cv2.cvtColor(img,cv2.COLOR_BGR2RGB)
    imgs = [img, gray_img, im_canny]

    for i in range(len(imgs)):
        plt.subplot(1, len(imgs), i + 1)
        plt.imshow(imgs[i], 'gray')
        plt.axis('off')
    plt.show()




    cv2.waitKey()
    cv2.destroyAllWindows()
