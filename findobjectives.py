import cv2
import numpy as np
import copy
import time
import pyautogui

DAY_TIME_CONSTANT = 130
NAV_DAY_LOWER_ARRAY = np.array([15, 160, 150], np.uint8)
NAV_DAY_UPPER_ARRAY = np.array([25, 255, 180], np.uint8)
NAV_NIGHT_LOWER_ARRAY = np.array([15, 150, 75], np.uint8)
NAV_NIGHT_UPPER_ARRAY = np.array([35, 255, 180], np.uint8)


def analyze_window(window, width, height, window_x, window_y):
    print("analyzing window")
    start_time = int(round(time.time() * 1000))
    upper_half = cv2.rectangle(copy.deepcopy(window), (0, 0), (width, int(height / 2)), (0, 0, 255), 1, cv2.LINE_8, 0)
    is_day = upper_half.mean() > DAY_TIME_CONSTANT
    locate_nav(window, is_day)
    print('analyzed window in ' + str(int(round(time.time() * 1000)) - start_time) + 'ms')


def locate_nav(window, is_day):
    print('locating nav')
    start_time = int(round(time.time() * 1000))

    # TODO: Implement way to detect/check for if navigation icon is in clouds
    if is_day:
        lower = NAV_DAY_LOWER_ARRAY
        upper = NAV_DAY_UPPER_ARRAY
    else:
        lower = NAV_NIGHT_LOWER_ARRAY
        upper = NAV_NIGHT_UPPER_ARRAY
    img = cv2.inRange(cv2.cvtColor(window, cv2.COLOR_BGR2HSV), lower, upper)

    template = cv2.imread('res/map_50px.png', 0)

    blur = cv2.medianBlur(cv2.bitwise_and(img, img), 5)

    w, h = template.shape[::-1]
    res = cv2.matchTemplate(blur, template, cv2.TM_CCOEFF)
    min_val, max_val, min_loc, max_loc = cv2.minMaxLoc(res)
    bottom_right = (min_loc[0] + w, min_loc[1] + h)
    if min_val < -500000 and max_val > 600000:
        cv2.rectangle(blur, min_loc, bottom_right, 255, 1)
    cv2.imshow("BomberCrewBot Test", blur)
    # cv2.moveWindow("BomberCrewBot Test", -1920, 0)
    print('located nav icon in ' + str(int(round(time.time() * 1000)) - start_time) + 'ms')
