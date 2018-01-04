import copy
import threading

import cv2
import numpy as np

from bot import templatefinder as template_finder
from movement.keyboard import movetonav as keyboard_nav
from movement.mouse import movetonav as mouse_nav

DAY_TIME = 130
NAV_DAY_LOWER = np.array([15, 160, 150], np.uint8)
NAV_DAY_UPPER = np.array([25, 255, 180], np.uint8)
NAV_NIGHT_LOWER = np.array([15, 150, 75], np.uint8)
NAV_NIGHT_UPPER = np.array([35, 255, 180], np.uint8)

is_day = None
use_mouse = True


def analyze_window(window, width, height):
    if is_day is None:
        calculate_time(window, width, height)

    locate_nav(window, width, height)


def calculate_time(window, width, height):
    global is_day

    upper_half = cv2.rectangle(copy.deepcopy(window), (0, 0), (width, int(height / 2)), (0, 0, 255), 1, cv2.LINE_8, 0)
    is_day = upper_half.mean() > DAY_TIME


def locate_nav(window, width, height):
    global is_day

    if is_day:
        lower = NAV_DAY_LOWER
        upper = NAV_DAY_UPPER
    else:
        lower = NAV_NIGHT_LOWER
        upper = NAV_NIGHT_UPPER
    pos_x, pos_y = template_finder.locate_template(window, width, height, cv2.imread('res/nav.png', 0), -500000,
                                                   600000, lower, upper)

    if pos_x is not None and pos_y is not None:
        if use_mouse:
            mouse_nav.move(width, height, pos_x, pos_y)
        else:
            threading.Thread(target=keyboard_nav.move,
                             args=(width, height, pos_x, pos_y,)).start()
