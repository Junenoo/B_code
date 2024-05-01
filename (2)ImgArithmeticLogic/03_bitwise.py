import cv2
import numpy as np

lena = cv2.imread('../../data/lena.jpg',0)
cv2.imshow('lena', lena)
h, w = lena.shape[:2]

zeros = np.zeros((h, w), dtype='uint8')
circle = cv2.circle(zeros, (int(h / 2), int(w / 2)), 80, (255, 255, 255), -1)
cv2.imshow('circle', circle)

print(lena.shape, circle.shape)

# 与运算(黑为0 白为1)
res01 = cv2.bitwise_and(lena, circle)
cv2.imshow('and', res01)
# 或运算(黑为0 白为1 对应白色像素原图加255)
res02 = cv2.bitwise_or(lena, circle)
cv2.imshow('or', res02)
# 非运算（255-）
res03 = cv2.bitwise_not(lena)
cv2.imshow('not', res03)
# 异或运算
res04 = cv2.bitwise_xor(lena, circle)
cv2.imshow('xor', res04)

cv2.waitKey()
cv2.destroyAllWindows()
