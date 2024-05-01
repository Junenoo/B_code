import cv2
import numpy as np

lena = cv2.imread('../../data/lena.jpg')
lily = cv2.imread('../../data/lily_square.png')

# np.shape(lena)[0]: h      np.shape(lena)[1]: w
lily = cv2.resize(lily, (np.shape(lena)[1], np.shape(lena)[0]))  # 两张图大小要一致

add01 = cv2.add(lena, lily)  # 像素叠加
cv2.imshow('add', add01)

add02 = cv2.addWeighted(lena, 0.8,
                        lily, 0.2,
                        50)  # 像素加权叠加后 + 50
cv2.imshow('addWeighted', add02)

cv2.waitKey()
cv2.destroyAllWindows()
