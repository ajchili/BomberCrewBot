import win32gui
import win32api
import win32con
import pyautogui
import pywintypes
from threading import Timer


def takeoff():
    pyautogui.press('1')
    try:
        hwnd = win32gui.FindWindow("UnityWndClass", None)
        left, top, right, bottom = win32gui.GetWindowRect(hwnd)
    except pywintypes.error:
        print("Bomber Crew Window Not Found!")
        return False

    width = right - left
    height = bottom - top
    x = int(left + width / 2)
    y = int(top + height * 0.8)
    win32api.SetCursorPos((x, y))
    win32api.mouse_event(win32con.MOUSEEVENTF_LEFTDOWN, x, y, 0, 0)
    Timer(0.01, win32api.mouse_event, [win32con.MOUSEEVENTF_LEFTUP, x, y, 0, 0, ]).start()
    return True
