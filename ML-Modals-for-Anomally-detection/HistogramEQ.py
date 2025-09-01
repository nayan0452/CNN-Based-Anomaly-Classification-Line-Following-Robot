import cv2 as cv
import os

cwd = os.getcwd()
frames = os.path.join(cwd,'Frames')
lis = os.listdir(frames)
output_folder = os.path.join(cwd,'HE')
if not os.path.exists(output_folder):
    os.mkdir(output_folder)
i = 0
for item in lis:
    path = os.path.join(frames,item)
    img = cv.imread(path)
    hsvIMG = cv.cvtColor(img,cv.COLOR_BGR2HSV)
    pi = hsvIMG[:,:,2]
    eqpi = cv.equalizeHist(pi)
    hsvIMG[:,:,2] = eqpi
    eqimg = cv.cvtColor(hsvIMG,cv.COLOR_HSV2BGR)
    cv.imwrite(os.path.join(output_folder,item),eqimg)

