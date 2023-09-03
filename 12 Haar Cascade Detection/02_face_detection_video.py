import cv2

# cap = cv2.VideoCapture("gallery/faces.mp4")
cap = cv2.VideoCapture(0)
face_cascade = cv2.CascadeClassifier("Haar Cascade/frontalface.xml")

while True:
    ret, frame = cap.read()
    frame = cv2.flip(frame, 1)  # for webcam
    gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)
    faces = face_cascade.detectMultiScale(gray, 1.3, 5)

    for (x, y, w, h) in faces:
        cv2.rectangle(frame, (x, y), (x+w, y+h), (0, 255, 0), 3)

    cv2.imshow("Video", frame)

    if cv2.waitKey(5) & 0xFF == ord("q"):
        break


cap.release()
cv2.destroyAllWindows()
