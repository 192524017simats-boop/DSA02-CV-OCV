# Computer Vision Lab
# Requires: Python 3.x, OpenCV, NumPy
# Install once:
#     pip install opencv-python numpy

import cv2
from pathlib import Path

image = cv2.imread(str(Path(__file__).resolve().parents[1] / "sample_image.jpg"))
gray = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)

# This experiment demonstrates general object recognition by template matching.
# Replace watch_template.jpg with a real watch image for actual watch matching.
template_path = Path(__file__).resolve().parents[1] / "watch_template.jpg"
if not template_path.exists():
    print("watch_template.jpg was not provided in the source list.")
    print("Place a cropped watch image with this name in the main project folder to run template matching.")
    cv2.imshow("Given Image", image)
    cv2.waitKey(0)
    cv2.destroyAllWindows()
else:
    template = cv2.imread(str(template_path), 0)
    result = cv2.matchTemplate(gray, template, cv2.TM_CCOEFF_NORMED)
    _, max_val, _, max_loc = cv2.minMaxLoc(result)
    h, w = template.shape
    top_left = max_loc
    bottom_right = (top_left[0] + w, top_left[1] + h)
    output = image.copy()
    cv2.rectangle(output, top_left, bottom_right, (0,255,0), 3)
    print("Best match score:", max_val)
    cv2.imshow("Watch Recognition", output)
    cv2.waitKey(0)
    cv2.destroyAllWindows()
