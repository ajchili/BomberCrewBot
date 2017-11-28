import cv2
import numpy as np


def analyze_window(window, width, height, window_x, window_y):
    print("analyzing window")
    upper_half = cv2.rectangle(window, (0, 0), (width, int(height / 2)), (0, 0, 255), 1, cv2.LINE_8, 0)
    is_day = upper_half.mean() > 130
    locate_nav(window, is_day)


def locate_nav(window, is_day):
    print('locating nav')

    # TODO: Implement way to detect/check for if navigation icon is in clouds
    if is_day:
        lower = np.array([15, 160, 150], np.uint8)
        upper = np.array([25, 255, 180], np.uint8)
    else:
        lower = np.array([15, 150, 75], np.uint8)
        upper = np.array([35, 255, 180], np.uint8)
    img = cv2.inRange(cv2.cvtColor(window, cv2.COLOR_BGR2HSV), lower, upper)

    template = cv2.imread('res/map_50px.png', 0)

    blur = cv2.medianBlur(cv2.bitwise_and(img, img), 5)

    w, h = template.shape[::-1]
    res = cv2.matchTemplate(blur, template, cv2.TM_CCOEFF)
    min_val, max_val, min_loc, max_loc = cv2.minMaxLoc(res)
    bottom_right = (min_loc[0] + w, min_loc[1] + h)
    cv2.rectangle(blur, min_loc, bottom_right, 255, 1)
    cv2.imshow("BomberCrewBot Test", blur)
    # cv2.moveWindow("BomberCrewBot Test", -1920, 0)
