import win32gui
from ctypes import windll
import time
import cv2
import numpy
import pywintypes
from findobjectives import analyze_window
from mss import mss

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
            time.sleep(1)
        else:
            width = right - left
            height = bottom - top
            game_window = {'top': top, 'left': left, 'width': width, 'height': height}

            foreground_window_name = win32gui.GetWindowText(win32gui.GetForegroundWindow())

            if foreground_window_name == "Bomber Crew":
                game_capture = numpy.array(mss().grab(game_window))
                analyze_window(game_capture)
                cv2.imshow('BomberCrewBot', game_capture)

                if cv2.waitKey(25) & 0xFF == ord('q'):
                    cv2.destroyAllWindows()
                    break
                return game_capture
            else:
                print("Bomber Crew Window Not Active!")
                time.sleep(.250)
                break
