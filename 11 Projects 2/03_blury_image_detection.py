import cv2

img = cv2.imread("gallery\starwars.jpg")
blurry_img = cv2.medianBlur(img, 5)

laplacian = cv2.Laplacian(blurry_img, cv2.CV_64F).var()

if laplacian < 500:
    print("blury image")

cv2.imshow("img", img)
cv2.imshow("blury img", blurry_img)
cv2.waitKey(0)
cv2.destroyAllWindows()
