import cv2
import numpy

file = "test_images/opencv_logo.png"
img = cv2.imread(file)

px = img[50, 50]
print(px)

(b, g, r) = img[50, 50]
print("red: {}  green: {}   blue:{}".format(r, g, b))
# image output format originally bgr not rgb

# accessing pixels value-1
blue = img[100, 100, 0]
green = img[100, 100, 1]
red = img[100, 100, 2]

# accessing pixels value-2
blue = img.item(10, 10, 2)
green = img.item(10, 10, 2)
red = img.item(10, 10, 2)
print("red: {}  green: {}   blue:{}".format(red, green, blue))
# setting pixel value
img.itemset((10, 10, 2), 100)
