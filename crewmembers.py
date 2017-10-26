import os
import json


class CrewMember:
    name = ""
    role = ""

    def __init__(self, name, role):
        self.name = name
        self.role = role

    def __str__(self):
        return str(self.name + " : " + str(self.role))

    def __repr__(self):
        return str(self.name + " : " + str(self.role))


def get_active_crew_members():
    with open("C:\\Users\\" + os.getlogin() + "\\AppData\\LocalLow\\Runner Duck\\Bomber Crew\\BC_SaveSlotV2_0.dat") \
            as file:
            return [CrewMember(crew_member["m_firstName"], crew_member["m_primarySkill"]["m_skillType"]) for
                    crew_member in json.load(file)["m_activeCrewmen"]]
