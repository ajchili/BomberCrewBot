import cv2
import numpy as np

ENEMY_NIGHT_LOWER = np.array([55, 100, 200], np.uint8)
ENEMY_NIGHT_UPPER = np.array([70, 160, 255], np.uint8)

SPOTTED_LOWER = np.array([170, 100, 0], np.uint8)
SPOTTED_UPPER = np.array([180, 255, 255], np.uint8)

# noinspection PyArgumentList
# for some dumb reason relative paths aren't working for this...
cap = cv2.VideoCapture(r'C:\Users\brian\PycharmProjects\BomberCrewBot\res\enemyspotting.avi')
while cap.isOpened():
    ret, frame = cap.read()
    hsv = cv2.cvtColor(frame, cv2.COLOR_BGR2HSV)
    hsv2 = cv2.inRange(hsv, ENEMY_NIGHT_LOWER, ENEMY_NIGHT_UPPER)
    median_blur = cv2.medianBlur(hsv2, 5)
    rows = median_blur.shape[0]
    circles = cv2.HoughCircles(median_blur, cv2.HOUGH_GRADIENT, 1, rows / 8, param1=100, param2=11, minRadius=0,
                               maxRadius=6)

    if circles is not None:
        circles = np.uint16(np.around(circles))
        for i in circles[0, :]:
            center = (i[0], i[1])
            # circle center
            cv2.circle(median_blur, center, 1, (0, 100, 100), 3)
            cv2.circle(frame, center, 1, (0, 100, 100), 3)
            # circle outline
            radius = i[2]
            cv2.circle(median_blur, center, radius + 20, (255, 255, 255), 5)
            cv2.circle(frame, center, radius, (0, 255, 255), 1)

            cv2.putText(median_blur, "enemy plane", (i[0], i[1] - 40), cv2.FONT_HERSHEY_SIMPLEX, 0.75, (255, 255, 255),
                        2, cv2.LINE_AA)

            print("enemy plane spotted at:", (i[0], i[1]))
            # TODO: Move mouse to detected plane

    hsv_spotted = cv2.inRange(hsv, SPOTTED_LOWER, SPOTTED_UPPER)
    median_spotted = cv2.medianBlur(hsv_spotted, 5)
    rows_spotted = median_spotted.shape[0]
    circles_spotted = cv2.HoughCircles(median_spotted, cv2.HOUGH_GRADIENT, 1, rows_spotted / 8, param1=100, param2=20,
                                       minRadius=10, maxRadius=30)
    if circles_spotted is not None:
        circles_spotted = np.uint16(np.around(circles_spotted))
        for i in circles_spotted[0, :]:
            spotted_center = (i[0], i[1])
            # circle center
            cv2.circle(median_spotted, spotted_center, 1, (0, 100, 100), 5)
            cv2.circle(frame, spotted_center, 1, (0, 100, 100), 3)
            # circle outline
            radius = i[2]
            cv2.circle(median_spotted, spotted_center, radius + 20, (255, 255, 255), 5)
            cv2.circle(frame, spotted_center, radius, (0, 255, 255), 1)

            cv2.putText(median_spotted, "enemy plane", (i[0], i[1] - 40), cv2.FONT_HERSHEY_SIMPLEX, 0.75,
                        (255, 255, 255), 2, cv2.LINE_AA)
            # TODO: Move mouse to detected plane

    # assign a unique indentifier to each circle
    # for (i, (x, y, r)) in enumerate(circles):

    cv2.namedWindow('finder', cv2.WINDOW_NORMAL)
    cv2.imshow('finder', median_blur)
    cv2.resizeWindow('finder', 960, 540)
    cv2.moveWindow('finder', 0, 0)

    cv2.namedWindow('video', cv2.WINDOW_NORMAL)
    cv2.imshow('video', frame)
    cv2.resizeWindow('video', 960, 540)
    cv2.moveWindow('video', 960, 0)

    cv2.namedWindow('spotter', cv2.WINDOW_NORMAL)
    cv2.imshow('spotter', median_spotted)
    cv2.resizeWindow('spotter', 960, 540)
    cv2.moveWindow('spotter', 0, 540)

    # changing waitkey interval changes playblack speed.
    if cv2.waitKey(25) & 0xFF == ord('q'):
        break

cap.release()
cv2.destroyAllWindows()
