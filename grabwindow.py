import time
import win32gui
from ctypes import windll

import cv2
import numpy
import pywintypes
from mss import mss

from findobjectives import analyze_window

# Make program aware of DPI scaling
windll.user32.SetProcessDPIAware()


def grab_window():
    while True:
        # Obtain Bomber Crew window size
        try:
            hwnd = win32gui.FindWindow("UnityWndClass", None)
            left, top, right, bottom = win32gui.GetWindowRect(hwnd)
        except pywintypes.error:
            print("Bomber Crew Window Not Found!")
            time.sleep(5)
        else:
            width = right - left
            height = bottom - top
            game_window = {'top': top, 'left': left, 'width': width, 'height': height}

            foreground_window_name = win32gui.GetWindowText(win32gui.GetForegroundWindow())

            if foreground_window_name == "Bomber Crew":
                game_capture = numpy.array(mss().grab(game_window))
                analyze_window(game_capture, width, height, left, top)
                cv2.waitKey(1)
            else:
                break
