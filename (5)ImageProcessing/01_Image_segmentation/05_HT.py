'''
霍夫变换(HT)
'''

import cv2
import numpy as np
import matplotlib.pyplot as plt

'''========================霍夫变换检测直线========================'''


def line(img01, edges01):
    # 转换为二值图像
    '''大于threshold2的称为强边界。
        threshold1和threshold2之间的为弱边界。
        如果只有强边界，那么边界可能断断续续,而且会少分割.
        所以弱边界的作用就是解决上面这个问题.
        如果强边界点的8连通区域内有弱边界点，那么认为该弱边界点为强边界.
    '''
    # threshold1 低阈值，常取高阈值的0.2或者0.3
    # threshold2 高阈值

    lines = cv2.HoughLines(edges01,
                           1,  # r 以像素为单位的累加器的距离精度
                           np.pi / 180,  # 以像素为单位的累加器的角度精度
                           10)  # 累加平面的阈值参数，识别某部分为图中的一条直线时它在累加平面必须达到的值,大于该直线段才能被检测返回
    print('lines\n', lines)
    # 转化为二维
    # line = lines[:, 0, :]
    line = lines[:, 0, :]
    print('line\n  距离          角度\n', line)

    # 检测到的线在极坐标中绘制
    for rho, theta in line[:]:
        a = np.cos(theta)
        b = np.sin(theta)
        x0 = a * rho
        y0 = b * rho

        x1 = int(x0 + 1000 * (-b))
        y1 = int(y0 + 1000 * (a))
        x2 = int(x0 - 1000 * (-b))
        y2 = int(y0 - 1000 * (a))
        print('--', x0, y0, x1, y1, x2, y2, '--')

        # 绘制直线
        cv2.line(img01, (x1, y1), (x2, y2), (255, 0, 0), 1)

    res = cv2.cvtColor(img01, cv2.COLOR_GRAY2BGR)

    titles = ['a)gray', 'b)Canny', 'c)line_HT']
    imgs = [gray, edges01, res]
    for i in range(len(imgs)):
        plt.subplot(1, len(imgs), i + 1)
        plt.title(titles[i])
        plt.imshow(imgs[i])
        plt.axis('off')
    # plt.show()
    return img01


'''========================霍夫变换检测直线========================'''


def lineP(img03, edges01):
    # 转换为二值图像
    '''大于threshold2的称为强边界。
        threshold1和threshold2之间的为弱边界。
        如果只有强边界，那么边界可能断断续续,而且会少分割.
        所以弱边界的作用就是解决上面这个问题.
        如果强边界点的8连通区域内有弱边界点，那么认为该弱边界点为强边界.
    '''
    # threshold1 低阈值，常取高阈值的0.2或者0.3
    # threshold2 高阈值

    lines = cv2.HoughLinesP(edges01,
                            1,  # r 以像素为单位的累加器的距离精度
                            np.pi / 180,  # 以像素为单位的累加器的角度精度
                            10,  # 累加平面的阈值参数，识别某部分为图中的一条直线时它在累加平面必须达到的值,大于该直线段才能被检测返回
                            minLineLength=10,  # 最低线段的长度,比这个设定参数短的线段不能显示出来
                            maxLineGap=5  # 允许将同一点与点之间连接起来的最大距离
                            )
    print('lines\n', lines)
    # 转化为二维
    # line = lines[:, 0, :]
    line = lines[:, 0, :]
    print('line\n  距离          角度\n', line)

    # 绘制直线
    for x1, y1, x2, y2 in line[:]:
        cv2.line(img03, (x1, y1), (x2, y2), (255, 0, 0), 1)

    res = cv2.cvtColor(img03, cv2.COLOR_GRAY2BGR)

    titles = ['a)gray', 'b)Canny', 'c)lineP_HT']
    imgs = [gray, edges01, res]
    for i in range(len(imgs)):
        plt.subplot(1, len(imgs), i + 1)
        plt.title(titles[i])
        plt.imshow(imgs[i])
        plt.axis('off')
    # plt.show()
    return img03


