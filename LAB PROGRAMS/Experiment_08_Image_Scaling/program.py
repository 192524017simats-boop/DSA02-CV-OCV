# Computer Vision Lab
# Requires: Python 3.x, OpenCV, NumPy
# Install once:
#     pip install opencv-python numpy

import cv2
from pathlib import Path

image = cv2.imread(str(Path(__file__).resolve().parents[1] / "sample_image.jpg"))
bigger = cv2.resize(image, None, fx=1.5, fy=1.5, interpolation=cv2.INTER_LINEAR)
smaller = cv2.resize(image, None, fx=0.5, fy=0.5, interpolation=cv2.INTER_AREA)
cv2.imwrite("bigger.jpg", bigger)
cv2.imwrite("smaller.jpg", smaller)
cv2.imshow("Original", image)
cv2.imshow("Bigger", bigger)
cv2.imshow("Smaller", smaller)
cv2.waitKey(0)
cv2.destroyAllWindows()
