import cv2
import numpy as np

# 1. Load Image
img = cv2.imread('images/image.png')

# 2. Convert to Grayscale for intensity
gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)

# 3. Define threshold x (e.g., 200)
threshold_value = 180

# 4. Apply threshold: pixels > x become 255, else 0
_, mask = cv2.threshold(gray, threshold_value, 255, cv2.THRESH_BINARY)
# 5. Optional: Highlight on original image
highlighted = img.copy()
highlighted[mask == 255] = [255, 0, 220] # Mark in Red

cv2.imshow('Mask', mask)
cv2.imshow('Highlighted', highlighted)
cv2.waitKey(0)
cv2.destroyAllWindows()



