import cv2
import numpy as np


img = cv2.imread('watch.JPG', cv2.IMREAD_COLOR)

px = img[55, 55]


img[55, 55] = [255, 255, 255]

px = img[55, 55]


#Region of Image = ROI


watch_face = img[100:350, 150:500]
img[0:250, 0:350] = watch_face

cv2.imshow('image', img)
cv2.waitKey(0)
cv2.destroyAllWindows()




