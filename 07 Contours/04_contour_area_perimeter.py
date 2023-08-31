import cv2
import numpy as np

img = cv2.imread("gallery\contour.png")
gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)

ret, thresh = cv2.threshold(gray, 127, 255, cv2.THRESH_BINARY)
contours, hierarchy = cv2.findContours(
    thresh, cv2.RETR_TREE, cv2.CHAIN_APPROX_SIMPLE)

cnt = contours[0]
M = cv2.moments(cnt)
area = cv2.contourArea(cnt)
perimeter = cv2.arcLength(cnt, True)

print(area)
print(M["m00"])
print(perimeter)

"""cv2.imshow("img",img)
cv2.waitKey(0)
cv2.destroyAllWindows()"""
