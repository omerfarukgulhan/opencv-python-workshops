import cv2

img = cv2.imread("klon.jpg")

# img = cv2 imread("C:\Users\ÖMERFARUKGÜLHAN\Desktop\klon.jpg")
# img = cv2.imread("klon.jpg",0) #gray
# img = cv2.imread("klon.jpg",IMREAD_GRAYSCALE) #gray
# print(img)

cv2.imwrite("klon1.jpg", img)

cv2.namedWindow("image", cv2.WINDOW_NORMAL)

cv2.imshow("image", img)
cv2.waitKey(0)
cv2.destroyAllWindows()
