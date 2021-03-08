import cv2 as cv 
import numpy as np

### TARGET: reduce noise using erode/dilate

img = cv.imread("data/images/sea.jpg")
cv.imshow("Image", img)

# Transform to HSV to achieve greater accuracy
hsv = cv.cvtColor(img, cv.COLOR_BGR2HSV)

mask = cv.inRange(hsv, (30, 50, 10), (90, 255, 255))

cv.imshow("Mask", mask)

# Firstly we dilate just to achieve connectivity in needed component
# Secondly erode with greater value to erase outside noises
# Thirdly return our component to the inital shape using dilate with small value
kernel_dilate = np.ones((5, 5), np.uint8)
kernel_erode = np.ones((7, 7), np.uint8)
kernel_post_dilate = np.ones((3, 3), np.uint8)
mask_denoised = cv.dilate(cv.erode(cv.dilate(mask, kernel_dilate), kernel_erode), kernel_post_dilate)

cv.imshow("Denoised mask", mask_denoised)

cv.waitKey(0)
