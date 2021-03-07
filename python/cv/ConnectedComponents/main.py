import cv2 as cv 
import numpy as np

### This time, we need to show the biggest one bubble

img = cv.imread("data/images/bubbles.jpg")
cv.imshow("Not transformed", img)

# Mask for all blue pixels
threshold_first = cv.inRange(img, (50, 50, 0), (255, 255, 100))

# But it marks not all needed pixels, so lets add one more region using or operation
threshold_second = cv.inRange(img, (100, 100, 160), (255, 255, 220))

# For each threshold_first.shape must be equal to threshold_second.shape
# And then we will get image, where each pixel equals to the bitwise_or of the two corresponding pixels of source images 
thresh = cv.bitwise_or(threshold_first, threshold_second)

cv.imshow("Threshold", thresh)

# That function makes a lot of things
# Firstly, in labels there are all objects on the picture marked with their IDs (they can be choosen randomly, so initially we don`t know them)
# Secondly, in stats there are some information about each ID, and it consists of a bunch of stuff, e.g. area of component
# Thirdly, centroids consist of the coordinates of centroids of each component (obviously) 
retval, labels, stats, centroids = cv.connectedComponentsWithStats(thresh)

# Zero label is always background, so lets remove it from stats and centroids
# Because otherwise out method will think that background is the biggest bubble, which is wrong

stats = np.delete(stats, 0, 0)
centroids = np.delete(centroids, 0, 0)

if len(stats) == 0:
    print("Empty mask found during CC")

# Then lets merge our stats and centroids lists to one, because it makes more sense (centroid is also information of the component)
# At this stage we can also extract from stats only needed data (area of the component)
# Also do not forget about adding one to the ID of the component, because we have deleted the background component already
# Actually we do not need centroids here, but lets add them as an example
cc_data = [[i + 1, stats[i, cv.CC_STAT_AREA], centroids[i]] for i in range(len(centroids))]

# Then sort cc_data by decreasing order of area of the component
cc_data.sort(key = lambda x: -x[1])

component_index = 0 # First element is the biggest one component
component = cc_data[component_index]

# Structure of the component [id, area, centroid]
# We need to get an ID, so
component_id = component[0]

# And then we need to make a mask, using our labels
mask = (labels == component_id)

# But our mask have only True/False, it is boolean. We need to make it showable
# It can be simply done by setting type of the array to uint8, and then multiplying to 255
# Google type punning or каламбур типизации, if you wondering why it is working
mask.dtype = np.uint8
mask *= 255

cv.imshow("Mask", mask)

# At the at we need to apply this mask on the image
# Lets think about how to apply mask
# We can use bitwise_and or some other functions, but it is boring
# So lets try to do it using numpy operations
# We need to make the mask 0 outside the bubble, and 1 inside, and then multiply initial image to it
# There is a problem, mask and image have different shapes (height, width, 3) and (height, width), so numpy just do not know how to multiply them
# We can use reshape to fix this
# Reshape makes mask shape equal to (height, width, 1) which has the same number of dimensions as the img, so numpy can multiply them

if True: # Good way, using functions
    result = cv.bitwise_and(img, img, mask=mask)
else: # Weird way, just to practice
    result = img * (mask != 0).reshape((img.shape[0], img.shape[1], 1))

# Show the result
cv.imshow("Biggest bubble", result)

cv.waitKey(0)