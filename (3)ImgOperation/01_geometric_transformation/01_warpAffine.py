'''
仿射变换（Affine Transformation）其实是另外两种简单变换的叠加：线性变换、平移变换
仿射变换变化包括缩放Scale/平移transform/旋转rotate/反射reflection,对图形照镜子/错切shear mapping，感觉像是一个图形的倒影
原来的直线仿射变换后还是直线，原来的平行线经过仿射变换之后还是平行线，这就是仿射
仿射变换中集合中的一些性质保持不变：
（1）凸性
（2）共线性：若几个点变换前在一条线上，则仿射变换后仍然在一条线上
（3）平行性：若两条线变换前平行，则变换后仍然平行
（4）共线比例不变性：变换前一条线上两条线段的比例，在变换后比例不变
'''
import numpy as np
import cv2


def slope(img):
    '''
    倾斜
    cv2.getAffineTransform()通过找原图像中三个点的坐标和变换图像的相应三个点坐标,创建一个2X3的矩阵。
    cv2.getAffineTransform(pts1 , pts2):
    函数作用:构建变换矩阵
    pts1:原图像三个点的坐标
    pts2:原图像三个点在变换后相应的坐标

    :param img: 原图像
    :return: 倾斜后的图形
    '''
    h, w = img.shape[:2]
    # 仿射变换矩阵
    pos1 = np.float32([[0, 0], [512, 0], [512, 512]])
    pos2 = np.float32([[500, 500], [512, 0], [50, 50]])
    M = cv2.getAffineTransform(pos1, pos2)
    # 图像仿射变换
    res = cv2.warpAffine(img,
                         M,
                         (w, h))
    return res


def translate(img, x, y):
    '''
    平移
    数学表达式：x1=x0+△x, y1=y0+△y（△x、 △y平移量）
                          ((1  0  0)
    (x1 y1 1) = (x0 y0 1)  (0  1  0)
                           (△x △y 1))
    :param img: 原图像
    :param x: 水平方向位移
    :param y: 垂直方向位移
    :return: 平移后的图像
    '''
    h, w = img.shape[:2]
    M = np.float32([
        [1, 0, x],
        [0, 1, y]
    ])
    res = cv2.warpAffine(img,
                         M,  # 平移矩阵
                         (w, h))  # 输出图像的尺寸
    return res


def rotate(img, angle, center=None):
    '''
    旋转
    (x0,y1)旋转到(x1,y1)的过程, (m,n)旋转中心, α旋转角度, (left, top)旋转后左上角坐标
                          ((1  0   0)  ((cosα -sinα 0)   (( 1    0    0)
    (x1 y1 1) = (x0 y0 1)  (0  -1  0)   (sinα  cosα 0)    ( 0   -1    0)
                           (-m n  1))   ( 0      0  1))   (left top   1))
    :param img: 原图像
    :param angle: 旋转角度
    :param center: 旋转中心
    :return: 旋转后的图像
    '''
    h, w = img.shape[:2]
    if center is None:
        center = (w / 2, h / 2)
    M = cv2.getRotationMatrix2D(center, angle, scale=1.0)
    res = cv2.warpAffine(img,
                         M,
                         (w, h))
    return res


if __name__ == '__main__':
    # img = cv2.imread('../../../data/black_white_img1.png')
    img = cv2.imread('../../../data/lena.jpg')
    print(img.shape,
          img.size,
          img.dtype,
          sep='\n')
    cv2.imshow('img', img)

    slp = slope(img)  # 倾斜
    cv2.imshow('slope', slp)

    rot = rotate(img, 45)  # 旋转
    tslt = translate(rot, 50, -50)  # 平移
    cv2.imshow('rot', rot)
    cv2.imshow('translate', tslt)

    cv2.waitKey()
    cv2.destroyAllWindows()
