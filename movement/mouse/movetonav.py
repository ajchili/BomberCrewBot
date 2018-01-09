import threading

import win32api
import win32con
import pyautogui

CIRCLE_WIDTH = 100
MOVEMENT_SPEED = 30
is_space_pressed = False
is_nav_selected = False


def move(width, height, nav_x, nav_y):
    global is_space_pressed, is_nav_selected
    center_x = width / 2
    center_y = height / 2
    x_movement = (nav_x - (center_x - CIRCLE_WIDTH)) / center_x
    y_movement = (nav_y - (center_y - CIRCLE_WIDTH)) / center_y
    min_x_movement_required = 1 - (center_x - (CIRCLE_WIDTH / 2)) / center_x
    min_y_movement_required = 1 - (center_y - (CIRCLE_WIDTH / 2)) / center_y

    if not is_space_pressed:
        is_space_pressed = True
        pyautogui.press('space')

    if min_x_movement_required > x_movement > -min_x_movement_required and min_y_movement_required > y_movement > -min_y_movement_required:
        is_nav_selected = True
        threading.Timer(3, reset)
    elif not is_nav_selected:
        win32api.mouse_event(win32con.MOUSEEVENTF_ABSOLUTE | win32con.MOUSEEVENTF_MOVE, int(65535 / 2), int(65535 / 2), 0, 0)
        win32api.mouse_event(win32con.MOUSEEVENTF_MOVE, int(x_movement * MOVEMENT_SPEED), int(y_movement * MOVEMENT_SPEED), 0, 0)


def reset():
    global is_space_pressed, is_nav_selected
    is_space_pressed = False
    pyautogui.press('space')
    is_nav_selected = False
