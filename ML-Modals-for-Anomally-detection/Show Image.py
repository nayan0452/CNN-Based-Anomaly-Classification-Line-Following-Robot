import cv2
import urllib.request
import numpy as np
import os
# Replace the URL with the IP camera's stream URL
cv2.namedWindow("live Cam Testing", cv2.WINDOW_NORMAL)
cv2.namedWindow("live Cam Testing2", cv2.WINDOW_NORMAL)
path = os.path.join(os.getcwd(),'Frames/500.jpg')
img = cv2.imread(path)
while True:
    # ret, frame = cap.read()

    cv2.imshow('live Cam Testing', img)
    key = cv2.waitKey(5)
    if key == ord('q'):
        break


img2 = img[:,241:1680]
while True:
    # ret, frame = cap.read()

    cv2.imshow('live Cam Testing2', img2)
    key = cv2.waitKey(5)
    if key == ord('q'):
        break

cv2.destroyAllWindows()
