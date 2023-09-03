import cv2
import numpy as np


def nothing(x):
    pass


img1 = cv2.imread("gallery/aircraft.jpg")
img2 = cv2.imread("gallery/balls.jpg")

img1 = cv2.resize(img1, (640, 480))
img2 = cv2.resize(img2, (640, 480))

output = cv2.addWeighted(img1, 0.5, img2, 0.5, 0)
windowName = "Transition Program"
cv2.namedWindow(windowName)

cv2.createTrackbar("Alpha-Beta", windowName, 0, 1000, nothing)

while True:
    cv2.imshow(windowName, output)
    alpha = cv2.getTrackbarPos("Alpha-Beta", windowName)/1000
    beta = 1-alpha
    output = cv2.addWeighted(img1, alpha, img2, beta, 0)

    if cv2.waitKey(80) & 0xFF == ord('q'):
        break

cv2.destroyAllWindows()
