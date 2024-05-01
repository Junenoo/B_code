'''
K最近邻分类
'''
import os
import cv2
import numpy as np
from sklearn.model_selection import train_test_split
from sklearn.metrics import confusion_matrix, classification_report

'''1、切分训练集和测试集'''
img_x = []
label_y = []
pixel_z = []

for i in range(11):
    for f in os.listdir('photo/%s' % i):
        img_x.append(['photo//' + str(i) + '//' + str(f)])
        label_y.append(i)
img_x = np.array(img_x)
label_y = np.array(label_y)

# 随机率为100%, 选取其中30%作为测试集
train_x, test_x, train_y, test_y = train_test_split(img_x, label_y,
                                                    test_size=0.3,
                                                    random_state=1)

'''2、图像读取及转换为像素直方图'''
# 训练集
train_xx = []
for i in train_x:
    # 读取图像
    img = cv2.imread(i)
    # 图像像素大小一致
    img = cv2.resize(img, (256, 256),
                     interpolation=cv2.INTER_CUBIC)
    # 计算图像直方图并储存至X数组
    hist = cv2.calcHist([img], [0, 1], None, [256, 256], [0.0, 255.0, 0.0, 255.0])
    train_xx.append(((hist / 255).flatten()))

# 测试集
test_xx = []
for i in test_x:
    img = cv2.imread(i)
    # 图像像素大小一致
    img = cv2.resize(img, (256, 256),
                     interpolation=cv2.INTER_CUBIC)
    # 计算图像直方图并储存至X数组
    hist = cv2.calcHist([img], [0, 1], None, [256, 256], [0.0, 255.0, 0.0, 255.0])
    test_xx.append(((hist / 255).flatten()))

'''3、基于KNN的图像分类处理'''
from sklearn.neighbors import KNeighborsClassifier

clf = KNeighborsClassifier(n_neighbors=11)
clf.fit(train_xx, test_y)
pred_y = clf.predict(test_xx)

# 打印预测结果
print(f'预测结果\n{pred_y}')
print(f'算法评价\n{classification_report(test_y, pred_y)}')

# 输出前十幅图像及预测结果
k = 0
while k < 10:
    print(test_x[k])
    img = cv2.imread(test_x[k])
    print(pred_y[k])
    cv2.imshow('img', img)
    cv2.waitKey()
    cv2.destroyAllWindows()
    k += 1
