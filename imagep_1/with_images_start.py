import cv2
import numpy as np
from matplotlib import pyplot as plt

img = cv2.imread("watch.JPG", 0)

cv2.namedWindow('watch', cv2.WINDOW_NORMAL)
cv2.imshow("watch", img)
cv2.waitKey(0)
cv2.imwrite('watch_gray.JPG', img)
cv2.destroyAllWindows()

plt.imshow(img, cmap='gray', interpolation='bicubic')
plt.xticks([]), plt.yticks([])
plt.show()
