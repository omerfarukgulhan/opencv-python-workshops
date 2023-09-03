import cv2
# haar cascade doesnt work properly on humans and cars
img = cv2.imread("gallery/body.jpg")

body_cascade = cv2.CascadeClassifier("Haar Cascade/fullbody.xml")

gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
bodies = body_cascade.detectMultiScale(gray, 1.1, 3)

for (x, y, w, h) in bodies:
    cv2.rectangle(img, (x, y), (x+w, y+h), (0, 255, 255), 3)

cv2.imshow("img", img)
cv2.waitKey(0)
cv2.destroyAllWindows()
