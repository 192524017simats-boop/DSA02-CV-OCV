# Computer Vision Lab
# Requires: Python 3.x, OpenCV, NumPy
# Install once:
#     pip install opencv-python numpy

import cv2
import numpy as np
from pathlib import Path

image = cv2.imread(str(Path(__file__).resolve().parents[1] / "sample_image.jpg"))
h, w = image.shape[:2]
M = np.float32([[1, 0, 100], [0, 1, 60]])
translated = cv2.warpAffine(image, M, (w, h))
cv2.imwrite("translated.jpg", translated)
cv2.imshow("Translated Image", translated)
cv2.waitKey(0)
cv2.destroyAllWindows()
