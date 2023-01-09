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
tipIds = [4, 8, 12, 16, 20]

folderPath = "images"
myList = os.listdir(folderPath)
overlayList = []
for imPath in myList:
    image = cv2.imread(f'{folderPath}/{imPath}')
    # print(f'{folderPath}/{imPath}')
    overlayList.append(image)

detector = htm.handDetector(detectionCon=0.75)
while True:
    if flag == 0:
        success, img = cap.read()
        img = detector.findHands(img)
        lmList = detector.findPosition(img, draw=False)

        if len(lmList) != 0:
            if cv2.waitKey(20) & 0xFF == ord('p'):
                fingers = []
                if lmList[tipIds[0]][1] > lmList[tipIds[0] - 1][1]:
                    fingers.append(1)
                else:
                    fingers.append(0)
                for id in range(1, 5):
                    if lmList[tipIds[id]][2] < lmList[tipIds[id] - 2][2]:
                        fingers.append(1)
                    else:
                        fingers.append(0)
                # print(fingers)
                totalFingers = fingers.count(1)
                # print(totalFingers)
                if totalFingers == 0:
                    h, w, c = overlayList[1].shape
                    img[0:h, wCam - w:wCam] = overlayList[1]
                    choice = 2
                    bot_choice = randint(1, 3)
                    # print(bot_choice)
                    print("User : ROCK ")
                    if bot_choice == 1:
                        print("Bot : PAPER ")
                        imagew = cv2.imread('loser.png')
                        h, w, c = imagew.shape
                        img[0:h, 0:w] = imagew
                        print("You Lost")
                        flag = 1
                    if bot_choice == 3:
                        print("Bot : SCISSORS ")
                        imagew = cv2.imread('winner.jpg')
                        h, w, c = imagew.shape
                        img[0:h, 0:w] = imagew
                        print("You Won")
                        flag = 1
                    if bot_choice == 2:
                        print("Bot : ROCK ")
                        imagew = cv2.imread('draw.png')
                        h, w, c = imagew.shape
                        img[0:h, 0:w] = imagew
                        print("DRAW ")
                        flag = 1
                if totalFingers == 5:
                    h, w, c = overlayList[0].shape
                    img[0:h, wCam - w:wCam] = overlayList[0]
                    choice = 1
                    bot_choice = randint(1, 3)
                    # print(bot_choice)
                    print("User : PAPER")
                    if bot_choice == 2:
                        print("Bot : ROCK ")
                        imagew = cv2.imread('winner.jpg')
                        h, w, c = imagew.shape
                        img[0:h, 0:w] = imagew
                        print("You Won")
                        flag = 1
                    if bot_choice == 3:
                        print("Bot : SCISSORS ")
                        imagew = cv2.imread('loser.png')
                        h, w, c = imagew.shape
                        img[0:h, 0:w] = imagew
                        print("You Lost")
                        flag = 1
                    if bot_choice == 1:
                        print("Bot : PAPER ")
                        imagew = cv2.imread('draw.png')
                        h, w, c = imagew.shape
                        img[0:h, 0:w] = imagew
                        print("DRAW  ")
                        flag = 1
                if totalFingers == 2:
                    h, w, c = overlayList[2].shape
                    img[0:h, wCam - w:wCam] = overlayList[2]
                    choice = 3
                    bot_choice = randint(1, 3)
                    # print(bot_choice)
                    print("User : SCISSORS")
                    if bot_choice == 1:
                        print("Bot : PAPER ")
                        imagew = cv2.imread('winner.jpg')
                        h, w, c = imagew.shape
                        img[0:h, 0:w] = imagew
                        print("You Won")
                        flag = 1
                    if bot_choice == 2:
                        print("Bot : ROCK ")
                        imagew = cv2.imread('loser.png')
                        h, w, c = imagew.shape
                        img[0:h, 0:w] = imagew
                        print("You Lost")
                        flag = 1
                    if bot_choice == 3:
                        print("Bot : SCISSORS ")
                        imagew = cv2.imread('draw.png')
                        h, w, c = imagew.shape
                        img[0:h, 0:w] = imagew
                        print("DRAW  ")
                        flag = 1
            cTime = time.time()
            fps = 1 / (cTime - pTime)
            pTime = cTime
            cv2.putText(img, f'FPS: {int(fps)}', (0, 30), cv2.FONT_HERSHEY_PLAIN, 2, (0, 0, 0), 3)

        elif cv2.waitKey(20) & 0xFF == ord('f'):
            cv2.destroyAllWindows()
            break
        else:
            success, img = cap.read()
            img = detector.findHands(img)
            lmList = detector.findPosition(img, draw=False)
    cv2.imshow("Image", img)
    cv2.waitKey(5)
