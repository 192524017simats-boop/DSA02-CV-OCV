# Computer Vision Lab
# Requires: Python 3.x, OpenCV, NumPy
# Install once:
#     pip install opencv-python numpy

import cv2
from pathlib import Path

img_path = Path(__file__).resolve().parents[1] / "sample_image.jpg"
image = cv2.imread(str(img_path))
gray = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)
cv2.imwrite("grayscale.jpg", gray)
cv2.imshow("Original", image)
cv2.imshow("Grayscale", gray)
cv2.waitKey(0)
cv2.destroyAllWindows()
