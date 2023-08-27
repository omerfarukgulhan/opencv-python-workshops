import cv2
import numpy as np

canvas = np.zeros((512, 512, 3), dtype=np.uint8) + 255

cv2.line(canvas, (0, 0), (512, 512), (255, 0, 0), thickness=5)
cv2.line(canvas, (512, 0), (0, 512), (0, 255, 0), thickness=5)

cv2.rectangle(canvas, (100, 100), (200, 200), (0, 0, 255), thickness=-1)
cv2.rectangle(canvas, (300, 300), (400, 400), (0, 0, 255), thickness=15)

cv2.circle(canvas, (256, 256), 50, (0, 0, 0), thickness=3)

points = np.array([[[0, 50], [100, 450], [450, 500], [220, 350]]], np.int32)
cv2.polylines(canvas, [points], True, (255, 0, 255), 5)

cv2.ellipse(canvas, (300, 300), (100, 50), 0, 0, 360, (255, 255, 0), -1)

cv2.imshow("Canvas", canvas)
cv2.waitKey(0)
cv2.destroyAllWindows()
