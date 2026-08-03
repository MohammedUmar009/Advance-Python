import cv2
from datetime import datetime

camera = cv2.VideoCapture(0)

while True:
    ret, frame = camera.read()

    if not ret:
        break

    # Get current date and time
    current_time = datetime.now().strftime("%d-%m-%Y %H:%M:%S")

    # Display date and time on the video
    cv2.putText(frame, current_time, (20, 30),
                cv2.FONT_HERSHEY_SIMPLEX,
                0.7, (0, 255, 0), 2)

    cv2.imshow("Date and Time on Webcam", frame)

    # Press Q to exit
    if cv2.waitKey(1) & 0xFF == ord('q'):
        break

camera.release()
cv2.destroyAllWindows()