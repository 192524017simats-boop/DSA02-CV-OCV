# Computer Vision Lab
# Requires: Python 3.x, OpenCV, NumPy
# Install once:
#     pip install opencv-python numpy

import cv2
from pathlib import Path

image = cv2.imread(str(Path(__file__).resolve().parents[1] / "sample_image.jpg"))
blur = cv2.GaussianBlur(image, (0,0), 3)
result = cv2.addWeighted(image, 1.5, blur, -0.5, 0)
cv2.imwrite("unsharp_masking.jpg", result)
cv2.imshow("Unsharp Masking", result)
cv2.waitKey(0)
cv2.destroyAllWindows()
