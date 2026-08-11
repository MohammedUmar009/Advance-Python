import cv2

camera = cv2.VideoCapture(0)

if not camera.isOpened():
    print("ERROR: Camera is not opening")
    exit()

print("Camera is open!")
print("H = Horizontal Flip")
print("V = Vertical Flip")
print("B = Both Flip")
print("N = Normal")
print("Q = Quit")

flip = 0

while True:
    ret, frame = camera.read()

    if not ret:
        print("ERROR: Cannot read camera")
        break

    if flip == 1:
        frame = cv2.flip(frame, 1)

    elif flip == 2:
        frame = cv2.flip(frame, 0)

    elif flip == 3:
        frame = cv2.flip(frame, -1)

    cv2.imshow("Camera", frame)

    key = cv2.waitKey(1) & 0xFF

    if key == ord("h"):
        flip = 1

    elif key == ord("v"):
        flip = 2

    elif key == ord("b"):
        flip = 3

    elif key == ord("n"):
        flip = 0

    elif key == ord("q"):
        break

camera.release()
cv2.destroyAllWindows()