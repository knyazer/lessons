import cv2 as cv 
import numpy as np

### TARGET: read an image and then show it


# Pixels are in format BGR (blue green red)
# And images presented as width x height x channels

img = cv.imread("data/images/deer.jpg")

print(img.shape) ### (height, width, number of channels)

# You can set pixel value:
img[5][60] = (250, 250, 250)

# Or particular pixel channel:
img[100][100][0] = 0


cv.imshow("Name of the window", img)


# Wait until ESC is pressed (0 means infinite delay, any positive number means delay in ms)
cv.waitKey(0)