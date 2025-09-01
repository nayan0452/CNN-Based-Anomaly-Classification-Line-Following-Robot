import cv2 as cv
import numpy as np
img = cv.imread("Basic-characters-of-Bangla-alphabet-first-eleven-are-vowels-and-rest-is-consonant (1).png")
cv.imshow()

resMatt = np.zeros((60,60), dtype= np.float32)