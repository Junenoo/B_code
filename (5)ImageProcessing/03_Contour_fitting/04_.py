# 构建多边形，逼近轮廓
import cv2
import numpy as np

im = cv2.imread("../../../data/89.png")
cv2.imshow("im", im)
gray = cv2.cvtColor(im, cv2.COLOR_BGR2GRAY)

# 提取图像轮廓
ret, binary = cv2.threshold(gray, 127, 255, cv2.THRESH_BINARY)
img, contours, hierarchy = cv2.findContours(binary,
                                            cv2.RETR_LIST,
                                            cv2.CHAIN_APPROX_NONE)
# 精度一
adp = im.copy()
epsilon = 0.005 * cv2.arcLength(contours[0], True)  # 精度，根据周长计算
approx = cv2.approxPolyDP(contours[0], epsilon, True)  # 构造多边形
adp = cv2.drawContours(adp, [approx], 0, (0, 0, 255), 2)  # 绘制多边形
cv2.imshow("result_0.005", adp)
# 精度二
adp2 = im.copy()
epsilon = 0.1 * cv2.arcLength(contours[0], True)  # 精度，根据周长计算
approx = cv2.approxPolyDP(contours[0], epsilon, True)  # 构造多边形
adp = cv2.drawContours(adp2, [approx], 0, (0, 0, 255), 2)  # 绘制多边形
cv2.imshow("result_0.01", adp2)

cv2.waitKey()
cv2.destroyAllWindows()