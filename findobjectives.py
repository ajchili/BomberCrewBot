import cv2
import numpy as np
#import pyautogui
from matplotlib import pyplot as plt


def analyze_window(window, width, height, window_x, window_y):
    print("analyzing window")
    locate_nav(window)


def locate_nav(window):
    print('locating nav')
    
    lower = np.array([15, 200, 79], np.uint8)
    upper = np.array([35, 255, 150], np.uint8)
    img = cv2.inRange(cv2.cvtColor(window, cv2.COLOR_BGR2HSV), lower, upper)

    template = cv2.imread('res/nav.png', 0)

    blur = cv2.medianBlur(cv2.bitwise_and(img, img), 5)

    w, h = template.shape[::-1]
    res = cv2.matchTemplate(blur, template, cv2.TM_CCOEFF)
    min_val, max_val, min_loc, max_loc = cv2.minMaxLoc(res)
    bottom_right = (min_loc[0] + w, min_loc[1] + h)
    cv2.rectangle(blur, min_loc, bottom_right, 255, 1)
    cv2.imshow("BomberCrewBot Test", blur)
    cv2.moveWindow("BomberCrewBot Test", -1920, 0)
