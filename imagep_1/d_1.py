import cv2
import numpy as np

A = cv2.imread('apple.JPG')
B = cv2.imread('orange.JPG')

# generate Gaussian pyramid for A


G = A.copy()
gpA = [G]
for i in range(6):
    G = cv2.pyrDown(G)
    gpA.append(G)


# generate Gaussian pyramid for B

G = B.copy()
gpB = [G]
for i in range(6):
    G = cv2.pyrDown(G)
    gpB.append(G)


# generate laplacian pyramid for A
lpA = [gpA[4]]
for i in range(2, 1, -1):
    GE = cv2.pyrUp(gpA[i])
    L = cv2.subtract(gpA[i-1], GE)
    lpA.append(L)

# generate laplacian pyramid for B
lpB = [gpB[4]]
for i in range(2, 1, -1):
    GE = cv2.pyrUp(gpB[i])
    L = cv2.subtract(gpB[i-1], GE)
    lpB.append(L)



# now add left and right halves of images in each level

LS = []
for la, lb in zip(lpA, lpB):
    rows, cols, dpt = la.shape
    ls = np.hstack((la[:,0:cols/2], lb[:, cols/2:]))
    LS.append(ls)


# now reconstruct
ls_ = LS[0]
for i in range(1,6):
    ls_ = cv2.pyrUp(ls_)
    ls_ = cv2.add(ls_, LS[i])

# imag with direct connecting each half

real = np.hstack((A[:,:cols/2],B[:,cols/2:]))

cv2.imwrite('Pyramid_blending2.jpg', ls_)
cv2.imwrite('Direct_blending.jpg', real)





