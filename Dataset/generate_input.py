import cv2 as cv
import numpy as np
import os

def generate(img_name):
    img=cv.imread('train_target/'+img_name)
    cv.imwrite('train_input/'+img_name+'.jpg',img[::4,::4,:])

files=os.listdir('train_target/')

for f in files:
    if len(f)>4 and f[-4:]=='.jpg':
        generate(f)