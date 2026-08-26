# Computer Vision Lab
# Requires: Python 3.x, OpenCV, NumPy
# Install once:
#     pip install opencv-python numpy

import cv2
from pathlib import Path

video_path = Path(__file__).resolve().parents[1] / "sample_video.avi"
cap = cv2.VideoCapture(str(video_path))
frames = []

while True:
    ret, frame = cap.read()
    if not ret:
        break
    frames.append(frame)
cap.release()

print("Playing video in reverse. Press q to quit.")
for frame in reversed(frames):
    cv2.imshow("Reverse Video", frame)
    if cv2.waitKey(30) & 0xFF == ord("q"):
        break
cv2.destroyAllWindows()
