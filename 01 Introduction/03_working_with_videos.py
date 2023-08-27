import cv2

cap = cv2.VideoCapture(0)  # webcam
# cap = cv2.VideoCapture("gallery\yvideo.jpg")  # file

while True:
    ret, frame = cap.read()
    frame = cv2.flip(frame, 1)  # y axis flip
    # frame = cv2.flip(frame, 0) # x axis flip
    # frame = cv2.flip(frame, -1) # origin flip
    if ret == 0:
        break

    cv2.imshow("Video", frame)
    if cv2.waitKey(1) & 0xFF == ord("q"):
        break

cap.release()
cv2.destroyAllWindows()
