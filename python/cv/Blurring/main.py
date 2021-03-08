import cv2 as cv 
import numpy as np

### TARGET: reduce noise using blurring

img = cv.imread("data/images/castle.jpeg")
cv.imshow("Image", img)

mask = cv.inRange(img, (60, 60, 150), (110, 110, 255))

cv.imshow("Mask", mask)

# Gaussian blur using gaussian convolution or filter to blur the image
# It is one of the best methods to apply blurring, and, probably, the most common
# (5, 5) is a kernel size, should be equal to (kSize, kSize) where is kSize is odd integer number
# Last argument equals to sigma, so zero is like default value for it 
img = cv.GaussianBlur(img, (7, 7), 0)
cv.imshow("Blurred image", img)

mask_blurred = cv.inRange(img, (60, 60, 150), (110, 110, 255))
cv.imshow("Blurred mask", mask_blurred)

cv.waitKey(0)
