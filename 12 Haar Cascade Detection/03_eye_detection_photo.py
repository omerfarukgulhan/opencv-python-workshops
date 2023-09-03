import cv2

img = cv2.imread("gallery/face.png")
face_cascade = cv2.CascadeClassifier("Haar Cascade/frontalface.xml")
eye_cascade = cv2.CascadeClassifier("Haar Cascade/eye.xml")

gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)

faces = face_cascade.detectMultiScale(gray, 1.3, 5)

for (x, y, w, h) in faces:
    cv2.rectangle(img, (x, y), (x+w, y+h), (0, 255, 255), 3)

img2 = img[y:y+h, x:x+h]
gray2 = gray[y:y+h, x:x+h]

eyes = eye_cascade.detectMultiScale(gray2)

for (ex, ey, ew, eh) in eyes:
    cv2.rectangle(img2, (ex, ey), (ex+ew, ey+eh), (255, 255, 0), 1)

cv2.imshow("img", img)
cv2.waitKey(0)
cv2.destroyAllWindows()
