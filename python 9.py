import cv2

# Read video from file
video = cv2.VideoCapture(
    r"C:\Users\mu261\OneDrive\Desktop\Advance Python\video.mp4"
)

while video.isOpened():

    ret, frame = video.read()

    if not ret:
        break

    cv2.imshow("Video Player", frame)

    # Press Q to exit
    if cv2.waitKey(25) & 0xFF == ord('q'):
        break

video.release()
cv2.destroyAllWindows()