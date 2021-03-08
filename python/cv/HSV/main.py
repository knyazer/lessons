import cv2 as cv 
import numpy as np

### TARGET: show hue of the image

img = cv.imread("data/images/landscape.jpg")
cv.imshow("Not transformed", img)

# Transform image from the BGR to the HSV colorspace
hsv = cv.cvtColor(img, cv.COLOR_BGR2HSV)

print(hsv.shape) # (height, width, channels) and channels are (hue, saturation, value)

# Show only hue
cv.imshow("Hue", hsv[:, :, 0])

# As you can see, HSV is very useful when colors are normal
# But it becomes useless when colors are dark or very light
# So use it with attention, in several situations it can produce weird values

cv.waitKey(0)