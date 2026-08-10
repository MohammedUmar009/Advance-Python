import cv2
import numpy as np

cap = cv2.VideoCapture(0)

# Transparent drawing layer
drawing_layer = None

drawing = False
last_x, last_y = -1, -1


def mouse_draw(event, x, y, flags, param):
    global drawing, last_x, last_y, drawing_layer

    if event == cv2.EVENT_LBUTTONDOWN:
        drawing = True
        last_x, last_y = x, y

    elif event == cv2.EVENT_MOUSEMOVE:
        if drawing:
            cv2.line(
                drawing_layer,
                (last_x, last_y),
                (x, y),
                (0, 0, 255),   # RED
                4
            )
            last_x, last_y = x, y

    elif event == cv2.EVENT_LBUTTONUP:
        drawing = False
        last_x, last_y = -1, -1


cv2.namedWindow("Camera")
cv2.setMouseCallback("Camera", mouse_draw)

while True:

    ret, frame = cap.read()

    if not ret:
        print("Camera not found!")
        break

    # Mirror camera
    frame = cv2.flip(frame, 1)

    # Create drawing layer once
    if drawing_layer is None:
        drawing_layer = np.zeros_like(frame)

    # Put drawing on camera
    output = cv2.add(frame, drawing_layer)

    cv2.imshow("Camera", output)

    # Press C to clear drawings
    key = cv2.waitKey(1) & 0xFF

    if key == ord('c'):
        drawing_layer = np.zeros_like(frame)

    # Press Q to quit
    if key == ord('q'):
        break


cap.release()
cv2.destroyAllWindows()