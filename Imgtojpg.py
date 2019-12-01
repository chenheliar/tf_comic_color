import cv2
from glob import glob

data = glob("D:\\Deep-Learning-21-Examples\\chapter_9\dataset\\colorlization\\anime_resized\\train\\*")

count = 0

for imname in data:
    cimg=cv2.imread(imname,1)
    count=count+1
    print(count)
    cv2.imwrite('D:\\dataset\\bw\img\\'+str(count)+'.jpg',cimg)

