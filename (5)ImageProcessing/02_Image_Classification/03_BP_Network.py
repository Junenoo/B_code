'''
误差反向传播（Back-propagation, BP）算法
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
from sklearn.preprocessing import LabelBinarizer
import random


def logistic(x):
    '''
    logistic函数也是神经网络最为常用的激活函数，即sigmoid函数
    :param x:
    :return:
    '''
    return 1 / (1 + np.exp(-x))


def logistic_derivative(x):
    return logistic(x) * (1 - logistic(x))
