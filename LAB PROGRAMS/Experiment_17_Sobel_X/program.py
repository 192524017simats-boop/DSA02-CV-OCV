# Computer Vision Lab
# Requires: Python 3.x, OpenCV, NumPy
# Install once:
#     pip install opencv-python numpy

import cv2
from pathlib import Path

image = cv2.imread(str(Path(__file__).resolve().parents[1] / "sample_image.jpg"), 0)
sobel_x = cv2.Sobel(image, cv2.CV_64F, 1, 0, ksize=3)
sobel_x = cv2.convertScaleAbs(sobel_x)
cv2.imwrite("sobel_x.jpg", sobel_x)
cv2.imshow("Sobel X", sobel_x)
cv2.waitKey(0)
cv2.destroyAllWindows()
