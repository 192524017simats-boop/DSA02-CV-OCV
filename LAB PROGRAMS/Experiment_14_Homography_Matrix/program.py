# Computer Vision Lab
# Requires: Python 3.x, OpenCV, NumPy
# Install once:
#     pip install opencv-python numpy

import cv2
import numpy as np
from pathlib import Path

image = cv2.imread(str(Path(__file__).resolve().parents[1] / "sample_image.jpg"))
h, w = image.shape[:2]
src = np.float32([[60,60], [w-60,60], [w-60,h-60], [60,h-60]])
dst = np.float32([[30,80], [w-30,50], [w-80,h-30], [70,h-40]])
H, _ = cv2.findHomography(src, dst)
result = cv2.warpPerspective(image, H, (w, h))
np.savetxt("homography_matrix.txt", H)
cv2.imwrite("homography_result.jpg", result)
cv2.imshow("Homography Result", result)
cv2.waitKey(0)
cv2.destroyAllWindows()
