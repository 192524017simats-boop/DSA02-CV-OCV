# Computer Vision Lab
# Requires: Python 3.x, OpenCV, NumPy
# Install once:
#     pip install opencv-python numpy

import cv2
import numpy as np
from pathlib import Path

video_path = Path(__file__).resolve().parents[1] / "sample_video.avi"
cap = cv2.VideoCapture(str(video_path))

while True:
    ret, frame = cap.read()
    if not ret:
        break
    h, w = frame.shape[:2]
    src = np.float32([[20,20], [w-20,20], [w-20,h-20], [20,h-20]])
    dst = np.float32([[50,40], [w-50,70], [w-70,h-40], [70,h-20]])
    H = cv2.getPerspectiveTransform(src, dst)
    result = cv2.warpPerspective(frame, H, (w, h))
    cv2.imshow("Perspective Video", result)
    if cv2.waitKey(30) & 0xFF == ord("q"):
        break

cap.release()
cv2.destroyAllWindows()
