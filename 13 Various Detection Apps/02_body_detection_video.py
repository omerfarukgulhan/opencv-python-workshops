import cv2
# haar cascade doesnt work properly on humans and cars
cap = cv2.VideoCapture("gallery/body.mp4")  # for video
# cap = cv2.VideoCapture(0) # for webcam

body_cascade = cv2.CascadeClassifier("Haar Cascade/fullbody.xml")

while True:
    ret, frame = cap.read()
    # frame = cv2.flip(frame, 1)  # for webcam
    gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)
    bodies = body_cascade.detectMultiScale(gray, 1.1, 1)

    for (x, y, w, h) in bodies:
        cv2.rectangle(frame, (x, y), (x+w, y+h), (0, 255, 255), 3)

    cv2.imshow("video", frame)

    if cv2.waitKey(5) & 0xFF == ord("q"):
        break

cap.release()
cv2.destroyAllWindows()
