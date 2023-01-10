import cv2
import time
import os
import HandTrackingModule as htm
from random import randint

choice = 0
wCam, hCam = 1280, 720
bot_choice = 0
flag = 0
cap = cv2.VideoCapture(1)
cap.set(3, wCam)
cap.set(4, hCam)
pTime = 0
TipsCords = [4, 8, 12, 16, 20]

myList = os.listdir(f"images")
ImgList = []
for path in myList:
    image = cv2.imread(f'images/{path}')
    ImgList.append(image)

detector = htm.handDetector(detectionCon=0.65)
while True:
    if flag == 0:
        success, img = cap.read()
        img = detector.findHands(img)
        lmList = detector.findPosition(img, draw=False)
        cTime = time.time()
        fps = 1 / (cTime - pTime)
        pTime = cTime
        cv2.putText(img, f'FPS: {int(fps)}', (0, 30), cv2.FONT_HERSHEY_PLAIN, 2, (255, 255, 0), 3)
        if len(lmList) != 0:
            if cv2.waitKey(10) & 0xFF == ord('p'):
                fingers = []
                if lmList[TipsCords[0]][1] > lmList[TipsCords[0] - 1][1]:
                    fingers.append(1)
                else:
                    fingers.append(0)
                for id in range(1, 5):
                    if lmList[TipsCords[id]][2] < lmList[TipsCords[id] - 2][2]:
                        fingers.append(1)
                    else:
                        fingers.append(0)
                totalFingers = fingers.count(1)
                if totalFingers == 0:
                    h, w, c = ImgList[1].shape
                    img[0:h, wCam - w:wCam] = ImgList[1]
                    choice = 2
                    bot_choice = randint(1, 3)
                    print("User : ROCK ")
                    if bot_choice == 1:
                        print("Bot : PAPER ")
                        image1 = cv2.imread('loser.png')
                        h, w, c = image1.shape
                        img[0:h, 0:w] = image1
                        print("You Lost")
                        flag = 1
                    if bot_choice == 3:
                        print("Bot : SCISSORS ")
                        image1 = cv2.imread('winner.jpg')
                        h, w, c = image1.shape
                        img[0:h, 0:w] = image1
                        print("You Won")
                        flag = 1
                    if bot_choice == 2:
                        print("Bot : ROCK ")
                        image1 = cv2.imread('draw.png')
                        h, w, c = image1.shape
                        img[0:h, 0:w] = image1
                        print("DRAW ")
                        flag = 1
                if totalFingers == 5:
                    h, w, c = ImgList[0].shape
                    img[0:h, wCam - w:wCam] = ImgList[0]
                    choice = 1
                    bot_choice = randint(1, 3)
                    print("User : PAPER")
                    if bot_choice == 2:
                        print("Bot : ROCK ")
                        image1 = cv2.imread('winner.jpg')
                        h, w, c = image1.shape
                        img[0:h, 0:w] = image1
                        print("You Won")
                        flag = 1
                    if bot_choice == 3:
                        print("Bot : SCISSORS ")
                        image1 = cv2.imread('loser.png')
                        h, w, c = image1.shape
                        img[0:h, 0:w] = image1
                        print("You Lost")
                        flag = 1
                    if bot_choice == 1:
                        print("Bot : PAPER ")
                        image1 = cv2.imread('draw.png')
                        h, w, c = image1.shape
                        img[0:h, 0:w] = image1
                        print("DRAW  ")
                        flag = 1
                if totalFingers == 2:
                    h, w, c = ImgList[2].shape
                    img[0:h, wCam - w:wCam] = ImgList[2]
                    choice = 3
                    bot_choice = randint(1, 3)
                    print("User : SCISSORS")
                    if bot_choice == 1:
                        print("Bot : PAPER ")
                        image1 = cv2.imread('winner.jpg')
                        h, w, c = image1.shape
                        img[0:h, 0:w] = image1
                        print("You Won")
                        flag = 1
                    if bot_choice == 2:
                        print("Bot : ROCK ")
                        image1 = cv2.imread('loser.png')
                        h, w, c = image1.shape
                        img[0:h, 0:w] = image1
                        print("You Lost")
                        flag = 1
                    if bot_choice == 3:
                        print("Bot : SCISSORS ")
                        image1 = cv2.imread('draw.png')
                        h, w, c = image1.shape
                        img[0:h, 0:w] = image1
                        print("DRAW  ")
                        flag = 1
        elif cv2.waitKey(1) & 0xFF == ord('f'):
            cv2.destroyAllWindows()
            break
        else:
            success, img = cap.read()
            img = detector.findHands(img)
            lmList = detector.findPosition(img, draw=False)
    cv2.imshow("Rock Paper Scissor", img)
    cv2.waitKey(1)
