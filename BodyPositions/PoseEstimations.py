import cv2 
import mediapipe as mp
import time

cap = cv2.VideoCapture(0)
mp_pose = mp.solutions.pose
pose = mp_pose.Pose()
mp_draw = mp.solutions.drawing_utils
prev_time = 0
while True:
    success, img = cap.read()
    curr_time = time.time()
    imgeRGB = cv2.cvtColor(img,cv2.COLOR_BGR2RGB)
    results = pose.process(imgeRGB)

    if results.pose_landmarks:
        mp_draw.draw_landmarks(img, results.pose_landmarks, mp_pose.POSE_CONNECTIONS)
        for id, landmark in enumerate(results.pose_landmarks.landmark):
            h, w, c = img.shape
            cx, cy = int(landmark.x*w), int(landmark.y*h) 
    
    try:
        fps = int(1/(curr_time-prev_time))
        cv2.putText(
            img,
            f'FPS: {fps}',
            (0,100),
            cv2.FONT_HERSHEY_PLAIN,
            3,
            (255,255,255),
          3)
        prev_time = curr_time  
    except ZeroDivisionError:
        print(curr_time,prev_time)
        pass

    cv2.imshow("Pose Estimation", img)
    cv2.waitKey(1)