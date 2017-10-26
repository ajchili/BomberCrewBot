import os
import json


class CrewMember:
    name = ""
    skill = ""

    def __init__(self, name, skill):
        self.name = name
        self.skill = Skill(skill)

    def __str__(self):
        return str(self.name + " : " + str(self.skill))

    def __repr__(self):
        return str(self.name + " : " + str(self.skill))


class Skill:
    skill = ""
    skills = ["Pilot", "Gunner", "Navigator", "Radio Op", "Engineer", "Bomber"]

    def __init__(self, skill):
        self.skill = self.skills[skill]

    def __str__(self):
        return str(self.skill)

    def __repr__(self):
        return str(self.skill)


def get_active_crew_members():
    with open("C:\\Users\\" + os.getlogin() + "\\AppData\\LocalLow\\Runner Duck\\Bomber Crew\\BC_SaveSlotV2_0.dat") \
            as file:
            return [CrewMember(crew_member["m_firstName"], crew_member["m_primarySkill"]["m_skillType"]) for
                    crew_member in json.load(file)["m_activeCrewmen"]]
