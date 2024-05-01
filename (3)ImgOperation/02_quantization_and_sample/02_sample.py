'''
采样
'''
import cv2
import numpy as np
import matplotlib.pyplot as plt


def sampling(img, sp: int):
    '''
    采样
    :param img: 原图像
    :param sp: 采样区域, int
    :return: 采样后
    '''
    # 获取高宽
    h, w = img.shape[:2]
    # 采样转换为spxsp区域
    num_h, num_w = h // sp, w // sp
    # 创建空图
    res = np.zeros((h, w, 3), dtype='uint8')
    # 图像循环采样spxsp区域
    for i in range(sp):
        # 获取Y坐标
        y = i * num_h
        for j in range(sp):
            # 获取X坐标
            x = j * num_w
            # 获取填充颜色 左上角像素点
            b = img[y, x][0]
            g = img[y, x][1]
            r = img[y, x][2]

            # 循环设置小区域采样
            for n in range(num_h):
                for m in range(num_w):
                    res[y + n, x + m][0] = np.uint8(b)
                    res[y + n, x + m][1] = np.uint8(g)
                    res[y + n, x + m][2] = np.uint8(r)
    return res


if __name__ == '__main__':
    img = cv2.imread('../../../data/albums/sour.jpg')
    cv2.imshow('lena', img)
    print(img.shape)
    res = sampling(img, 8)
    cv2.imshow('Sampling', res)
    print('\t对应采样后图像像素值（选取对角线8个方块）',
          f'x:{0}~{0 + 512 / 8 - 1}, y:{0}~{0 + 512 / 8 - 1} 像素值:{img[0, 0]}',
          f'x:{0}~{0 + 512 / 8 - 1}, y:{0 + 512 / 8}~{512 / 8 * 2 - 1} 像素值:{img[0, int(512 / 8)]}',
          f'x:{0 + 512 / 8}~{512 / 8 * 2 - 1}, y:{0}~{0 + 512 / 8 - 1} 像素值:{img[int(512 / 8), 0]}',
          f'x:{0 + 512 / 8 * 1}~{512 / 8 * 2 - 1}, y:{0 + 512 / 8 * 1}~{512 / 8 * 2 - 1} 像素值:{img[int(512 / 8 * 1), int(512 / 8 * 1)]}',
          f'x:{0 + 512 / 8 * 2}~{512 / 8 * 3 - 1}, y:{0 + 512 / 8 * 2}~{512 / 8 * 3 - 1} 像素值:{img[int(512 / 8 * 2), int(512 / 8 * 2)]}',
          f'x:{0 + 512 / 8 * 3}~{512 / 8 * 4 - 1}, y:{0 + 512 / 8 * 3}~{512 / 8 * 4 - 1} 像素值:{img[int(512 / 8 * 3), int(512 / 8 * 3)]}',
          f'x:{0 + 512 / 8 * 4}~{512 / 8 * 5 - 1}, y:{0 + 512 / 8 * 4}~{512 / 8 * 5 - 1} 像素值:{img[int(512 / 8 * 4), int(512 / 8 * 4)]}',
          f'x:{0 + 512 / 8 * 5}~{512 / 8 * 6 - 1}, y:{0 + 512 / 8 * 5}~{512 / 8 * 6 - 1} 像素值:{img[int(512 / 8 * 5), int(512 / 8 * 5)]}',
          f'x:{0 + 512 / 8 * 6}~{512 / 8 * 7 - 1}, y:{0 + 512 / 8 * 6}~{512 / 8 * 7 - 1} 像素值:{img[int(512 / 8 * 6), int(512 / 8 * 6)]}',
          f'x:{0 + 512 / 8 * 7}~{512 / 8 * 8 - 1}, y:{0 + 512 / 8 * 7}~{512 / 8 * 8 - 1} 像素值:{img[int(512 / 8 * 7), int(512 / 8 * 7)]}',
          sep='\n')

    plt.subplot(1, 2, 1)
    plt.imshow(cv2.cvtColor(img, cv2.COLOR_BGR2RGB))
    plt.xticks([0, 64, 128, 192, 256, 320, 384, 448, 511])
    plt.yticks([0, 64, 128, 192, 256, 320, 384, 448, 511])
    plt.subplot(1, 2, 2)
    plt.imshow(cv2.cvtColor(res, cv2.COLOR_BGR2RGB))
    plt.xticks([0, 64, 128, 192, 256, 320, 384, 448, 511])
    plt.yticks([0, 64, 128, 192, 256, 320, 384, 448, 511])
    plt.tight_layout()
    plt.show()

    cv2.waitKey()
    cv2.destroyAllWindows()
