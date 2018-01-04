import cv2
import threading

import movement.keyboard.movetonav as keyboard_nav
import movement.mouse.movetonav as mouse_nav


def locate_template(window, width, height, template, min_val, max_val, lower, upper, use_mouse):
    img = cv2.inRange(cv2.cvtColor(window, cv2.COLOR_BGR2HSV), lower, upper)
    blur = cv2.medianBlur(cv2.bitwise_and(img, img), 5)

    w, h = template.shape[::-1]
    res = cv2.matchTemplate(blur, template, cv2.TM_CCOEFF)
    local_min_val, local_max_val, min_loc, max_loc = cv2.minMaxLoc(res)
    bottom_right = (min_loc[0] + w, min_loc[1] + h)

    if local_min_val < min_val and local_max_val > max_val:
        if use_mouse:
            mouse_nav.move(width, height, min_loc[0] + (w / 2), min_loc[1] + (h / 2))
        else:
            threading.Thread(target=keyboard_nav.move,
                             args=(width, height, min_loc[0] + (w / 2), min_loc[1] + (h / 2),)).start()
        cv2.rectangle(blur, min_loc, bottom_right, 255, 1)

    cv2.imshow("BomberCrewBot Template Locator", blur)
