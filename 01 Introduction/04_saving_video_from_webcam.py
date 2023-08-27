import cv2

cap = cv2.VideoCapture(0)

file_name = "C:/Users/ÖMERFARUKGÜLHAN/Desktop/udemy/opencv-projects/gallery/video.avi"
codec = cv2.VideoWriter_fourcc('W', 'M', 'V', '2')
frame_rate = 30
resolution = (640, 480)

video_file_output = cv2.VideoWriter(file_name, codec, frame_rate, resolution)

while True:
    ret, frame = cap.read()
    video_file_output.write(frame)
    cv2.imshow("Video", frame)

    if cv2.waitKey(30) & 0xFF == ord("q"):
        break

video_file_output.release()
cap.release()
cv2.destroyAllWindows()
