

import cv2
import cv2

#classifier
detector = cv2.CascadeClassifier('haarcascade_frontalface_alt.xml')

#capture webcam video
cap = cv2.VideoCapture(0)

while True:
    ret, frame = cap.read()

    if not ret:
        print("can not receive image")
        break

    grayScaleFrame = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)
    #faces
    faces = detector.detectMultiScale(grayScaleFrame, 1.1, 4)

    for(x, y, w, h) in faces:
        cv2.rectangle(frame, (x, y), (x + w, y + h), (255, 0, 0), 2)

    cv2.imshow("face-detection",frame)

    key = cv2.waitKey(30) & 0xff
    if key == 27:
        break

cap.release()