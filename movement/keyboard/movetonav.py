import threading

import pyautogui

CIRCLE_WIDTH = 150
MOVEMENT_TIME = 0.1
is_space_pressed = False
is_nav_selected = False


def move(width, height, nav_x, nav_y):
    global is_space_pressed, is_nav_selected
    nav_is_centered_x = False
    nav_is_centered_y = False

    if not is_space_pressed:
        is_space_pressed = True
        pyautogui.press('space')

    if is_space_pressed and not is_nav_selected:
        center_x = width / 2
        center_y = height / 2
        x_movement = (nav_x - (center_x - CIRCLE_WIDTH)) / center_x
        y_movement = (nav_y - (center_y - CIRCLE_WIDTH)) / center_y
        min_x_movement_required = 1 - (center_x - (CIRCLE_WIDTH / 2)) / center_x
        min_y_movement_required = 1 - (center_y - (CIRCLE_WIDTH / 2)) / center_y

        if x_movement > min_x_movement_required:
            pyautogui.keyDown('right', MOVEMENT_TIME * abs(x_movement))
            pyautogui.keyUp('right')
        elif x_movement < -min_x_movement_required:
            pyautogui.keyDown('left', MOVEMENT_TIME * abs(x_movement))
            pyautogui.keyUp('left')
        else:
            nav_is_centered_x = True

        if y_movement > min_y_movement_required:
            pyautogui.keyDown('down', MOVEMENT_TIME * abs(y_movement))
            pyautogui.keyUp('down')
        elif y_movement < -min_y_movement_required:
            pyautogui.keyDown('up', MOVEMENT_TIME * abs(y_movement))
            pyautogui.keyUp('up')
        else:
            nav_is_centered_y = True

    if nav_is_centered_x and nav_is_centered_y and not is_nav_selected:
        is_nav_selected = True
        threading.Timer(3, reset).start()


def reset():
    global is_space_pressed, is_nav_selected
    is_space_pressed = False
    pyautogui.press('space')
    is_nav_selected = False
