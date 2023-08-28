import cv2
import numpy as np

circle = np.zeros((512, 512, 3), np.uint8) + 255
cv2.circle(circle, (256, 256), 60, (255, 0, 0), -1)

recantgle = np.zeros((512, 512, 3), np.uint8) + 255
cv2.rectangle(recantgle, (150, 150), (350, 350), (0, 0, 255), -1)

dst = cv2.addWeighted(circle, 0.7, recantgle, 0.3,0)

print(recantgle[160,160])
print(circle[160,160])
print(255*3/10)
print(255*7/10)
print(dst[160,160])
print(dst[255,255])

cv2.imshow("Circle", circle)
cv2.imshow("Rectangel", recantgle)
cv2.imshow("DST", dst)
cv2.waitKey(0)
cv2.destroyAllWindows()
