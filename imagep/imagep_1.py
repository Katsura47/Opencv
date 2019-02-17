import cv2
import numpy as np
import matplotlib.pyplot as plt

face_cascade = cv2.CascadeClassifier('haarcascade_frontalface_default.xml')
eye_cascade = cv2.CascadeClassifier('haarcascade_eye.xml')

img = cv2.imread('ben2.jpg')
img2 = cv2.imread('ben.jpg')
mask = np.zeros(img.shape[:2], np.uint8)
mask2 = np.zeros(img2.shape[:2], np.uint8)

bgdModel = np.zeros((1, 65), np.float64)
fgdModel = np.zeros((1, 65), np.float64)


gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
gray2 = cv2.cvtColor(img2, cv2.COLOR_BGR2GRAY)
faces = face_cascade.detectMultiScale(gray, 1.3, 5)
faces2 = face_cascade.detectMultiScale(gray2, 1.3, 5)
print('ye')
lst = []
for (x, y, w ,h) in faces:
    lst.append((x,y,w,h))
for (x, y, w ,h) in faces2:
    lst.append((x,y,w,h))

cv2.grabCut(img, mask, lst[0], bgdModel, fgdModel, 5, cv2.GC_INIT_WITH_RECT)
cv2.grabCut(img2, mask2, lst[1], bgdModel, fgdModel, 5, cv2.GC_INIT_WITH_RECT)
mask2_1 = np.where((mask==2) | (mask==0), 0, 1).astype('uint8')
mask2_2 = np.where((mask2==2) | (mask2==0), 0, 1).astype('uint8')
img = img*mask2_1[:,:,np.newaxis]
img2 = img2*mask2_2[:,:,np.newaxis]
print('ye')
orb = cv2.ORB_create()

kp1, des1 = orb.detectAndCompute(img, None)
kp2, des2 = orb.detectAndCompute(img2, None)

bf = cv2.BFMatcher(cv2.NORM_HAMMING, crossCheck = True)

matches = bf.match(des1, des2)
matches = sorted(matches, key= lambda x:x.distance)

img3 = cv2.drawMatches(img, kp1, img2, kp2, matches[:1000], None, flags=2)

plt.imshow(img3)
plt.show()
