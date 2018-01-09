import cv2
import numpy as np

ENEMY_SPOTTED_LOWER = np.array([55, 100, 200], np.uint8)
ENEMY_SPOTTED_UPPER = np.array([70, 160, 255], np.uint8)

ENEMY_MARKING_LOWER = np.array([170, 100, 0], np.uint8)
ENEMY_MARKING_UPPER = np.array([180, 255, 255], np.uint8)

# noinspection PyArgumentList
# for some dumb reason relative paths aren't working for this...
cap = cv2.VideoCapture(r'C:\Users\brian\PycharmProjects\BomberCrewBot\res\enemyspotting.avi')
while cap.isOpened():
    ret, frame = cap.read()
    hsv = cv2.cvtColor(frame, cv2.COLOR_BGR2HSV)
    spotted_thresh = cv2.inRange(hsv, ENEMY_SPOTTED_LOWER, ENEMY_SPOTTED_UPPER)
    spotted_blur = cv2.medianBlur(spotted_thresh, 5)

    rows = spotted_blur.shape[0]
    spotted_circles = cv2.HoughCircles(spotted_blur, cv2.HOUGH_GRADIENT, 1, rows / 8, param1=100, param2=11, minRadius=0,
                                       maxRadius=6)

    if spotted_circles is not None:
        spotted_circles = np.uint16(np.around(spotted_circles))
        # for x, y, r in spotted_circles[0, :]:
        for i, (x, y, r) in enumerate(spotted_circles[0, :]):
            center = (x, y)
            # circle center
            cv2.circle(spotted_blur, center, 1, (0, 100, 100), 3)
            cv2.circle(frame, center, 1, (0, 100, 100), 3)
            # circle outline
            cv2.circle(spotted_blur, center, r + 20, (255, 255, 255), 5)
            cv2.circle(frame, center, r, (0, 255, 255), 1)

            cv2.putText(spotted_blur, "enemy plane", (x, y - 40), cv2.FONT_HERSHEY_SIMPLEX, 0.75, (255, 255, 255),
                        2, cv2.LINE_AA)

            # TODO: Move mouse to detected plane

    marking_thresh = cv2.inRange(hsv, ENEMY_MARKING_LOWER, ENEMY_MARKING_UPPER)
    marking_blur = cv2.medianBlur(marking_thresh, 5)
    marking_rows = marking_blur.shape[0]
    marking_circles = cv2.HoughCircles(marking_blur, cv2.HOUGH_GRADIENT, 1, marking_rows / 64, param1=100, param2=20,
                                       minRadius=10, maxRadius=30)
    if marking_circles is not None:
        marking_circles = np.uint16(np.around(marking_circles))
        min_x = 0
        min_y = 0
        max_x = 960
        max_y = 540
        scale = 50

        for i, (x, y, r) in enumerate(marking_circles[0, :]):
            spotted_center = (x, y)
            # circle center
            cv2.circle(marking_blur, spotted_center, 1, (0, 100, 100), 5)
            cv2.circle(frame, spotted_center, 1, (0, 100, 100), 3)
            # circle outline
            cv2.circle(marking_blur, spotted_center, r + 20, (255, 255, 255), 5)
            cv2.circle(frame, spotted_center, r, (0, 255, 255), 1)
            cv2.putText(marking_blur, "enemy plane " + str(i), (x, y + 100), cv2.FONT_HERSHEY_SIMPLEX, 1,
                        (255, 255, 255), 2, cv2.LINE_AA)

            if i == 0:
                min_x = x
                min_y = y
                max_x = x
                max_y = y
            else:
                if min_x > x:
                    min_x = x
                elif max_x < x:
                    max_x = x
                if min_y > y:
                    min_y = y
                elif max_y < y:
                    max_y = y

        if min_x - scale > 0:
            min_x -= scale
        else:
            min_x -= min_x
        if min_y - scale > 0:
            min_y -= scale
        else:
            min_y -= min_y
        if max_x + scale < 960:
            max_x += scale
        else:
            max_x = 960
        if max_y + scale < 540:
            max_y += scale
        else:
            max_y = 540

        roi_topleft = (min_x, min_y)
        roi_bottomright = (max_x, max_y)
        marking_blur = marking_blur[min_y:max_y + 540, min_x:max_x + 960]
        #cv2.imshow("cropped", crop_img)

        #cv2.rectangle(marking_blur, roi_topleft, roi_bottomright, (255, 255, 255), 3)
            # TODO: Move mouse to detected plane

    cv2.namedWindow('spotted', cv2.WINDOW_NORMAL)
    cv2.imshow('spotted', spotted_blur)
    cv2.resizeWindow('spotted', 960, 540)
    cv2.moveWindow('spotted', 0, 0)

    cv2.namedWindow('video', cv2.WINDOW_NORMAL)
    cv2.imshow('video', frame)
    cv2.resizeWindow('video', 960, 540)
    cv2.moveWindow('video', 960, 0)

    cv2.namedWindow('marking', cv2.WINDOW_NORMAL)
    cv2.imshow('marking', marking_blur)
    cv2.resizeWindow('marking', 960, 540)
    cv2.moveWindow('marking', 0, 540)

    # changing waitkey interval changes playblack speed.
    if cv2.waitKey(25) & 0xFF == ord('q'):
        break

cap.release()
cv2.destroyAllWindows()
