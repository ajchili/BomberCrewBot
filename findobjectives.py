import pyautogui
import cv2
import numpy as np
from matplotlib import pyplot as plt


def analyze_window(window, window_x, window_y):
    print("analyzing window")
    locate_nav(window)


def locate_nav(window):
    print('locating nav')

    lower = np.array([15, 95, 55], np.uint8)
    upper = np.array([25, 255, 255], np.uint8)
    img = cv2.inRange(cv2.cvtColor(window, cv2.COLOR_BGR2HSV), lower, upper)
    dim = (100, 100)
    template = cv2.resize(cv2.imread('res/nav.jpg', 0), dim, interpolation=cv2.INTER_AREA)

    mask = np.zeros(img.shape, dtype="uint8")
    cv2.rectangle(mask, (0, 0), (1280, 860), (255, 255, 255), -1)
    cv2.rectangle(mask, (1160, 35), (1200, 65), (0, 0, 0), -1)

    blur = cv2.medianBlur(cv2.bitwise_and(img, mask), 5)

    w, h = template.shape[::-1]
    res = cv2.matchTemplate(blur, template, cv2.TM_CCOEFF)
    min_val, max_val, min_loc, max_loc = cv2.minMaxLoc(res)
    bottom_right = (min_loc[0] + w, min_loc[1] + h)
    cv2.rectangle(blur, min_loc, bottom_right, 255, 1)
    cv2.imshow('BomberCrewBot 2', blur)
