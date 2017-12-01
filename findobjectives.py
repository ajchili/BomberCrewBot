import copy
import threading

import ctypes
import cv2
import numpy as np

import movementhandler as mvt

DAY_TIME = 130
NAV_DAY_LOWER = np.array([15, 160, 150], np.uint8)
NAV_DAY_UPPER = np.array([25, 255, 180], np.uint8)
NAV_NIGHT_LOWER = np.array([15, 150, 75], np.uint8)
NAV_NIGHT_UPPER = np.array([35, 255, 180], np.uint8)


def analyze_window(window, width, height, window_x, window_y):
    upper_half = cv2.rectangle(copy.deepcopy(window), (0, 0), (width, int(height / 2)), (0, 0, 255), 1, cv2.LINE_8, 0)
    is_day = upper_half.mean() > DAY_TIME
    locate_nav(window, width, height, is_day, window_x, window_y)


def locate_nav(window, width, height, is_day, window_x, window_y):
    if is_day:
        lower = NAV_DAY_LOWER
        upper = NAV_DAY_UPPER
    else:
        lower = NAV_NIGHT_LOWER
        upper = NAV_NIGHT_UPPER

    img = cv2.inRange(cv2.cvtColor(window, cv2.COLOR_BGR2HSV), lower, upper)
    template = cv2.imread('res/map_50px.png', 0)
    blur = cv2.medianBlur(cv2.bitwise_and(img, img), 5)

    w, h = template.shape[::-1]
    res = cv2.matchTemplate(blur, template, cv2.TM_CCOEFF)
    min_val, max_val, min_loc, max_loc = cv2.minMaxLoc(res)
    bottom_right = (min_loc[0] + w, min_loc[1] + h)

    if min_val < -500000 and max_val > 600000:
        threading.Thread(target=mvt.move_to_nav, args=(width, height, min_loc[0] + (w / 2), min_loc[1] + (h / 2),)).start()
        cv2.rectangle(blur, min_loc, bottom_right, 255, 1)

    cv2.imshow("BomberCrewBot Test", blur)
    cv2.moveWindow("BomberCrewBot Test", -1920, 0)