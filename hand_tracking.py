import cv2
import mediapipe as mp
import time

# Read the camera
cap = cv2.VideoCapture(0)
# Hand tracker
mphands = mp.solutions.hands
hands   = mphands.Hands()
# Drawer class
mpdraw  = mp.solutions.drawing_utils

previous_time = 0 
while True:
    
    success, img = cap.read()
    imgRGB = cv2.cvtColor(img, cv2.COLOR_BGR2RGB)
    
    previous_time = time.time()

    # Detecting land marks    
    results = hands.process(imgRGB)
    # print(results.multi_hand_landmarks)
    hands_landmarks = results.multi_hand_landmarks
    if hands_landmarks:
        for hand_landmarks in hands_landmarks:
            for id, lm in enumerate(hand_landmarks.landmark):
                # will give us each landmark with (x,y,z) 
                # print(id,lm)
                # 
                h, w, c = img.shape
                # multiply the width with x and the height with y  
                # to get the real position 
                cx, cy  = int(lm.x*w), int(lm.y*h)
                # print(id, cx, cy)
                mpdraw.draw_landmarks(img, hand_landmarks, mphands.HAND_CONNECTIONS)
                ## draw a circle in landmark number 0
                #if id == 0:
                #    cv2.circle((cx,cy), 15, (255,0,255), cv2.FILLED)


    # Calculate fps
    current_time = time.time()
    fps = int(1/(current_time - previous_time))
    previous_time = current_time
    # Add text
    cv2.putText(
        img,
        f'FPS: {fps}',
        (10,78),
        cv2.FONT_HERSHEY_PLAIN,
        3,
        (255,0,255),
        3)

    cv2.imshow('Image', img)
    cv2.waitKey(1)
