import os
import cv2 as cv
import numpy as np
resize = 56
cwd = os.getcwd()
oriPath = os.path.join(cwd, "Datasets/RawData/BengChar/Bengali_Dataset/New Folder/BanglaLekha-Isolated/Images")
folderList = os.listdir(oriPath)
copyPath = os.path.join(cwd,f"BengChar{resize}x{resize}")
os.mkdir(copyPath)
for folder in folderList:
    readDirectory = os.path.join(oriPath,folder)
    saveDirectory = os.path.join(copyPath, folder)
    os.mkdir(saveDirectory)
    print(folder)
    for item in os.listdir(readDirectory):
        read = os.path.join(readDirectory, item)
        save = os.path.join(saveDirectory, item)
        oriImage = cv.imread(read)
        resizeImage = cv.resize(oriImage,(resize,resize))
        cv.imwrite(save,resizeImage)