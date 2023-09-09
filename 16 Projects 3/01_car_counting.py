import cv2
import numpy as np

cap = cv2.VideoCapture("gallery/traffic.avi")
back_sub = cv2.createBackgroundSubtractorMOG2()
count = 0

while True:
    ret, frame = cap.read()

    if ret:
        fgmask = back_sub.apply(frame)
        cv2.line(frame, (50, 0), (50, 300), (0, 255, 0), 2)
        cv2.line(frame, (70, 0), (70, 300), (0, 255, 0), 2)

        contours, hierarchy = cv2.findContours(
            fgmask, cv2.RETR_TREE, cv2.CHAIN_APPROX_SIMPLE)

        try:
            hierarchy = hierarchy[0]
        except:
            hierarchy = []

        for contour, hier in zip(contours, hierarchy):
            (x, y, w, h) = cv2.boundingRect(contour)

            if w > 40 and h > 40:
                cv2.rectangle(frame, (x, y), (x+w, y+h), (255, 0, 0), 3)
                if x > 50 and x < 70:
                    count = count + 1

        cv2.putText(frame, "car: "+str(count), (90, 100),
                    cv2.FONT_HERSHEY_SIMPLEX, 2, (0, 0, 255), 2, cv2.LINE_AA)

        cv2.imshow("Car Counter", frame)

        if cv2.waitKey(5) & 0xFF == ord("q"):
            break


cap.release()
cv2.destroyAllWindows()
