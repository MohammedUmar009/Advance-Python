import cv2

camera = cv2.VideoCapture(0)

while True:
    ret, frame = camera.read()

    if not ret:
        break

    h, w = frame.shape[:2]

    # Draw diagonal line
    cv2.line(frame, (0, 0), (w, h), (0, 255, 0), 3)

    # Draw horizontal line
    cv2.line(frame, (0, h//2), (w, h//2), (255, 0, 0), 2)

    cv2.imshow("Drawing Lines on Video", frame)

    if cv2.waitKey(1) & 0xFF == ord('q'):
        break

camera.release()
cv2.destroyAllWindows()