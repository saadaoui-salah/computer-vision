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


previouse_time = 0
while True:

    success, img = capture.read()
    if success:
        h,w,c = images[0].shape
        img[0:h,0:w] = images[0]
        
        
        current_time = time.time()
        fps = int(1/(current_time-previouse_time))
        previouse_time = current_time
        cv2.putText(
            img,
            f'FPS: {str(fps)}',
            (0,0),
            cv2.FONT_HERSHEY_COMPLEX,
            3,
            (0,0,0),
            3)
        cv2.imshow("Image",img)
        cv2.waitKey(1)


    else:
        break
