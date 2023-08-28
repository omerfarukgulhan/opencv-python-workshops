import cv2
import numpy as np

circle = np.zeros((512, 512, 3), np.uint8) + 255
cv2.circle(circle, (256, 256), 60, (255, 0, 0), -1)

recantgle = np.zeros((512, 512, 3), np.uint8) + 255
cv2.rectangle(recantgle, (150, 150), (350, 350), (0, 0, 255), -1)

combination = cv2.add(recantgle, circle)

cv2.imshow("Circle", circle)
cv2.imshow("Rectangel", recantgle)
cv2.imshow("Combination", combination)
cv2.waitKey(0)
cv2.destroyAllWindows()
