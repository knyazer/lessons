import cv2 as cv 
import numpy as np

### Lets try to replace all green pixels of spotify logo to black


# Load image
img = cv.imread("data/images/spotify.jpg")

# Show it
cv.imshow("Not transformed", img)

# inRange(src, lowerb, higherb) finds all pixels which satisfies inequality lowerb < pixel <= higherb
mask = cv.inRange(img, (0, 100, 0), (150, 255, 50))

print(mask.shape) # (height, width)

# Show the mask
cv.imshow("Mask", mask)

# Mask is a numpy array, so we can apply many operations on it:
mask = 255 - mask # 0 -> 255, 255 -> 0, so it means that mask is inverted

# And inverted mask is what we want to get
cv.imshow("Inverted mask", mask)

### Wait until ESC is pressed (0 means infinite delay, any positive number means delay in ms)
cv.waitKey(0)