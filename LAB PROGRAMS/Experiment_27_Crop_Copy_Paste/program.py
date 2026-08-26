# Computer Vision Lab
# Requires: Python 3.x, OpenCV, NumPy
# Install once:
#     pip install opencv-python numpy

import cv2
from pathlib import Path

image = cv2.imread(str(Path(__file__).resolve().parents[1] / "sample_image.jpg"))
h, w = image.shape[:2]
crop = image[100:350, 100:350]
result = image.copy()
result[20:270, 20:270] = crop
cv2.imwrite("cropped_copy_paste.jpg", result)
cv2.imshow("Crop Copy Paste", result)
cv2.waitKey(0)
cv2.destroyAllWindows()
