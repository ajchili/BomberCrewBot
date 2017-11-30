import threading

import pyautogui

CIRCLE_WIDTH = 200
MOVEMENT_SPEED = .75
is_space_pressed = False
is_space_reset = False


def move_to_nav(width, height, nav_x, nav_y):
    global is_space_pressed, is_space_reset
    is_centered = True
    center_x = width / 2
    center_y = height / 2

    if not is_space_pressed:
        is_space_pressed = True
        pyautogui.press('space')

    if is_space_pressed and not is_space_reset:
        x_movement = (nav_x - (center_x - CIRCLE_WIDTH)) / center_x
        y_movement = (nav_y - (center_y - CIRCLE_WIDTH)) / center_y

        if x_movement > 0.125:
            is_centered = False
            pyautogui.keyDown('right', MOVEMENT_SPEED * abs(x_movement))
            pyautogui.keyUp('right')
        elif x_movement < -0.125:
            is_centered = False
            pyautogui.keyDown('left', MOVEMENT_SPEED * abs(x_movement))
            pyautogui.keyUp('left')

        if y_movement > 0.125:
            is_centered = False
            pyautogui.keyDown('up', MOVEMENT_SPEED * abs(y_movement))
            pyautogui.keyUp('up')
        elif y_movement < -0.125:
            is_centered = False
            pyautogui.keyDown('down', MOVEMENT_SPEED * abs(y_movement))
            pyautogui.keyUp('down')

    if is_centered and not is_space_reset:
        is_space_reset = True
        threading.Timer(2.5, reset_is_space_pressed).start()


def reset_is_space_pressed():
    global is_space_pressed, is_space_reset
    is_space_pressed = False
    pyautogui.press('space')
    is_space_reset = False