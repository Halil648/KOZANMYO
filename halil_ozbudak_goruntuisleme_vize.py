import cv2
import mediapipe as mp
import numpy as np

def parmak_acik_mi(el, parmak_index):
    return el.landmark[parmak_index].y < el.landmark[parmak_index - 2].y

def tespit_et(el):
    # Parmaklar ve baş parmak durumu
    isaret, orta, yuzuk, serce = [parmak_acik_mi(el, i) for i in [8, 12, 16, 20]]
    basparmak = el.landmark[4].x < el.landmark[3].x  # başparmak kapalı mı

    # İşaret Tespiti
    if isaret and orta and not yuzuk and not serce:
        return "Zafer Isareti"
    elif isaret and serce and not orta and not yuzuk and basparmak:
        return "Bozkurt Isareti"
    elif not basparmak and isaret and orta and yuzuk and serce:
        return "AKP Isareti"
    return ""

def draw_landmarks_on_image(image, landmarks, handedness, h, w):
    renk = (255, 255, 0)
    for hand_landmarks in landmarks:
        # Koordinatlar
        x1, y1 = int(hand_landmarks.landmark[8].x * w), int(hand_landmarks.landmark[8].y * h)
        x2, y2 = int(hand_landmarks.landmark[4].x * w), int(hand_landmarks.landmark[4].y * h)
        image = cv2.circle(image, (x1, y1), 9, renk, 5)
        image = cv2.circle(image, (x2, y2), 9, renk, 5)
        image = cv2.line(image, (x1, y1), (x2, y2), renk, 5)
        
        # İşaret Tanıma
        tespit = tespit_et(hand_landmarks)
        if tespit:
            image = cv2.putText(image, tespit, (50, 50), cv2.FONT_HERSHEY_SIMPLEX, 1.2, (0, 255, 0), 3)
        
        cv2.putText(image, handedness, (50, 100), cv2.FONT_HERSHEY_DUPLEX, 1, (88, 205, 54), 1, cv2.LINE_AA)
    return image

# Mediapip'i başlatma ve el tespiti
mp_hands = mp.solutions.hands
hands = mp_hands.Hands(min_detection_confidence=0.7, min_tracking_confidence=0.5)

cap = cv2.VideoCapture(0)
while cap.isOpened():
    success, image = cap.read()
    if not success:
        continue
    image = cv2.flip(image, 1)
    rgb_image = cv2.cvtColor(image, cv2.COLOR_BGR2RGB)
    
    # El tespiti
    result = hands.process(rgb_image)
    if result.multi_hand_landmarks and result.multi_handedness:
        for hand_landmarks, handedness in zip(result.multi_hand_landmarks, result.multi_handedness):
            el_tipi = handedness.classification[0].label  # "Left" veya "Right"
            image = draw_landmarks_on_image(image, [hand_landmarks], el_tipi, *image.shape[:2])

    cv2.imshow("El İşareti Tanıma", image)
    if cv2.waitKey(1) & 0xFF == ord('q'):
        break

cap.release()
cv2.destroyAllWindows()
