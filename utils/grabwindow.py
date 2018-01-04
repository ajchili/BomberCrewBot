import time
import win32gui
from ctypes import windll

import cv2
import numpy
import pywintypes
from mss import mss
import threading

import bot.core as core

# Make program aware of DPI scaling
windll.user32.SetProcessDPIAware()

isRunning = False


def grab_window():
    global isRunning

    while isRunning:
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
                core.run(game_capture, width, height)
                cv2.waitKey(1)
            else:
                break


def begin():
    global isRunning

    if not isRunning:
        isRunning = True
        threading.Thread(target=grab_window).start()


def end():
    global isRunning

    isRunning = False
