from grabwindow import grab_window
from crewmembers import get_active_crew_members
import cv2
import numpy as np

crew_members = get_active_crew_members()

while True:
    print('locating nav')
    grab_window()
