import numpy as np
import cv2
import os
import random

file = ['../../../data/Linus.png']
output = 'Linus-wu.png'

for file_img in file:
    # 打开图像
    img = cv2.imread(file_img)
    mask_img = cv2.imread(file_img)

    # 雾的颜色
    mask_img[:, :] = (166, 178, 180)

    # 里面参数可调，主要调整雾的浓度
    image = cv2.addWeighted(img,
                            round(random.uniform(0.03, 0.28), 2),
                            mask_img, 1, 0)
    cv2.imshow('wu', image)

    cv2.waitKey()
    cv2.destroyAllWindows()
    # 保存的文件夹
    # cv.imwrite(output, image)
