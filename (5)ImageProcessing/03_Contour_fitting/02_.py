import cv2
import numpy as np
import matplotlib.pyplot as plt
im=cv2.imread('flower.png')
iim=cv2.imread('../../../data/flower2.jpg')
iim=cv2.resize(iim,(int(im.shape[1]),int(im.shape[0])))
cv2.imshow('img',im)

blur=cv2.medianBlur(im,25)
kernel = np.ones((2,2), np.uint8)
res = cv2.morphologyEx(im,
                       cv2.MORPH_OPEN,
                       kernel,
                       iterations=5)

cv2.imshow('open',res)
cv2.imshow('blur',blur)
gray01=cv2.cvtColor(res, cv2.COLOR_BGR2GRAY)
gray02=cv2.cvtColor(blur, cv2.COLOR_BGR2GRAY)
# 提取图像轮廓
ret, binary = cv2.threshold(gray02, 127, 255, cv2.THRESH_BINARY)
img, contours, hierarchy = cv2.findContours(binary,
                                            cv2.RETR_EXTERNAL,
                                            cv2.CHAIN_APPROX_NONE)
# 精度一
print(contours)
adp = iim.copy()
epsilon = 0.000001* cv2.arcLength(contours[0],True)  # 精度，根据周长计算
approx = cv2.approxPolyDP(contours[0], epsilon, False)  # 构造多边形
print(approx)
adp = cv2.drawContours(adp, [approx], 0, (0, 0, 255), 5)  # 绘制多边形
cv2.imshow("result_0.005", adp)


cv2.waitKey()
cv2.destroyAllWindows()