'''
k-means聚类量化处理
'''

import cv2
import numpy as np
import matplotlib.pyplot as plt
file='../../../data/albums/cy.png'
img = cv2.imread(file)
h,w=img[:2]
# img=cv2.resize(img,None, fx=0.3, fy=0.3)
cv2.imshow('lena', img)

# 二维转化为一维
data = img.reshape((-1, 3))
data = np.float32(data)

'''
定义中心(type, max_iter, epsilon)
criteria：迭代停止的模式选择,这是一个含有三个元素的元组型数. 格式为（type, max_iter, epsilon） 
type: 
    cv2.TERM_CRITERIA_EPS：精确度（误差）满足epsilon，则停止。
    cv2.TERM_CRITERIA_MAX_ITER：迭代次数超过max_iter，则停止。
    cv2.TERM_CRITERIA_EPS+cv2.TERM_CRITERIA_MAX_ITER：两者结合，满足任意一个结束。
'''
criteria = (cv2.TERM_CRITERIA_EPS + cv2.TERM_CRITERIA_MAX_ITER,  # type
            10,  # max_iter
            0.1)  # epsilon

'''
设置标签
flags：初始中心选择，可选以下两种：
cv2.KMEANS_PP_CENTERS：使用kmeans++算法的中心初始化算法，即初始中心的选择使眼色相差最大.
cv2.KMEANS_RANDOM_CENTERS：每次随机选择初始中心（Select random initial centers in each attempt.）
'''
flags = cv2.KMEANS_RANDOM_CENTERS

# KMeans聚类分为四类
'''
compactness：紧密度, 返回每个点到相应重心的距离的平方和
labels：结果标记，每个成员被标记为分组的序号 如 0,1,2,3,4...等
centers：由聚类的中心组成的数组
'''
compactness, \
labels, \
centers = cv2.kmeans(data=data,
                     K=6,
                     bestLabels=None,
                     criteria=criteria,
                     attempts=20,  # attempts：重复试验kmeans算法次数，将会返回最好的一次结果
                     flags=flags)
print(f'compactness:{compactness}\nlabels:{labels}\ncenters: {centers}')
# 图像转为二维
centers = np.uint8(centers)
res = centers[labels.flatten()]
dst = res.reshape((img.shape))
cv2.imshow('img_rgb', img)
cv2.imshow('dst_rgb', dst)

# 转为rgb
img = cv2.cvtColor(img, cv2.COLOR_BGR2RGB)
# dst = cv2.cvtColor(dst, cv2.COLOR_BGR2RGB)

# plt.rcParams['font.sans-serif'] = ['SimHei']
# titles = [u'(a)原始图像', u'(b)聚类量化K=4']
# imgs = [img, dst]
# plt.figure('Img show')
# for i in range(2):
#     plt.subplot(2, 5, i + 1)
#     plt.imshow(imgs[i].astype('int32'))
#     plt.title(titles[i])
#     plt.xticks([])
#     plt.yticks([])
#
# plt.tight_layout()
# plt.show()
i = file.rsplit('/', 1)[1]
# cv2.imwrite(i, dst)
# cv2.imwrite(i, canny02)
print('写入成功')
cv2.waitKey()
cv2.destroyAllWindows()
