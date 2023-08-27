import cv2
import numpy as np

canvas = np.zeros((512, 512, 3), dtype="uint8") + 255

cv2.putText(canvas,"OpenCV",(0,256),cv2.FONT_ITALIC,2,(0,0,0),cv2.LINE_4)

cv2.imshow("Canvas", canvas)
cv2.waitKey(0)
cv2.destroyAllWindows()
