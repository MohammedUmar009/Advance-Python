import cv2
import numpy as np

# Create a blank color image (300x400)
img = np.zeros((300, 400, 3), dtype=np.uint8)

# Fill each horizontal strip with a different color (BGR format)

img[0:50, :] = (255, 0, 0)       # Blue
img[50:100, :] = (0, 255, 0)      # Green
img[100:150, :] = (0, 0, 255)     # Red
img[150:200, :] = (0, 255, 255)   # Yellow
img[200:250, :] = (255, 255, 0)   # Cyan
img[250:300, :] = (255, 0, 255)   # Magenta

# Display the image
cv2.imshow("Different Colors", img)

cv2.waitKey(0)
cv2.destroyAllWindows()