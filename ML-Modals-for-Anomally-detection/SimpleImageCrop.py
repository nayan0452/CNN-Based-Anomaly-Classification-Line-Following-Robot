import cv2
import urllib.request
import numpy as np
import os
# Replace the URL with the IP camera's stream URL
path = os.path.join(os.getcwd(),'Frames')
lis = os.listdir(path)
for item in lis:
    print(item)
    save = os.path.join(path,item)
    img = cv2.imread(save)
    img2 = img[:,241:1680]
    cv2.imwrite(save,img2)

