import win32gui
from ctypes import windll

import cv2
import numpy
from mss import mss

# Make program aware of DPI scaling
windll.user32.SetProcessDPIAware()


def grab_window():
    while True:
        # Obtain Bomber Crew window size
        hwnd = win32gui.FindWindow("UnityWndClass", None)
        left, top, right, bottom = win32gui.GetWindowRect(hwnd)
        width = right - left
        height = bottom - top
        game_window = {'top': top, 'left': left, 'width': width, 'height': height}

        foreground_window = win32gui.GetWindowText(win32gui.GetForegroundWindow())

        while foreground_window == "Bomber Crew":
            print(foreground_window)
            img = numpy.array(mss().grab(game_window))
            cv2.imshow('test', img)
            if cv2.waitKey(25) & 0xFF == ord('q'):
                cv2.destroyAllWindows()
                break
        else:
            print("Bomber Crew Window Not Active!")
