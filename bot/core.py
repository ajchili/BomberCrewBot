from bot import takeoffmanager as take_off_manager
from bot import findobjectives as find_objectives
from bot import findenemy as find_enemy


hasTakenOff = False


def run(window, width, height):
    global hasTakenOff

    if not hasTakenOff:
        take_off_manager.takeoff()
        hasTakenOff = True
    else:
        find_objectives.analyze_window(window, width, height)
        find_enemy.analyze_window(window, width, height)


