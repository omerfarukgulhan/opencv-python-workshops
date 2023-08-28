import cv2
import numpy as np

img_filter = cv2.imread("gallery/filter.png")
img_median = cv2.imread("gallery/median.png")
img_bilateral = cv2.imread("gallery/bilateral.png")

blur = cv2.blur(img_filter, (5, 5))
blur_g = cv2.GaussianBlur(img_filter, (5, 5), cv2.BORDER_DEFAULT)

blur_m = cv2.medianBlur(img_median, 5)

blur_g = cv2.bilateralFilter(img_bilateral, 9, 75, 75)

cv2.imshow("Original", img_filter)
cv2.imshow("Blue", blur)

cv2.waitKey(0)
cv2.destroyAllWindows()
