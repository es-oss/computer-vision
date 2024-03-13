#عرض الفديوهات في البرنامج

import cv2

cam = cv2.VideoCapture('video/apple.mp4')

while True:
    ret, frame = cam.read()
    gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)
    size = cv2.resize(frame, (400,300))
    cv2.imshow('eslam', size)




    if cv2.waitKey(1) & 0xff == ord('q'):
        break

