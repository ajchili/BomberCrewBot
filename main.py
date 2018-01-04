from utils import grabwindow
from utils.crewmembers import get_active_crew_members

from pynput.keyboard import Key, KeyCode, Listener

isActive = False
hasTakenOff = False
crew_members = get_active_crew_members()


def on_press(key):
    global isActive, hasTakenOff

    if key == KeyCode(vk=0, char='q'):
        isActive = not isActive
        if isActive:
            grabwindow.begin()
        else:
            grabwindow.end()


def on_release(key):
    global isActive

    if key == Key.esc:
        isActive = False
        return False


# Collect events until released
with Listener(on_press=on_press, on_release=on_release) as listener:
    listener.join()
