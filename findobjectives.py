import copy

import cv2
import numpy as np

import bot.templatefinder as template_finder

DAY_TIME = 130
NAV_DAY_LOWER = np.array([15, 160, 150], np.uint8)
NAV_DAY_UPPER = np.array([25, 255, 180], np.uint8)
NAV_NIGHT_LOWER = np.array([15, 150, 75], np.uint8)
NAV_NIGHT_UPPER = np.array([35, 255, 180], np.uint8)

use_mouse = True


def analyze_window(window, width, height, window_x, window_y):
    upper_half = cv2.rectangle(copy.deepcopy(window), (0, 0), (width, int(height / 2)), (0, 0, 255), 1, cv2.LINE_8, 0)
    is_day = upper_half.mean() > DAY_TIME
    locate_nav(window, width, height, is_day)


def locate_nav(window, width, height, is_day):
    if is_day:
        lower = NAV_DAY_LOWER
        upper = NAV_DAY_UPPER
    else:
        lower = NAV_NIGHT_LOWER
        upper = NAV_NIGHT_UPPER
    template_finder.locate_template(window, width, height, cv2.imread('res/nav.png', 0), -500000, 600000, lower, upper,
                                    use_mouse)