import cv2
import numpy as np

cap = cv2.VideoCapture("gallery/line.mp4")

circles = []


def mouse(event, x, y, flags, params):
    if event == cv2.EVENT_LBUTTONDOWN:
        circles.append((x, y))


cv2.namedWindow("Frame")
cv2.setMouseCallback("Frame", mouse)

while True:
    ret, frame = cap.read()
    frame = cv2.resize(frame, (640, 480))
    for center in circles:
        cv2.circle(frame, center, 20, (255, 0, 0), 3)
    cv2.imshow("Frame", frame)
    if cv2.waitKey(1) & 0xFF == ord("q"):
        break
    elif cv2.waitKey(1) == ord("h"):
        circles = []

cap.release()
cv2.destroyAllWindows()
