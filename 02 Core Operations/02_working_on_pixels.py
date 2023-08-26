import cv2
import numpy as np
import matplotlib.pyplot as plt

file = "test_images/plant.png"
img = cv2.imread(file)

corner = img[0:100, 0:250]  # [y,x]
img[0:100, 0:250] = (255, 255, 0)

cv2.imshow("Forest", img)
cv2.imshow("Corner", corner)

cv2.waitKey(0)
cv2.destroyAllWindows()
