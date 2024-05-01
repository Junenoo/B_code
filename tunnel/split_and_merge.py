'''
      通道拆分与合并
'''
import cv2

img = cv2.imread('../../data/lena.jpg')
print(f'shape: {img.shape}',
      f'img.size: {img.size}',
      f'dtype: {img.dtype}', sep='\n')

'''    拆分通道    '''
# bgr
b, g, r = cv2.split(img)
cv2.imshow('img', img)
# hsv
hsv = cv2.cvtColor(img, cv2.COLOR_BGR2HSV)
h, s, v = cv2.split(hsv)  # h:色调 s:饱和度 v:亮度
cv2.imshow('b: ', b)
cv2.imshow('g: ', g)
cv2.imshow('r: ', r)
cv2.imshow('h: ', h)
cv2.imshow('s: ', s)
cv2.imshow('v: ', v)

'''    合并通道    '''
# bgr
bgr_merge = cv2.merge([b, g, r])
cv2.imshow('bgr_merge', bgr_merge)
cv2.imwrite('bgr.bmp', bgr_merge)
# hsv
hsv_merge = cv2.merge([h, s, v])
bgr = cv2.cvtColor(hsv_merge, cv2.COLOR_HSV2BGR)
cv2.imshow('bgr', bgr)
cv2.imwrite('bgr1.bmp', bgr)


cv2.waitKey()
cv2.destroyAllWindows()
