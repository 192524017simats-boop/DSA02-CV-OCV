# Computer Vision Lab
# Requires: Python 3.x, OpenCV, NumPy
# Install once:
#     pip install opencv-python numpy

import cv2
import numpy as np
from pathlib import Path

image = cv2.imread(str(Path(__file__).resolve().parents[1] / "sample_image.jpg"))
gray = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)
kernel = np.array([[-1,-1,-1], [-1,8,-1], [-1,-1,-1]], dtype=np.float32)
boundary = cv2.filter2D(gray, -1, kernel)
boundary = cv2.convertScaleAbs(boundary)
cv2.imwrite("boundary_convolution.jpg", boundary)
cv2.imshow("Boundary using Convolution", boundary)
cv2.waitKey(0)
cv2.destroyAllWindows()
