import cv2
import numpy as np
from glob import glob
import random

data = glob("D:\\dataset\\bw\img\\*.jpg")
count = 30041

for imname in data:

    cimg = cv2.imread(imname, 1)
    realme = cv2.resize(cimg, (256, 256))
    cimg = cv2.resize(cimg, (256, 256))
    realimg = cimg
    # 转换为线稿
    img_gray_inv = 255 - cimg
    # ksize太小的话线容易看不清
    img_blur = cv2.GaussianBlur(img_gray_inv, ksize=(9, 9),
                                sigmaX=0, sigmaY=0)

    img_blend = cv2.divide(cimg, 255 - img_blur, scale=256)
    img_blend = cv2.cvtColor(img_blend, cv2.COLOR_BGR2GRAY)
    # 转3通道，不然拼接不了
    img_blend = cv2.merge([img_blend, img_blend, img_blend])

    for num in range(50):
        r = 15
        x = random.randint(0, 256 - r)
        y = random.randint(0, 256 - r)
        for xnum in range(x, x + r):
            for ynum in range(y, y + r):
                realimg[xnum, ynum] = (255, 255, 255)

    blur = cv2.GaussianBlur(cimg, (125,125), 0)

    # 两张图片叠加，设置权重
    dst = cv2.addWeighted(img_blend, 0.6, blur, 0.4, 0)

    concat_img = np.concatenate((realme, dst), axis=1)

    count = count + 1

    # cv2.imshow("",concat_img)
    # cv2.waitKey()

    print(count)

    # if (count <= 4):
    #     cv2.imwrite('D:\\dataset\\test\\' + str(count)+'.jpg', concat_img)
    # # elif (count > 4000) & (count <= 4020):
    # #     cv2.imwrite('D:\\Pix2pix\\dataset\\comic\\test\\' + str(count)+'.jpg', concat_img)
    # # elif count > 4000:
    # #     cv2.imwrite('D:\\dataset\\bigtrain\\' + str(count)+'.jpg', concat_img)
    # else:
    #     pass


    cv2.imwrite('D:\\dataset\\bw\\train\\' + str(count)+'.jpg', concat_img)
