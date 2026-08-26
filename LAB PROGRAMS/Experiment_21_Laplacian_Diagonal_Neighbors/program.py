# Computer Vision Lab
# Requires: Python 3.x, OpenCV, NumPy
# Install once:
#     pip install opencv-python numpy

import cv2
import numpy as np
from pathlib import Path

image = cv2.imread(str(Path(__file__).resolve().parents[1] / "sample_image.jpg"))
kernel = np.array([[1,1,1], [1,-8,1], [1,1,1]], dtype=np.float32)
lap = cv2.filter2D(image, cv2.CV_32F, kernel)
result = cv2.convertScaleAbs(image - lap)
cv2.imwrite("laplacian_diagonal.jpg", result)
cv2.imshow("Laplacian with Diagonal Neighbors", result)
cv2.waitKey(0)
cv2.destroyAllWindows()
