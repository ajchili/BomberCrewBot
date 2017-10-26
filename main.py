import sys
import numpy as np
import cv2
from mss import mss
from PIL import ImageGrab
import win32gui


hwndMain = win32gui.FindWindow("UnityWndClass", None)


def game_record():
    while True:
        printscreen = np.array(ImageGrab.grab(bbox=(0, 40, 800, 640)))
        cv2.imshow('window',cv2.cvtColor(printscreen, cv2.COLOR_BGR2RGB))
