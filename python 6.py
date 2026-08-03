import cv2

# Read the image
img = cv2.imread("image.jpg")

if img is None:
    print("Image not found!")
else:
    # Get image height, width, and channels
    height, width, channels = img.shape

    # Display image resolution on the image
    text = f"Resolution: {width} x {height}"

    cv2.putText(img, text, (20, 30),
                cv2.FONT_HERSHEY_SIMPLEX,
                0.8, (0, 255, 0), 2)

    print("Width :", width)
    print("Height:", height)
    print("Channels:", channels)

    cv2.imshow("Pixels and Image Resolution", img)
    cv2.waitKey(0)
    cv2.destroyAllWindows()