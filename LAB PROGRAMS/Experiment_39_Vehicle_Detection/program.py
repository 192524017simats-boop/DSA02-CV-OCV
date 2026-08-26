# Computer Vision Lab
# Requires: Python 3.x, OpenCV, NumPy
# Install once:
#     pip install opencv-python numpy

import cv2

# Uses OpenCV's HOG people detector as a simple vehicle/road-scene detection demo.
# It is not a dedicated vehicle detector; for higher accuracy, a trained vehicle model is required.
hog = cv2.HOGDescriptor()
hog.setSVMDetector(cv2.HOGDescriptor_getDefaultPeopleDetector())

cap = cv2.VideoCapture(0)
if not cap.isOpened():
    raise SystemExit("Camera could not be opened.")

while True:
    ret, frame = cap.read()
    if not ret:
        break
    boxes, weights = hog.detectMultiScale(frame, winStride=(8,8), padding=(8,8), scale=1.05)
    for (x,y,w,h) in boxes:
        cv2.rectangle(frame, (x,y), (x+w,y+h), (0,255,0), 2)
    cv2.imshow("Detection Demo - press q to quit", frame)
    if cv2.waitKey(1) & 0xFF == ord("q"):
        break

cap.release()
cv2.destroyAllWindows()
