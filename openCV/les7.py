#التعرف علي الاشياء داخل الصور

import cv2

img = cv2.imread('images/baby.jpg')

# line- rectangle- text
#cv2.line(img, (10,10), (200,10), (0, 255, 0), 6)
cv2.rectangle(img, (100,200),(350,400), (0, 255, 0), 4)



cv2.putText(img, "baby face", (150,200),cv2.FONT_HERSHEY_PLAIN,1, (0,0,255), 2)

cv2.imshow('eslam', img)

cv2.waitKey(0)

