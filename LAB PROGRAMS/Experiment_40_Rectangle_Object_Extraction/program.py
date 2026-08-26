# Computer Vision Lab
# Requires: Python 3.x, OpenCV, NumPy
# Install once:
#     pip install opencv-python numpy

import cv2
from pathlib import Path

image = cv2.imread(str(Path(__file__).resolve().parents[1] / "sample_image.jpg"))
h, w = image.shape[:2]

# Draw a rectangular selection and extract the object/region.
x1, y1, x2, y2 = 100, 100, min(400, w), min(350, h)
output = image.copy()
cv2.rectangle(output, (x1,y1), (x2,y2), (0,255,0), 3)
object_crop = image[y1:y2, x1:x2]

cv2.imwrite("rectangle_selection.jpg", output)
cv2.imwrite("extracted_object.jpg", object_crop)
cv2.imshow("Selected Object", output)
cv2.imshow("Extracted Object", object_crop)
cv2.waitKey(0)
cv2.destroyAllWindows()
