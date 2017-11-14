from grabwindow import grab_window
from crewmembers import get_active_crew_members

crew_members = get_active_crew_members()

while True:
    print('locating nav')
    grab_window()
