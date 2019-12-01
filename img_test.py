import cv2
import random
import numpy as np
from glob import glob
# from test_model import *


touming=cv2.imread("C:\\Users\\chenz\\Desktop\\1sketac.jpg")
touming=cv2.resize(touming,(256,256))
cimg=cv2.imread("C:\\Users\\chenz\\Desktop\\test.jpg")
cimg=cv2.resize(cimg,(256,256))

# 转换为线稿
img_gray_inv = 255 - cimg
# ksize太小的话线容易看不清
img_blur = cv2.GaussianBlur(img_gray_inv, ksize=(9, 9),
                            sigmaX=0, sigmaY=0)

img_blend = cv2.divide(cimg, 255 - img_blur, scale=256)
img_blend = cv2.cvtColor(img_blend, cv2.COLOR_BGR2GRAY)
# 转3通道，不然拼接不了
img_blend = cv2.merge([img_blend, img_blend, img_blend])


# for num in range(50):
#     r=15
#     x = random.randint(0, 256-r)
#     y = random.randint(0, 256-r)
#     for xnum in range(x, x + r):
#         for ynum in range(y, y + r):
#             cimg[xnum, ynum] = (255, 255, 255)

# 高斯模糊
blur=cv2.GaussianBlur(touming,(125,125),0)


dst=cv2.addWeighted(img_blend,0.6,blur,0.4,0)

# 图片拼接
concat_img = np.concatenate((cimg, dst), axis=1)

# cv2.imshow("",concat_img)

cv2.imwrite("D:\\Pix2pix\\dataset\\comic\\val\\1sketac.jpg",concat_img)
# cv2.imshow("",blur)
cv2.waitKey()

# load_uploadpic(dst,"test")