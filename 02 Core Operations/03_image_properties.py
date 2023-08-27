import cv2
import numpy as np
import matplotlib.pyplot as plt

file = "gallery\opencv_logo.png"
img = cv2.imread(file)

print(img.shape)  # height, width, channel
# channel = 3, colored
# channel = 1 = no output, grayscale

print("Image size: {}".format(img.size))
# size = height*width*channel
# for gray photos height*width

cv2.imshow("OpenCV", img)
cv2.waitKey(0)
cv2.destroyAllWindows()
