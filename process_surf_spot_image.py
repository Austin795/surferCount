import matplotlib.pyplot as plt
import numpy as np

import cv2
from imutils.object_detection import non_max_suppression
  
# Reading the image and the template
img = cv2.imread('canoes.png')
temp = cv2.imread('canoesSurfer.png')
  
# save the image dimensions
W, H = temp.shape[:2]
  
# Define a minimum threshold
thresh = 0.65
  
# Converting them to grayscale
img_gray = cv2.cvtColor(img, 
                        cv2.COLOR_BGR2GRAY)
temp_gray = cv2.cvtColor(temp,
                         cv2.COLOR_BGR2GRAY)
  
# Passing the image to matchTemplate method
match = cv2.matchTemplate(
    image=img_gray, templ=temp_gray, 
  method=cv2.TM_CCOEFF_NORMED)
  
# Select rectangles with
# confidence greater than threshold
(y_points, x_points) = np.where(match >= thresh)
  
# initialize our list of rectangles
boxes = list()
  
# loop over the starting (x, y)-coordinates again
for (x, y) in zip(x_points, y_points):
    
    # update our list of rectangles
    boxes.append((x, y, x + W, y + H))
  
# apply non-maxima suppression to the rectangles
# this will create a single bounding box
boxes = non_max_suppression(np.array(boxes))
print(len(boxes))
# loop over the final bounding boxes
for (x1, y1, x2, y2) in boxes:
    
    # draw the bounding box on the image
    cv2.rectangle(img, (x1, y1), (x2, y2),
                  (255, 0, 0), 3)
  
# Show the template and the final output
# plt.imshow("Template", temp)
# plt.imshow("After NMS", img)
plt.imshow(temp),plt.show()
plt.figure(figsize = (15,15))
plt.imshow(img),plt.show()