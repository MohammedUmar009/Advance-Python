import cv2

# Open camera
camera = cv2.VideoCapture(0)

if not camera.isOpened():
    print("Camera could not be opened!")
    exit()

flip_mode = 0

print("Camera started.")
print("Press:")
print("H = Horizontal Flip")
print("V = Vertical Flip")
print("B = Horizontal + Vertical Flip")
print("N = Normal Camera")
print("Q = Quit")

while True:

    ret, frame = camera.read()

    if not ret:
        print("Could not read camera.")
        break

    # Apply flip
    if flip_mode == 1:
        frame = cv2.flip(frame, 1)      # Horizontal

    elif flip_mode == 2:
        frame = cv2.flip(frame, 0)      # Vertical

    elif flip_mode == 3:
        frame = cv2.flip(frame, -1)     # Both

    # Show camera
    cv2.imshow("Camera", frame)

    key = cv2.waitKey(1) & 0xFF

    if key == ord('h'):
        flip_mode = 1

    elif key == ord('v'):
        flip_mode = 2

    elif key == ord('b'):
        flip_mode = 3

    elif key == ord('n'):
        flip_mode = 0

    elif key == ord('q'):
        break

camera.release()
cv2.destroyAllWindows()