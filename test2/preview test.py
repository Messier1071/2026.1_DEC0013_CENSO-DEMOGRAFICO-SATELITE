import cv2

# 1. Load an image or capture video frame
img = cv2.imread('images/image.png',0)
img2 = cv2.imread('images/image.png')

# 2. Create the preview window
# Syntax: cv2.imshow(window_name, image_variable)
cv2.imshow('Preview Window', img2)

# 3. Essential: Wait for a key press
# Without waitKey(0), the window will close instantly
cv2.waitKey(0)

# 4. Clean up
cv2.destroyAllWindows()
