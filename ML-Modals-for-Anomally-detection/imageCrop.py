import cv2 as cv
import numpy as np
import os
import threading
import warnings
import time

warnings.filterwarnings("ignore")


def showImage(img, wName:str):
    cv.namedWindow(wName,cv.WINDOW_NORMAL)
    cv.imshow(wName, img)
    cv.waitKey(0)
    cv.destroyWindow(wName)


def getPartOfImage(srcImage, points: list, shape) :
    p1 = np.float32(points)
    p2 = np.float32([[0,0], [shape[0], 0], [0,shape[1]], [shape[0], shape[1]]])
    matt = cv.getPerspectiveTransform(p1,p2)
    out = cv.warpPerspective(srcImage,matt,shape,flags=cv.INTER_NEAREST)
    return out


def zoomImage(srcImage : np.array, zoom:int) :
    shape = srcImage.shape
    p2 = np.float32([[0 + zoom, 0 + zoom], [shape[0] - zoom, 0 + zoom], [0 + zoom, shape[1] - zoom], [shape[0] - zoom, shape[1] - zoom]])
    out = getPartOfImage(srcImage, p2, (shape[0], shape[1]))
    return out


def tacilateImage(image: np.array, tX:int, tY:int):
    s = image.shape
    p = [[0, 0], [s[0], 0], [0, s[1]], [s[0], s[1]]]
    p2 = [[p[0][0] - tX, p[0][1] - tY], [p[1][0] - tX, p[1][1] - tY], [p[2][0] - tX, p[2][1] - tY], [p[3][0] - tX, p[3][1] - tY]]
    rImage = getPartOfImage(image, p2, [s[0], s[1]])
    return rImage


def rotateImage(image: np.array, rotation:int):
    s = image.shape
    p = [[0, 0], [s[0], 0], [0, s[1]], [s[0], s[1]]]
    if rotation < 0:
        p2 = [[p[0][0] - rotation, p[0][1]], [p[1][0], p[1][1] - rotation], [p[2][0], p[2][1] + rotation], [p[3][0] + rotation, p[3][1]]]
    else:
        p2 = [[p[0][0], p[0][1] + rotation], [p[1][0] - rotation, p[1][1]], [p[2][0] + rotation, p[2][1]],
              [p[3][0], p[3][1] - rotation]]
    rImage = getPartOfImage(image, p2, [s[0], s[1]])
    return rImage


if __name__ == '__main__':
    currentDir = os.getcwd()
    lis = os.listdir(currentDir)
    for x in lis:
        filePath = os.path.join(currentDir, x)
        isFile = os.path.isfile(filePath)
        if isFile and x.split('.')[1] == 'png':
            img = cv.imread(filePath)
            thr1 = threading.Thread(target=showImage,args=(img,"Image"))
            thr1.start()
            time.sleep(0.5)
            print("Enter the points:")
            points = []
            for n in range(4):
                x = int(input())
                y = int(input())
                points.append([x,y])

            print("Enter Width and hight:")
            x = int(input())
            y = int(input())
            shape = [x,y]

            imagePart = getPartOfImage(img, points, shape)
            cv.imshow("Output", imagePart)
            cv.waitKey(0)
            cv.destroyWindow("Output")
            thr1.join()
    cv.destroyAllWindows()