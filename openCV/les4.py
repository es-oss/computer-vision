#تغير حجم الصوره والنافذه

import cv2

img = cv2.imread('images/baby.jpg')

new_img = cv2.resize(img, (200, 200))

cv2.imshow('size img', new_img)

cv2.waitKey(0)

