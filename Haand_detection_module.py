import cv2 as cv
import mediapipe as mp
import time


class HandDetector():
    def __init__(self, mode=False, maxHands = 2, detectionCon = 0.5, trackCon = 0.5):
        self.mode = mode
        self.maxHands = maxHands
        self.detectionCon = detectionCon
        self.trackCon = trackCon
        self.mpHands = mp.solutions.hands
        self.hands = self.mpHands.Hands(self.mode, self.maxHands, self.detectionCon, self.trackCon)
        self.mpDraw = mp.solutions.drawing_utils

    def FindHands(self, img, draw = True):
        img_RGB = cv.cvtColor(img, cv.COLOR_BGR2RGB)
        self.results = self.hands.process(img_RGB)
        # print(results.multi_hand_landmarks)
        if self.results.multi_hand_landmarks:
            for handLms in self.results.multi_hand_landmarks:
                if draw:
                    self.mpDraw.draw_landmarks(img, handLms, self.mpHands.HAND_CONNECTIONS)
        return img

    def FindPosition(self, img, handNo=0, draw = True):

            lmlist = []

            if self.results.multi_hand_landmarks:
                myHand = self.results.multi_hand_landmarks[handNo]
                for id, Lm in enumerate(myHand.landmark):
                    h, w, c = img.shape
                    cx, cy = int(Lm.x * w), int(Lm.y * h)
                    # print(id, cx, cy)
                    lmlist.append([id, cx, cy])
                    if not draw:
                        continue
                    cv.circle(img, (cx, cy), 5, (0, 0, 255), cv.FILLED)
            return lmlist




def main():
    CTime = 0
    pTime = 0

    a = cv.VideoCapture(0)
    detector = HandDetector()

    while True:
        success, img = a.read()
        img = detector.FindHands(img)
        lmlist = detector.FindPosition(img)
        if len(lmlist) != 0:
             print(lmlist[4])

        CTime = time.time()
        fps = 1 / (CTime - pTime)
        pTime = CTime

        cv.putText(img, str(int(fps)), (10, 70), cv.FONT_HERSHEY_COMPLEX_SMALL, 3, (255, 0, 0), 3)

        cv.imshow('A_I', img)
        cv.waitKey(1)



if __name__ =="__main__":
    main()
