import cv2

camera = cv2.VideoCapture(0)

while True:
    ret, frame = camera.read()

    if not ret:
        print("Failed to grab frame")
        break

    cv2.imshow("Web Camera", frame)

    # Press Q to exit
    if cv2.waitKey(1) == ord('q'):
        break

camera.release()
cv2.destroyAllWindows()