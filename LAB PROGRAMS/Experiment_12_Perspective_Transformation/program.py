# Computer Vision Lab
# Requires: Python 3.x, OpenCV, NumPy
# Install once:
#     pip install opencv-python numpy

import cv2
import numpy as np
from pathlib import Path

image = cv2.imread(str(Path(__file__).resolve().parents[1] / "sample_image.jpg"))
h, w = image.shape[:2]
src = np.float32([[80,80], [w-80,80], [w-80,h-80], [80,h-80]])
dst = np.float32([[30,40], [w-30,80], [w-80,h-40], [80,h-20]])
H = cv2.getPerspectiveTransform(src, dst)
result = cv2.warpPerspective(image, H, (w, h))
cv2.imwrite("perspective.jpg", result)
cv2.imshow("Perspective Transformation", result)
cv2.waitKey(0)
cv2.destroyAllWindows()
