import numpy as np
import cv2 as cv

# image = cv2.copyMakeBorder( src, top, bottom, left, right, borderType)

def change_dimension(img_name):
    img=cv.imread(img_name)
    ht,wd,cc=img.shape
    top=(720-ht)//2
    bottom=720-ht-top
    left=(1024-wd)//2
    right=(1024-wd-left)
    borderType=cv.BORDER_WRAP
    img_modified = cv.copyMakeBorder( img, top, bottom, left, right, borderType)
    cv.imshow('modified',img_modified)
    cv.waitKey(0)

change_dimension('heic0206b.jpg')