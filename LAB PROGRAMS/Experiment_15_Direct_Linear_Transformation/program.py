# Computer Vision Lab
# Requires: Python 3.x, OpenCV, NumPy
# Install once:
#     pip install opencv-python numpy

import cv2
import numpy as np
from pathlib import Path

# DLT estimates a projective transformation from corresponding points.
image = cv2.imread(str(Path(__file__).resolve().parents[1] / "sample_image.jpg"))
h, w = image.shape[:2]

src = np.float64([[60,60], [w-60,60], [w-60,h-60], [60,h-60]])
dst = np.float64([[30,80], [w-30,50], [w-80,h-30], [70,h-40]])

A = []
for (x, y), (u, v) in zip(src, dst):
    A.append([-x, -y, -1, 0, 0, 0, u*x, u*y, u])
    A.append([0, 0, 0, -x, -y, -1, v*x, v*y, v])
A = np.asarray(A)
_, _, Vt = np.linalg.svd(A)
H = Vt[-1].reshape(3, 3)
H = H / H[2, 2]

result = cv2.warpPerspective(image, H, (w, h))
np.savetxt("DLT_homography_matrix.txt", H)
cv2.imwrite("dlt_result.jpg", result)
cv2.imshow("DLT Result", result)
cv2.waitKey(0)
cv2.destroyAllWindows()
