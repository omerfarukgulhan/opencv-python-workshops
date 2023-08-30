import cv2
import numpy as np

img = cv2.imread("gallery/text.png")
img1 = cv2.imread("gallery/contour.png")

gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
gray = np.float32(gray)
corners = cv2.goodFeaturesToTrack(gray, 50, 0.01, 10)
corners = np.int0(corners)

for corner in corners:
    x, y = corner.ravel()
    cv2.circle(img, (x, y), 3, (0, 0, 255), -1)

cv2.imshow("img", img)
# cv2.imshow("img1", img1)
cv2.waitKey(0)
cv2.destroyAllWindows()
