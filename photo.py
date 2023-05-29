import cv2
from time import sleep
import mediapipe as mp

# Define a dictionary of sign language gestures and their meanings



def main():
    cap = cv2.VideoCapture(0)
    
    # Initialize MediaPipe Hands
    mp_hands = mp.solutions.hands
    hands = mp_hands.Hands()
    mp_drawing = mp.solutions.drawing_utils
    with mp_hands.Hands(min_detection_confidence=0.8, min_tracking_confidence=0.5) as hands:
        i = 1
        while cap.isOpened():
                # Add more gesture recognition logic here
        

            success, frame = cap.read()
            if not success:
                break

            
            # Convert the image to RGB
            image_rgb = cv2.cvtColor(frame, cv2.COLOR_BGR2RGB)
            cv2.flip(frame ,1)
            
            # Process the image with MediaPipe Hands
            results = hands.process(image_rgb)
            
            if results.multi_hand_landmarks:
                for hand_landmarks in results.multi_hand_landmarks:
                    # Draw the landmarks on the image
                # Draw hand landmarks
                    index_finger = hand_landmarks.landmark[mp_hands.HandLandmark.INDEX_FINGER_TIP]
                    middle_finger = hand_landmarks.landmark[mp_hands.HandLandmark.MIDDLE_FINGER_TIP]
                    index_to_middle_dist = abs(index_finger.x - middle_finger.x) + abs(index_finger.y - middle_finger.y) + abs(index_finger.z - middle_finger.z)

                    if index_to_middle_dist > 0.15:
                        for counter in range(5,0, -1):
                            cv2.putText(frame,str(counter), (10, 30), cv2.FONT_HERSHEY_SIMPLEX, 1, (0, 0, 255), 2)
                            cv2.imshow('Sign Recognition', frame)
                            cv2.waitKey(1000)
                        print("image saved succsessfully")              
                        i+=1

            # Display the resulting image
            cv2.imshow('Sign Recognition', frame)
            
            if cv2.waitKey(1) == ord('q'):
                break

        
        cap.release()
        cv2.destroyAllWindows()

main()


