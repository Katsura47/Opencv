import cv2
import numpy as np
import matplotlib.pyplot as plt


img = cv2.imread('watch.jpg')

# normal blr.
blur = cv2.blur(img,(5,5))

# gaussian blur gaussian noise removing.
g_blur = cv2.GaussianBlur(img,(5,5), 0)

#  efective at salt and pepper noise in images.
median = cv2.medianBlur(img, 5)

#Köşelere dikkat eder.
bilateral = cv2.bilateralFilter(img, 9, 75, 75)

plt.subplot(121),plt.imshow(img),plt.title('Original')
plt.xticks([]),plt.yticks([])
plt.subplot(122),plt.imshow(blur),plt.title('Blurred')
plt.xticks([]),plt.yticks([])
plt.show()
