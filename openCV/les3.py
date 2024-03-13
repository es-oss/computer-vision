#عرض الصور ابعاد الصور والبكسلات imginfo

import cv2

img = cv2.imread('images/car.jpg')

pixels = img.size
dimensions = img.shape
cv2.imshow('eslam', img)
print("number of pixels:", pixels)
print("dimensions :", dimensions)
cv2.waitKey(0)
