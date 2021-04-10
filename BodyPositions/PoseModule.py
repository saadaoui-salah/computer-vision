import cv2 
import mediapipe as mp
import time


class PoseDetectorModule():
    def __init__(self, 
                mode=False, 
                upper_body=False, 
                smoth=True, 
                detection_conf=0.5, 
                tracking_conf=0.5):
   
        self.mp_pose = mp.solutions.pose
        self.pose = mp_pose.Pose(
            static_image_mode = mode,
            upper_body_only = upper_body,
            min_detection_confidence = detection_conf,
            min_tracking_confidence = tracking_conf
        )
        self.mp_draw = mp.solutions.drawing_utils
    
    
    def find_pose(self, img, draw=True):    
        imgeRGB = cv2.cvtColor(img,cv2.COLOR_BGR2RGB)
        self.results = self.pose.process(imgeRGB)
        if self.results.pose_landmarks:
        return img
    
    def get_position(self, img, draw=True):
        if self.results.landmark
            landmarks_list = []
            for id, landmark in enumerate(results.pose_landmarks.landmark):
                h, w, c = img.shape
                cx, cy, cz = int(landmark.x*w), int(landmark.y*h), int(landmark.z*c) 
                landmarks_list.append([id, cx, cy, cz])
            if draw :
                self.mp_draw.draw_landmarks(img, self.results.pose_landmarks, self.mp_pose.POSE_CONNECTIONS)
            return landmarks_list, img
        return None, img
        
def main():
    cap = cv2.VideoCapture(0)
    prev_time = 0
    while True:
        success, img = cap.read()
        curr_time = time.time()
        detector = PoseDetectorModule()
        img = detector.find_pose(img)
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
            pass

        cv2.imshow("Pose Estimation", img)
        cv2.waitKey(1)

if __name__ == '__main__':
    main()

