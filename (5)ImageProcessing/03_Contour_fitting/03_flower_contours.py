import cv2
import numpy as np
import os


def extract_red():
    '''
        提取红色
    :return: 提取红色的图像
    '''
    global red
    hsv = cv2.cvtColor(im, cv2.COLOR_BGR2HSV)
    # =============指定红色值的范围=============
    minRed01 = np.array([0, 70, 70])
    maxRed01 = np.array([5, 255, 255])
    minRed02 = np.array([170, 70, 70])
    maxRed02 = np.array([180, 255, 255])
    # 确定红色区域
    mask01 = cv2.inRange(hsv, minRed01, maxRed01)
    mask02 = cv2.inRange(hsv, minRed02, maxRed02)
    mask = mask01 + mask02
    # 通过掩码控制的按位与运算，锁定红色区域
    red = cv2.bitwise_and(im, im, mask=mask)  # 执行掩模运算
    return red


def extract_contours(im, gray):
    '''
    提取图像轮廓
    :return: None
    '''

    # 二值化
    ret, binary = cv2.threshold(gray, 50, 255, cv2.THRESH_BINARY)
    # 模糊处理
    # img = cv2.GaussianBlur(binary, (3, 3), 0)
    img = cv2.medianBlur(binary,3)
    # 开运算
    kernel = cv2.getStructuringElement(cv2.MORPH_RECT, (3, 3))
    img = cv2.morphologyEx(img, cv2.MORPH_OPEN, kernel, iterations=2)
    # 提取轮廓
    img, contours, hierarchy = cv2.findContours(img,
                                                cv2.RETR_EXTERNAL,
                                                cv2.CHAIN_APPROX_NONE)
    cv2.imshow('medianBlur', img)

    # 方法一： 筛选、过滤小轮廓
    new_cnts = []  #  存放筛选后的轮廓
    for c in contours:  #  遍历所有轮廓
        area = cv2.contourArea(c)  # 计算面积
        cir_len = cv2.arcLength(c, True)  # 计算周长
        # print('周长：', cir_len)
        # print('面积：', area)
        if cir_len >= 500:  #  留下主要轮廓
            new_cnts.append(c)
    #
    #  对轮廓排序
    new_cnts = sorted(new_cnts,
                      key=cv2.contourArea,  # 排序依据：面积
                      reverse=True)  # 倒序排列
    # print(new_cnts)

    new_cnts = new_cnts[:len(new_cnts)]  # 取出主要轮廓
    # print(new_cnts)
    # #  绘制轮廓
    img_cnt = cv2.drawContours(im, new_cnts, -1, (0, 255, 255), 2)
    cv2.imshow("result", img_cnt)
    return im

    # 方法二（只提取一朵花）
    # adp = im.copy()
    # epsilon = 0.0001 * cv2.arcLength(contours[0], True)  # 精度,根据周长计算
    # approx = cv2.approxPolyDP(contours[0], epsilon, False)  # 构造多边形
    # adp = cv2.drawContours(adp, [approx], 0, (255, 0, 0), 2)  # 绘制多边形
    # print(contours)

    # cv2.imshow("result", adp)


if __name__ == '__main__':
    filename = "../../../data/flower.jpg"
    im = cv2.imread(filename)
    im = cv2.resize(im, (int(im.shape[1] / 5), int(im.shape[0] / 5)))
    cv2.imshow('original', im)

    # 提取红色
    red = extract_red()
    gray = cv2.cvtColor(red, cv2.COLOR_BGR2GRAY)
    cv2.imshow('red', red)

    # 提取轮廓
    img = extract_contours(im, gray)

    # 保存图像
    fn = filename.rsplit('/')[-1]
    if not os.path.exists('contours'):
        os.makedirs('contours')
    cv2.imwrite('contours/%s' % fn, img)
    print('写入成功')

    cv2.waitKey()
    cv2.destroyAllWindows()
