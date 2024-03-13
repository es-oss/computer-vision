#فتح وعرض صوره نخصص زر لاغلاق البرنامج وز لحفظ الصوره

import cv2

img = cv2.imread('images/car.jpg',0)

cv2.imshow('eslam', img)

k = cv2.waitKey(0)

if k == ord('q') :
    cv2.destroyAllWindows()
elif k == ord('s'):
    cv2.imwrite('F:\\graycar.jpg', img)   
    cv2.destroyWindow() 


