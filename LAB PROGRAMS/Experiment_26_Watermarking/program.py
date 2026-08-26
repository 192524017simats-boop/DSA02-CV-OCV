# Computer Vision Lab
# Requires: Python 3.x, OpenCV, NumPy
# Install once:
#     pip install opencv-python numpy

import cv2
from pathlib import Path

image = cv2.imread(str(Path(__file__).resolve().parents[1] / "sample_image.jpg"))
watermark = image.copy()
cv2.putText(watermark, "COMPUTER VISION LAB", (80, 550),
            cv2.FONT_HERSHEY_SIMPLEX, 1.2, (255,255,255), 3, cv2.LINE_AA)
cv2.imwrite("watermarked.jpg", watermark)
cv2.imshow("Watermarked Image", watermark)
cv2.waitKey(0)
cv2.destroyAllWindows()
