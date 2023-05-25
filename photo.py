import cv2
import mediapipe as mp

def main():
    # Initialize VideoCapture object
    cap = cv2.VideoCapture(0)

    # Initialize Mediapipe Hand object
    mp_hands = mp.solutions.hands
    hands = mp_hands.Hands()

    while True:
        # Read frame from camera
        ret, frame = cap.read()

        # Convert image to RGB
        image = cv2.cvtColor(frame, cv2.COLOR_BGR2RGB)

        # Process the image with Mediapipe
        results = hands.process(image)

        # Check for hand landmarks
        if results.multi_hand_landmarks:
            for hand_landmarks in results.multi_hand_landmarks:
                # Draw hand landmarks on the frame
                mp_drawing.draw_landmarks(frame, hand_landmarks, mp_hands.HAND_CONNECTIONS)

        # Display the resulting frame
        cv2.imshow('Hand Tracking', frame)

        # Check for 'q' key press to exit
        if cv2.waitKey(1) & 0xFF == ord('q'):
            break

    # Release the VideoCapture object and close windows
    cap.release()
    cv2.destroyAllWindows()

if __name__ == '__main__':
    main()
