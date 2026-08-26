# Computer Vision Lab
# Requires: Python 3.x, OpenCV, NumPy
# Install once:
#     pip install opencv-python numpy

import cv2
import numpy as np
from pathlib import Path

image = cv2.imread(str(Path(__file__).resolve().parents[1] / "sample_image.jpg"))
h, w = image.shape[:2]
src = np.float32([[50,50], [w-50,50], [50,h-50]])
dst = np.float32([[20,80], [w-100,40], [100,h-40]])
M = cv2.getAffineTransform(src, dst)
result = cv2.warpAffine(image, M, (w, h))
cv2.imwrite("affine.jpg", result)
cv2.imshow("Affine Transformation", result)
cv2.waitKey(0)
cv2.destroyAllWindows()
