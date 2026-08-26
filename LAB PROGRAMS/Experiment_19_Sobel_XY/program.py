# Computer Vision Lab
# Requires: Python 3.x, OpenCV, NumPy
# Install once:
#     pip install opencv-python numpy

import cv2
from pathlib import Path

image = cv2.imread(str(Path(__file__).resolve().parents[1] / "sample_image.jpg"), 0)
sx = cv2.Sobel(image, cv2.CV_64F, 1, 0, ksize=3)
sy = cv2.Sobel(image, cv2.CV_64F, 0, 1, ksize=3)
xy = cv2.magnitude(sx, sy)
xy = cv2.convertScaleAbs(xy)
cv2.imwrite("sobel_xy.jpg", xy)
cv2.imshow("Sobel XY", xy)
cv2.waitKey(0)
cv2.destroyAllWindows()
