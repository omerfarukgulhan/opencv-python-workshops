import cv2
import numpy as np
import matplotlib.pyplot as plt

file = "test_images/opencv_logo.png"
img = cv2.imread(file)

(B, G, R) = cv2.split(img)
merged = cv2.merge([B, G, R])

black = np.zeros(img.shape[:2], dtype="uint8")

cv2.imshow("OpenCV", img)
cv2.imshow("Red", cv2.merge([black, black, R]))
cv2.imshow("Green", cv2.merge([black, G, black]))
cv2.imshow("Blue", cv2.merge([B, black, black]))

# cv2.imshow("OpenCV", img)
# cv2.imshow("OpenCV-Merged", merged)
# cv2.imshow("OpenCV-B", B)
# cv2.imshow("OpenCV-G", G)
# cv2.imshow("OpenCV-R", R)

cv2.waitKey(0)
cv2.destroyAllWindows()
