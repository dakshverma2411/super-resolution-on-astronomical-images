import cv2 as cv
import numpy as np
print(cv.__version__)
img=cv.imread('demo.jpg')
img_blur=img
print(img_blur.shape)
# cv.imshow('Space',img)
# cv.imshow('Blurred',img_blur)
cv.imwrite('demo_blur.jpg',img_blur[::4,::4])
cv.waitKey(0)