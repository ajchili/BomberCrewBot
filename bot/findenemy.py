import os
import cv2
import numpy as np

ENEMY_NIGHT_LOWER = np.array([60, 100, 200], np.uint8)
ENEMY_NIGHT_UPPER = np.array([70, 160, 255], np.uint8)

# noinspection PyArgumentList
# for some dumb reason relative paths aren't working for this...
cap = cv2.VideoCapture(r'C:\Users\brian\PycharmProjects\BomberCrewBot\enemyspotting.avi')
while(cap.isOpened()):
    ret, frame = cap.read()
    hsv = cv2.cvtColor(frame, cv2.COLOR_BGR2HSV)
    hsv2 = cv2.inRange(hsv, ENEMY_NIGHT_LOWER, ENEMY_NIGHT_UPPER)
    cv2.imshow('spotter', hsv2)
    cv2.imshow('video', frame)
    cv2.moveWindow('spotter', 0, 0)
    cv2.moveWindow('video', 960, 0)
    # changing waitkey interval changes playblack speed.
    if cv2.waitKey(25) & 0xFF == ord('q'):
        break

cap.release()
cv2.destroyAllWindows()
