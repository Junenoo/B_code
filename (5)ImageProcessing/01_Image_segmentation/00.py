import cv2
import numpy as np
import matplotlib.pyplot as plt

'''全白全黑图像'''
# black_img = np.zeros((512, 512), dtype='uint8')
# white_img = np.zeros((512, 512), dtype='uint8')
b = np.zeros((512, 512), dtype='uint8')
g = np.zeros((512, 512), dtype='uint8')
r = np.zeros((512, 512), dtype='uint8')

b[:512//4,:] = 255
g[:512//4,:] = 255
r[:512//4,:] = 255
b[512//4 * 2:512//4*3,:] = 255
g[512//4 * 2:512//4*3,:] = 255
r[512//4 * 2:512//4*3,:] = 255
# g[512//4 - 10:512//4  + 10, 512//4  - 10:512//4  + 10] = 255
# r[512//4  - 10:512//4  + 10, 512//4  - 10:512//4  + 10] = 255

# for i in range(0,512,512//4):
#     b[512//4 - 10:512//4  + 10, 512//4  - 10:512//4  + 10] = 255
#     g[512//4 - 10:512//4  + 10, 512//4  - 10:512//4  + 10] = 255
#     r[512//4  - 10:512//4  + 10, 512//4  - 10:512//4  + 10] = 255
# b[:] = g[:] = r[:] = 127
bgr = cv2.merge([b, g, r])

cv2.imshow('gray', bgr)
# cv2.imwrite('../../../data/85.png', bgr)
cv2.imwrite('../../../data/black_white_img6.png', bgr)
print('写入成功')
cv2.waitKey()
cv2.destroyAllWindows()

'''1*1平铺3*3'''
# img = cv2.imread('../../../data/black_white_img2.png')
# img_rs = cv2.resize(img, (512, 512))
# cv2.imshow('img_rs', img_rs)
# # h, w = img_rs.shape
# # zeros = np.zeros((h * 3, w * 3), dtype=np.uint8)
# #
# # for zh in range(3):
# #     for zw in range(3):
# #         zeros[h * zh:h * (zh + 1), w * zw:w * (zw + 1)] = img_rs[:]
# #
# # cv2.imshow('i', img)
# # cv2.imshow('rs', zeros)
# cv2.imwrite('../../../data/black_white_img2.png', img_rs)
# cv2.waitKey()
# cv2.destroyAllWindows()
