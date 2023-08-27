import cv2
import numpy as np

canvas = np.zeros((10, 10, 3), dtype="uint8")

"""
canvas = np.zeros((10, 10, 0), dtype="uint8")
canvas[0, 0] = 255
canvas[0, 1] = 150
canvas[0, 2] = 100
canvas[0, 3] = 0
"""

canvas[0, 0] = (255, 255, 255)
canvas[0, 1] = (255, 255, 200)
canvas[0, 2] = (255, 255, 150)
canvas[0, 3] = (255, 255, 100)
canvas[0, 4] = (255, 255, 50)


canvas = cv2.resize(canvas, (1000, 1000), interpolation=cv2.INTER_AREA)

cv2.imshow("Canvas", canvas)
cv2.waitKey(0)
cv2.destroyAllWindows()
