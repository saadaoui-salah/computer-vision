import cv2
import time
import os
import HandTrackingModule

capture = cv2.VideoCapture(0) 
capture.set(3,900)
capture.set(4,800)

folder = "data"
dirs = os.listdir(folder)
images = []

for im_path in dirs:
    img = cv2.imread(f'{folder}/{im_path}')
    images.append(img)



while True:

    success, img = capture.read()
    if success:
        h,w,c = images[0].shape
        img[0:h,0:w] = images[0]
        cv2.imshow("Image",img)
        cv2.waitKey(1)


    else:
        break
