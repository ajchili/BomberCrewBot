from grabwindow import grab_window
from utils.crewmembers import get_active_crew_members

crew_members = get_active_crew_members()

while True:
    grab_window()
