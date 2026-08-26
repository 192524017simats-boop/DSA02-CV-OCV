# Computer Vision Lab
# Requires: Python 3.x, OpenCV, NumPy
# Install once:
#     pip install opencv-python numpy

import cv2
from pathlib import Path

image = cv2.imread(str(Path(__file__).resolve().parents[1] / "sample_image.jpg"))
clockwise = cv2.rotate(image, cv2.ROTATE_90_CLOCKWISE)
counter = cv2.rotate(image, cv2.ROTATE_90_COUNTERCLOCKWISE)
cv2.imwrite("clockwise.jpg", clockwise)
cv2.imwrite("counter_clockwise.jpg", counter)
cv2.imshow("Clockwise", clockwise)
cv2.imshow("Counter Clockwise", counter)
cv2.waitKey(0)
cv2.destroyAllWindows()
