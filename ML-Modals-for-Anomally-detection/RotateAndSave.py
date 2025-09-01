import os
import cv2 as cv
import numpy as np
import imageCrop
rotArr = [-3,-2,-1,1, 2, 3]
p = [[0, 0], [40, 0], [0, 40], [40, 40]]
rotName = {
    -3 : "RA3",
    -2 : "RA2",
    -1: "RA1",
        1 :"RC1",
        2 : "RC2",
        3 : "RC3"
}

Path = "/home/bulu/Desktop/BengChar40x40"
folderList = os.listdir(Path)
cv.namedWindow("rImage",cv.WINDOW_NORMAL)
cv.namedWindow("oImage",cv.WINDOW_NORMAL)
k = -1
for folder in folderList:
    Directory = os.path.join(Path, folder)
    print(folder)
    for item in os.listdir(Directory):
        read = os.path.join(Directory, item)
        image = cv.imread(read)
        x = item.split('.')
        cv.imshow("oImage", image)
        for val in rotArr:
            # if val < 0:
            #     p2 = [[p[0][0] - val , p[0][1]], [p[1][0], p[1][1] - val], [p[2][0] , p[2][1] + val], [p[3][0] + val, p[3][1]]]
            # else :
            #     p2 = [[p[0][0], p[0][1] + val], [p[1][0] - val, p[1][1]], [p[2][0] + val, p[2][1]],
            #           [p[3][0], p[3][1] - val]]
            save = os.path.join(Directory, x[0] + rotName[val] + '.' + x[1])
            # rImage = imageCrop.getPartOfImageZoom(image,p2,[40,40],0)
            rImage = imageCrop.rotateImage(image,val)
            #cv.imwrite(save,rImage)
            print(save)
            cv.imshow('rImage',rImage)
            k = cv.waitKey(0)
            if k == ord('n'):
                break
            if k == ord('q'):
                exit(0)

        if k == ord('n'):
            break


