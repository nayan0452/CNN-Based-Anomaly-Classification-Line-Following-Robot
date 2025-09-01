import os
import cv2 as cv
import random
import numpy as np

def addNoiseSaltPeper (image,ll,ul, inPlace = True):
    if ll >= ul:
        return image
    if not inPlace :
        image = np.copy(image)
    times = random.randint(ll,ul)
    s = image.shape
    if len(s) == 3 and s[2] == 3:
        for n in range(times):
            x = random.randint(0,s[0] -1)
            y = random.randint(0,s[1] -1)
            tf = random.randint(0,99)
            if tf % 2 == 0:
                image[x][y][0] = image[x][y][2] = image[x][y][1] = 0
            else:
                image[x][y][0] = image[x][y][1] = image[x][y][2] = 255


    if len(s) == 2 or (len(s) == 3 and s[2] == 1):
        for n in range(times):
            x = random.randint(0,s[0] -1)
            y = random.randint(0,s[1] -1)
            tf = random.randint(0,99)
            if tf % 2 == 0:
                image[x][y] = 0
            else:
                image[x][y] = 255

    return image

def addNoiseRandom (image,ll,ul, inPlace = True):
    if ll >= ul:
        return image
    if not inPlace :
        image = np.copy(image)
    times = random.randint(ll,ul)
    s = image.shape
    if len(s) == 3 and s[2] == 3:
        for n in range(times):
            x = random.randint(0,s[0] -1)
            y = random.randint(0,s[1] -1)
            image[x][y][0] = random.randint(0,255)
            image[x][y][1] = random.randint(0,255)
            image[x][y][2] = random.randint(0,255)

    if len(s) == 2 or (len(s) == 3 and s[2] == 1):
        for n in range(times):
            x = random.randint(0,s[0] -1)
            y = random.randint(0,s[1] -1)
            image[x][y] = random.randint(0,255)

    return image



if __name__ == '__main__':
    oriPath = "/home/bulu/Desktop/BengChar40x40"
    folderList = os.listdir(oriPath)
    savePath = "/home/bulu/Desktop/BengChar40x40Augmented"
    k = -1
    show = True
    save = False
    cv.namedWindow("Image", cv.WINDOW_NORMAL)
    for folder in folderList:
        readDirectory = os.path.join(oriPath,folder)
        saveDirectory = os.path.join(savePath, folder)
        if not os.path.exists(saveDirectory) and save:
            os.mkdir(saveDirectory)
            print(folder)
        for item in os.listdir(readDirectory):
            read = os.path.join(readDirectory, item)
            image = cv.imread(read)
            image = cv.cvtColor(image,cv.COLOR_BGR2GRAY)
            print(image.shape)
            addNoiseRandom(image,100,200)
            if show:
                cv.imshow("Image",image)
                k = cv.waitKey(0)
                if k == ord('n') or k == ord('q'):
                    break
            if save:
                x = item.split('.')
                slNumber = random.randint(0,100)
                name = f"{x[0]}N{slNumber}.{x[1]}"
                save = os.path.join(saveDirectory, name)
                #print(save)
                cv.imwrite(save)
        if k == ord('q'):
            exit(0)

