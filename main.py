import sys
import numpy as np
import cv2
from PIL import Image
import win32gui
import win32ui
from ctypes import windll
from grabwindow import grab_window
from crewmembers import get_active_crew_members

grab_window()
crew_members = get_active_crew_members()

print(crew_members)