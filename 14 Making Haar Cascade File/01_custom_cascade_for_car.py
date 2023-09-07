import cv2

cap = cv2.VideoCapture("gallery\car.mp4")

car_cascade = cv2.CascadeClassifier("Haar Cascade\car_cascade.xml")

while True:
    ret, frame = cap.read()

    frame = cv2.resize(frame, (640, 480))
    gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)
    cars = car_cascade.detectMultiScale(gray, 1.3, 3)

    for (x, y, w, h) in cars:
        cv2.rectangle(frame, (x, y), (x+w, y+h), (0, 0, 255), 3)

    cv2.imshow("video", frame)

    if cv2.waitKey(5) & 0xFF == ord("q"):
        break


cap.release()
cv2.destroyAllWindows()
