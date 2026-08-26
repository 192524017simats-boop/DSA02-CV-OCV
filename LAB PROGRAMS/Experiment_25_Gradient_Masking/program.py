# Computer Vision Lab
# Requires: Python 3.x, OpenCV, NumPy
# Install once:
#     pip install opencv-python numpy

import cv2
import numpy as np
from pathlib import Path

image = cv2.imread(str(Path(__file__).resolve().parents[1] / "sample_image.jpg"))
gray = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)
gx = cv2.Sobel(gray, cv2.CV_32F, 1, 0, ksize=3)
gy = cv2.Sobel(gray, cv2.CV_32F, 0, 1, ksize=3)
magnitude = cv2.magnitude(gx, gy)
magnitude = cv2.normalize(magnitude, None, 0, 255, cv2.NORM_MINMAX).astype(np.uint8)
result = cv2.addWeighted(image, 1.0, cv2.cvtColor(magnitude, cv2.COLOR_GRAY2BGR), 0.7, 0)
cv2.imwrite("gradient_masking.jpg", result)
cv2.imshow("Gradient Masking", result)
cv2.waitKey(0)
cv2.destroyAllWindows()
