import numpy as np
import cv2 as cv


cap = cv.VideoCapture(0)
cascade = cv.CascadeClassifier('hand.xml')


if not cap.isOpened():
    print("Cannot open camera")
    exit()

while True:
    # Capture frame-by-frame
    ret, frame = cap.read()
    # if frame is read correctly ret is True
    if not ret:
        print("Can't receive frame (stream end?). Exiting ...")
        break
    # Display the resulting frame

    gray = cv.cvtColor(frame, cv.COLOR_BGR2GRAY)
    hands = cascade.detectMultiScale(gray, 1.1, 1)

    for (x,y,w,h) in hands:
        cv.rectangle(frame, (x,y), (x+w, y+h), (0,0,255), 2)

    cv.imshow('frame', frame)
    if cv.waitKey(1) == ord('q'):
        break
# When everything done, release the capture
cap.release()
cv.destroyAllWindows()