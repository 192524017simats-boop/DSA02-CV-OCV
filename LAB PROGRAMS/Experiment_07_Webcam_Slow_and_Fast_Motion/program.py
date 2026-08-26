# Computer Vision Lab
# Requires: Python 3.x, OpenCV, NumPy
# Install once:
#     pip install opencv-python numpy

import cv2

cap = cv2.VideoCapture(0)
if not cap.isOpened():
    raise SystemExit("Web camera could not be opened.")

print("Press q to quit.")
print("Press s for slow motion and f for fast motion.")

delay = 1
while True:
    ret, frame = cap.read()
    if not ret:
        break
    cv2.imshow("Web Camera", frame)
    key = cv2.waitKey(delay) & 0xFF
    if key == ord("q"):
        break
    if key == ord("s"):
        delay = 80
    elif key == ord("f"):
        delay = 1

cap.release()
cv2.destroyAllWindows()
