import cv2
import numpy as np
from matplotlib import pyplot as plt

events = [i for i in dir(cv2) if 'EVENT' in i]

def draw_circle(event, x, y, flags, param):
    if event == cv2.EVENT_LBUTTONDBLCLK:
        cv2.circle(img, (x, y), 100, (255, 0, 0), -1)


img = np.zeros((512,512,3), np.uint8)

cv2.namedWindow('image')
cv2.setMouseCallback('image', draw_circle)

while (1):
    cv2.imshow('image', img)
    k = cv2.waitKey(20)
    if k == 27 & 0xFF:
        break
cv2.destroyAllWindows()





"""cv2.imshow('image', img)

k = cv2.waitKey(0)
if k == 27 & 0xFF:
    cv2.destroyAllWindows()"""