'''========================霍夫变换检测圆========================'''


def circle(img02, edges01):
    # circles01 = cv2.HoughCircles(gray,
    #                              dp=1,  # 用来检测圆心的累加器与图像的分辨率输入图像之比的倒数,允许创建一个比输入图像分辨率低的累加器
    #                              minDist=10,  # 霍夫变换检测到的圆与圆心之间最小的距离
    #                              method=cv2.HOUGH_GRADIENT,
    #                              param2=24,  # 参数method设置检测方法的对应参数, 对当前唯一的方法霍夫提低发,它表示检测阶段圆心的累加器阈值,越小,将检测到更多不存在的圆,
    #                              maxRadius=8
    #                              )
    # circles01 = cv2.HoughCircles(gray,
    #                              dp=1,  # 用来检测圆心的累加器与图像的分辨率输入图像之比的倒数,允许创建一个比输入图像分辨率低的累加器
    #                              minDist=60,  # 霍夫变换检测到的圆与圆心之间最小的距离
    #                              method=cv2.HOUGH_GRADIENT,
    #                              param2=15,  # 参数method设置检测方法的对应参数, 对当前唯一的方法霍夫提低发,它表示检测阶段圆心的累加器阈值,越小,将检测到更多不存在的圆,
    #                              maxRadius=50
    #                              )
    circles01 = cv2.HoughCircles(edges01,
                                 dp=1,  # 用来检测圆心的累加器与图像的分辨率输入图像之比的倒数,允许创建一个比输入图像分辨率低的累加器
                                 minDist=45,  # 霍夫变换检测到的圆与圆心之间最小的距离
                                 method=cv2.HOUGH_GRADIENT,
                                 param2=35,  # 参数method设置检测方法的对应参数, 对当前唯一的方法霍夫提低发,它表示检测阶段圆心的累加器阈值,越小,将检测到更多不存在的圆,
                                 minRadius=45,
                                 # maxRadius=200
                                 )
    circles = circles01[0, :, :]
    # 取整四舍五入
    circles = np.uint16(np.round(circles))

    # 绘制圆
    for i in circles[:]:
        cv2.circle(img02, (i[0], i[1]), i[2], (255, 0, 0), 3)
        cv2.circle(img02, (i[0], i[1]), 2, (255, 0, 255), 5)
    res = cv2.cvtColor(img02, cv2.COLOR_GRAY2BGR)
    gray02 = cv2.cvtColor(gray, cv2.COLOR_GRAY2RGB)
    # 显示
    titles02 = ['a)gray', 'b)circle_HT']
    imgs02 = [gray02, res]
    for i in range(len(imgs02)):
        plt.subplot(1, len(imgs02), i + 1)
        plt.title(titles02[i])
        plt.imshow(imgs02[i])
    # plt.show()
    return img02


if __name__ == '__main__':
    file = '../../../data/tea.jpg'
    img = cv2.imread(file)
    # print(lena,lily,face)

    # 显示ROI区域（ROI: 感兴趣区域）
    roi = img[50:, 180:]
    cv2.imshow('roi', roi)
    gray = cv2.cvtColor(roi, cv2.COLOR_BGR2GRAY)
    blur = cv2.GaussianBlur(gray, (17,15), sigmaX=3)
    edges01 = cv2.Canny(blur,
                        10,
                        150)
    cv2.imshow('canny', edges01)
    img1 = gray.copy()
    img2 = gray.copy()
    img3 = gray.copy()
    c = circle(img1, edges01)
    # l = line(img2,edges01)
    lp = lineP(img3, edges01)

    cv2.imshow('c', c)
    # cv2.imshow('l', l)
    cv2.imshow('lp', lp)

    cv2.waitKey()
    cv2.destroyAllWindows()
