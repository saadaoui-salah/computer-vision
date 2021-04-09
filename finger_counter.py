import cv2
import time
import os
from HandTrackingModule import HandDetector

capture = cv2.VideoCapture(0) 
capture.set(3,480)
capture.set(4,700)

folder = "data"
dirs = os.listdir(folder)
images = []

for im_path in dirs:
    img = cv2.imread(f'{folder}/{im_path}')
    images.append(img)

detector = HandDetector(detection_conf=0.7, track_conf=0.7)

tip_ids = [4, 8, 12, 16, 20]

previouse_time = 0
while True:

    success, img = capture.read()
    if success:
        current_time = time.time()
        img = detector.find_hands(img)
        landmarks_list = detector.find_position(img,draw=False)
        
        if len(landmarks_list) != 0: # if there are hand
            fingers = []
            cv2.rectangle(img,(0,150),(170,300),(0,255,100),cv2.FILLED)
            if landmarks_list[4][1] > landmarks_list[20][1]:
                print('right')
                cv2.putText(
                    img,
                    'right',
                    (0,280),# location
                    cv2.FONT_HERSHEY_COMPLEX,# text font
                    1,# scale
                    (200,0,0),# color
                    3)# thiknes

            else:
                cv2.putText(
                    img,
                    'left',
                    (0,280),# location
                    cv2.FONT_HERSHEY_COMPLEX,# text font
                    1,# scale
                    (200,0,0),# color
                    3)# thiknes
                print('left')

            if landmarks_list[tip_ids[0]][2] < landmarks_list[tip_ids[0]+1][2]: 
                fingers.append(1)
            else:
                fingers.append(0)

            for id in range(1,5):
                   #y of land mark x              <        y of land mark x-2
                if landmarks_list[tip_ids[id]][2] < landmarks_list[tip_ids[id]-2][2]: 
                    fingers.append(1)
                else:
                    fingers.append(0)
            #print(fingers)
            total_fingers = fingers.count(1)
            h,w,c = images[total_fingers].shape
            img[0:h,0:w] = images[total_fingers]
            cv2.putText(
                img,
                f'{total_fingers}',
                (50,250),# location
                cv2.FONT_HERSHEY_COMPLEX,# text font
                3,# scale
                (200,0,0),# color
                3)# thiknes
        try:
            fps = int(1/(current_time-previouse_time))
            previouse_time = current_time
            cv2.putText(
                img,
                f'FPS: {str(fps)}',
                (0,400),# location
                cv2.FONT_HERSHEY_COMPLEX,# text font
                1,# scale
                (100,100,0),# color
                3)# thiknes
        except ZeroDivisionError:
            pass       
        cv2.imshow("Image",img)
        cv2.waitKey(1)


    else:
        break
