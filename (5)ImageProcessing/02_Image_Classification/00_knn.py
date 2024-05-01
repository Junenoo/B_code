import os
import numpy as np
from sklearn import preprocessing

text = ['the game was very forgettable', 'the clean but close election', 'a close but clean match',
        'it was a clean game', 'so forgettable was the election', 'so close was the match', 'it was the very election']
label = ['sports', 'not sports', 'sports', 'sports', 'not sports', 'sports', 'not sports']
pred_text = ['game game game game game', 'match match match match match']

text_num = ''
for i in text:
    text_num += i + ' '
text_num = text_num.split(' ')

# 训练的编码
enc01 = preprocessing.LabelEncoder()
text_enc = enc01.fit(text_num)
text_encode = []
for i in text:
    text_list = i.split(' ')
    # 标签编码
    text_list = text_enc.transform(text_list)
    text_encode.append(text_list)
text_encode = np.array(text_encode).reshape(len(text), 5)
# print('text_encode\n', text_encode)

# 标签的编码
enc02 = preprocessing.LabelEncoder()
label_encode = enc02.fit_transform(label)
# print('label_encode\n', label_encode)

# 预测的编码
pred_text_encode = []
# print('pred_text: ', pred_text)
for j in pred_text:
    pred_text_list = j.split(' ')
    pred_text_list = text_enc.transform(pred_text_list)
    pred_text_encode.append(pred_text_list)
pred_text_encode = np.array(pred_text_encode).reshape(2, 5)
# print('pred_text_encode\n', pred_text_encode)

'''使用knn分类器'''
from sklearn.neighbors import KNeighborsClassifier

knn = KNeighborsClassifier(n_neighbors=2)
knn.fit(text_encode, label_encode)
pred_label_encode = knn.predict(pred_text_encode)

# 打印预测结果
pred_label_decode = enc02.inverse_transform(pred_label_encode)
print(f'预测结果\n{pred_label_decode}')

# 查看概率
prob = knn.predict_proba(pred_text_encode)
pred_text_decode = enc01.inverse_transform(pred_text_encode[0])
# print('测试文本\n', pred_text_decode)
print(f'{pred_text[0]}不是体育概率 {prob[0][0]}\n'
      f'{pred_text[0]}是体育概率 {prob[0][1]}\n'
      f'{pred_text[1]}不是体育概率 {prob[1][0]}\n'
      f'{pred_text[1]}是体育概率 {prob[1][1]}')

# print('训练文本')
# for j in range(len(text_encode[0])):
#     text_decode = enc01.inverse_transform(text_encode[j])
#     print(text_decode)

label_decode = enc02.inverse_transform(label_encode)
# print('标签\n', label_decode)
