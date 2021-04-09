import cv2
import mediapipe as mp
import time


class HandDetector():
    def __init__(self,mode=False, max_hands=2, detection_conf=0.6, track_conf=0.6):
        self.mode           = mode
        self.max_hands      = max_hands
        self.detection_conf = detection_conf
        self.track_conf     = track_conf
        
        self.mphands = mp.solutions.hands
        self.hands   = self.mphands.Hands(
                    self.mode,
                    self.max_hands,
                    self.detection_conf,
                    self.track_conf,
        )
        self.mpdraw  = mp.solutions.drawing_utils


    def find_hends(self,img):    
        imgRGB = cv2.cvtColor(img, cv2.COLOR_BGR2RGB)
        self.results = self.hands.process(imgRGB)
        self.hands_landmarks = self.results.multi_hand_landmarks
        if self.hands_landmarks:
            for hand_landmarks in self.hands_landmarks:
                    self.mpdraw.draw_landmarks(img, hand_landmarks, self.mphands.HAND_CONNECTIONS)
        return img         
    
    def find_position(self,img,hand_number=0):
        landmarks_list = []
        if self.hands_landmarks:
            hand = self.hands_landmarks[hand_number]
            #print(self.hands_landmarks)
            for id, lm in enumerate(hand.landmark):
                self.mpdraw.draw_landmarks(img, hand, self.mphands.HAND_CONNECTIONS)
                h, w, c = img.shape
                cx, cy  = int(lm.x*w), int(lm.y*h)
                landmarks_list.append([id, cx, cy])
                #cv2.circle(img, (cx,cy), 15, (255,0,255), cv2.FILLED)

        return landmarks_list

def main():

    cap = cv2.VideoCapture(0)
    detector = HandDetector()
    previous_time = 0
    while True:    
        success, img = cap.read()
        
        img = detector.find_hends(img)
        landmarks_list = detector.find_position(img)
        if landmarks_list != 0:
           print(landmarks_list)
        current_time = time.time()
        fps = 1/(current_time - previous_time)
        previous_time = current_time
        cv2.putText(
            img,
            f'FPS: {str(fps)}',
            (10,78),
            cv2.FONT_HERSHEY_PLAIN,
            3,
            (255,0,255),
            3)
        cv2.imshow('Image', img)
        cv2.waitKey(1)


if __name__ == '__main__':
    main()