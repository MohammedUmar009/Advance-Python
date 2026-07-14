import cv2
import numpy as np

# Create a white canvas
img = np.ones((500, 500, 3), dtype=np.uint8) * 255

# Variables
start_point = None

# Mouse callback
def draw_rectangle(event, x, y, flags, param):
    global start_point, img

    # First click
    if event == cv2.EVENT_LBUTTONDOWN:
        start_point = (x, y)

    # Second click
    elif event == cv2.EVENT_LBUTTONUP:
        end_point = (x, y)

        # Draw start and end points
        cv2.circle(img, start_point, 4, (0, 0, 255), -1)
        cv2.circle(img, end_point, 4, (0, 0, 255), -1)

        # Draw rectangle
        cv2.rectangle(img, start_point, end_point, (255, 0, 0), 2)

        # Reset for next rectangle
        start_point = None


cv2.namedWindow("Draw Rectangle")
cv2.setMouseCallback("Draw Rectangle", draw_rectangle)

while True:
    cv2.imshow("Draw Rectangle", img)

    key = cv2.waitKey(1) & 0xFF

    # Reset
    if key == ord('r'):
        img = np.ones((500, 500, 3), dtype=np.uint8) * 255

    # Quit
    elif key == ord('q'):
        break

cv2.destroyAllWindows()