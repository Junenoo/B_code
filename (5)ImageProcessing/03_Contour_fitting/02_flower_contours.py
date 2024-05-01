    #  边沿提取
    im_canny = cv2.Canny(im_dilate, 60, 240)  # 60,240需要自己调
    # cv2.imshow('Canny_%s'%f_mame, im_canny)
    #
    #  提取轮廓(图像，轮廓数据，轮廓层级关系)
    img, cnts, hie = cv2.findContours(im_canny,
                                      cv2.RETR_LIST, # 所有轮廓
                                      cv2.CHAIN_APPROX_NONE)  # 存储轮廓所有的点
    #
    # #  筛选、过滤小轮廓
    new_cnts = []  #  存放筛选后的轮廓
    for c in cnts:  #  遍历所有轮廓
        area = cv2.contourArea(c)  # 计算面积
        cir_len = cv2.arcLength(c, True) # 计算周长
        # print('周长：', cir_len)
        # print('面积：', area)
        if cir_len >= 1000:  #  留下
            new_cnts.append(c)
    #
    #  对轮廓排序
    new_cnts = sorted(new_cnts,
                      key=cv2.contourArea,  # 排序依据：面积
                      reverse=True)  # 倒序排列
    # print(new_cnts)
    new_cnts = new_cnts[1:2]  # 取出面积第二大的轮廓
    # print(new_cnts)
    # #  绘制轮廓
    red = (0, 0, 255)
    img_cnt = cv2.drawContours(im,  # 原图上操作
                               new_cnts,  # 轮廓信息
                               -1,  # 所有轮廓
                               red, 2)  # 轮廓颜色、粗细