import pyautogui
import cv2
import numpy as np
from matplotlib import pyplot as plt


def analyze_window(window, window_x, window_y):
    print("analyzing window")
    locate_nav(window)


def locate_nav(window):
    print('locating nav')
    lower = np.array([15, 90, 50], np.uint8)
    upper = np.array([30, 255, 255], np.uint8)
    img = cv2.inRange(cv2.cvtColor(window, cv2.COLOR_BGR2HSV), lower, upper)
    template = cv2.imread('res/nav.jpg', 0)
    w, h = template.shape[::-1]
    res = cv2.matchTemplate(img, template, cv2.TM_CCOEFF)
    min_val, max_val, min_loc, max_loc = cv2.minMaxLoc(res)
    top_left = max_loc
    bottom_right = (top_left[0] + w, top_left[1] + h)
    cv2.rectangle(img, top_left, bottom_right, 255, 2)
    #cv2.imshow('BomberCrewBot 2', cv2.rectangle(img, top_left, bottom_right, 255, 2))

    plt.subplot(121), plt.imshow(res, 'gray')
    plt.title('Matching Result'), plt.xticks([]), plt.yticks([])
    plt.subplot(122), plt.imshow(img, 'gray')
    plt.title('Detected Point'), plt.xticks([]), plt.yticks([])
    plt.show()