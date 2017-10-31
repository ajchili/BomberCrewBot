import sys
import numpy
import cv2
from PIL import Image
import win32gui
import win32ui
from ctypes import windll
from grabwindow import grab_window
from crewmembers import get_active_crew_members
from matplotlib import pyplot as plt

while True:
    grab_window()
    #TODO: get "game_capture" from grabwindow
    get_active_crew_members()


# TODO: Implement Template Matching
#     img2 = img.copy()
#     template = cv2.imread('nav.png', 0)
#     w, h = template.shape[::-1]
#     res = cv2.matchTemplate(img, template, cv2.TM_CCOEFF)
#     img = img2.copy()
#     min_val, max_val, min_loc, max_loc = cv2.minMaxLoc(res)
#     top_left = max_loc
#     bottom_right = (top_left[0] + w, top_left[1] + h)
#     cv2.rectangle(img, top_left, bottom_right, 255, 2)
#
#     plt.subplot(121), plt.imshow(res, cmap='gray')
#     plt.title('Matching Result'), plt.xticks([]), plt.yticks([])
#     plt.subplot(122), plt.imshow(img, cmap='gray')
#     plt.title('Detected Point'), plt.xticks([]), plt.yticks([])
#     plt.show()
