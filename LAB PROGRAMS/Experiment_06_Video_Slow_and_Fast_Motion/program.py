# Computer Vision Lab
# Requires: Python 3.x, OpenCV, NumPy
# Install once:
#     pip install opencv-python numpy

import cv2
from pathlib import Path

video_path = Path(__file__).resolve().parents[1] / "sample_video.avi"
cap = cv2.VideoCapture(str(video_path))

print("Press q to quit.")
print("Slow motion: every frame is displayed with a longer delay.")
print("Fast motion: every second frame is skipped.")

while True:
    ret, frame = cap.read()
    if not ret:
        break
    cv2.imshow("Slow Motion", frame)
    if cv2.waitKey(100) & 0xFF == ord("q"):
        break

cap.release()
cv2.destroyAllWindows()

cap = cv2.VideoCapture(str(video_path))
while True:
    ret, frame = cap.read()
    if not ret:
        break
    cv2.imshow("Fast Motion", frame)
    if cv2.waitKey(10) & 0xFF == ord("q"):
        break
    cap.grab()  # skip one frame
cap.release()
cv2.destroyAllWindows()
