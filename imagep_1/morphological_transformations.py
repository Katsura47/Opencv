import cv2
import numpy as np


img = cv2.imread('j.png')

kernel = np.ones((5,5), np.uint8)
erosion = cv2.erode(img, kernel, iterations = 1)
dilation = cv2.dilate(img, kernel, iterations = 1)

cv2.imshow('image', img)

# Useful in removing noise.
opening = cv2.morphologyEx(img, cv2.MORPH_OPEN, kernel)



# remove smaall black points on the object.
closing = cv2.morphologyEx(img, cv2.MORPH_CLOSE, kernel)



# outline of a object
gradient = cv2.morphologyEx(img, cv2.MORPH_GRADIENT, kernel)


# diff between opening and img.
tophat = cv2.morphologyEx(img, cv2.MORPH_TOPHAT, kernel)

cv2.imshow('tophat', tophat)

# diff between closing and img.
blackhat = cv2.morphologyEx(img, cv2.MORPH_BLACKHAT, kernel)



"""# Rectangular Kernel
>>> cv2.getStructuringElement(cv2.MORPH_RECT,(5,5))
array([[1, 1, 1, 1, 1],
       [1, 1, 1, 1, 1],
       [1, 1, 1, 1, 1],
       [1, 1, 1, 1, 1],
       [1, 1, 1, 1, 1]], dtype=uint8)

# Elliptical Kernel
>>> cv2.getStructuringElement(cv2.MORPH_ELLIPSE,(5,5))
array([[0, 0, 1, 0, 0],
       [1, 1, 1, 1, 1],
       [1, 1, 1, 1, 1],
       [1, 1, 1, 1, 1],
       [0, 0, 1, 0, 0]], dtype=uint8)

# Cross-shaped Kernel
>>> cv2.getStructuringElement(cv2.MORPH_CROSS,(5,5))
array([[0, 0, 1, 0, 0],
       [0, 0, 1, 0, 0],
       [1, 1, 1, 1, 1],
       [0, 0, 1, 0, 0],
       [0, 0, 1, 0, 0]], dtype=uint8)"""
