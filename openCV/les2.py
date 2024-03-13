#عرض الصوره مع بقاء النفاذه شغاله


import cv2 


img = cv2.imread('images/car.jpg')

cv2.imshow('eslam', img)

cv2.waitKey(0)
