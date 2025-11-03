import cv2
import mediapipe as mp
import sys

# Setupgit
mp_hands = mp.solutions.hands
hands = mp_hands.Hands()
mp_draw = mp.solutions.drawing_utils

# Try opening camera index 0 first; if it fails, try indices 1..4
cap = cv2.VideoCapture(0)
if not cap.isOpened():
    print("WARN: cannot open camera at index 0; trying indices 1..4")
    for idx in range(1, 5):
        cap.release()
        cap = cv2.VideoCapture(idx)
        if cap.isOpened():
            print(f"Opened camera at index {idx}")
            break
    else:
        print("ERROR: No camera could be opened. Check /dev/video* permissions or that the device is connected.")
        sys.exit(1)

try:
    while True:
        success, img = cap.read()
        if not success or img is None:
            print("ERROR: Failed to read frame from camera. success=", success)
            break

        # Defensive: ensure we have a proper image before converting
        try:
            img_rgb = cv2.cvtColor(img, cv2.COLOR_BGR2RGB)
        except Exception as e:
            print("ERROR: cvtColor failed:", e)
            break

        # Process frame
        result = hands.process(img_rgb)

        if result and getattr(result, 'multi_hand_landmarks', None):
            for hand_landmarks in result.multi_hand_landmarks:
                mp_draw.draw_landmarks(img, hand_landmarks, mp_hands.HAND_CONNECTIONS)

        cv2.imshow("Hand Tracking", img)

        if cv2.waitKey(1) & 0xFF == ord('q'):
            break
except KeyboardInterrupt:
    print('\nInterrupted by user')
finally:
    cap.release()
    cv2.destroyAllWindows()

