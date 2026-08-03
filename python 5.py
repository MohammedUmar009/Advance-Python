import cv2

# Read the image
img = cv2.imread("image.jpg")

# Check if image is loaded
if img is None:
    print("Image not found!")
else:
    cv2.imshow("Image", img)
    cv2.waitKey(0)
    cv2.destroyAllWindows()
    