import cv2
# haar cascade doesnt work properly on humans and cars

img = cv2.imread("gallery\car.jpg")
car_cascade = cv2.CascadeClassifier("Haar Cascade\car.xml")


gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
cars = car_cascade.detectMultiScale(gray, 1.1, 1)

for (x, y, w, h) in cars:
    cv2.rectangle(img, (x, y), (x+w, x+h), (0, 0, 255), 3)

cv2.imshow("img", img)

cv2.waitKey()
cv2.destroyAllWindows()
