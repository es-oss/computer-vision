#نظام الالوان في الصوره

import cv2

img = cv2.imread('images/baby.jpg')

gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)

cv2.imshow('eslam', gray)

cv2.waitKey(0)
