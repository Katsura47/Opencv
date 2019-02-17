import cv2
import numpy as np
import matplotlib.pyplot as plt



img = cv2.imread('watch.JPG')

rows, cols, ch = img.shape

M = cv2.getRotationMatrix2D((cols/2, rows/2), 45, 1)
dst = cv2.warpAffine(img, M, (cols, rows))
cv2.imshow('dst', dst)
