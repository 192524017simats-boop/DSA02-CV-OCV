# Computer Vision Lab
# Requires: Python 3.x, OpenCV, NumPy
# Install once:
#     pip install opencv-python numpy

import cv2
from pathlib import Path

image = cv2.imread(str(Path(__file__).resolve().parents[1] / "sample_image.jpg"))
blur = cv2.GaussianBlur(image, (15, 15), 0)
cv2.imwrite("gaussian_blur.jpg", blur)
cv2.imshow("Original", image)
cv2.imshow("Gaussian Blur", blur)
cv2.waitKey(0)
cv2.destroyAllWindows()
