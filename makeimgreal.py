import cv2



img=cv2.imread("C:\\Users\\chenz\\Desktop\\191102170309.png")

# blur=cv2.blur(img,(5,5))
#
# # blur = cv2.bilateralFilter(img,9,75,75)
#
# gaussian =cv2.GaussianBlur(img,(5,5),1)
#
# dst=cv2.addWeighted(img,0.4,gaussian,0.6,0)
#
# d=cv2.bilateralFilter(src=img,d=0, sigmaColor=10 , sigmaSpace=15)

img=cv2.resize(img,(512,512),interpolation=cv2.INTER_BITS2)

img2=cv2.resize(img,(256,256),interpolation=cv2.INTER_BITS2)

cv2.imshow("",img)

cv2.imwrite("test.jpg",img)

cv2.waitKey()




# load_uploadpic(dst,"test")