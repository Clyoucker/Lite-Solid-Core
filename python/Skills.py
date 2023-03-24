from Error import FoundError
from FileWorker import db
import os
clear = lambda: os.system('cls')


class Skills:
    def __init__(self, skills: dict):
        self.__max_skills = db.get_setting(setting_name="max_skills")
        self._all_skills = db.get_all_objects(category="base",types="skills")
        self._skills_bonus = None
        self._current_skills = skills

    def set_skills(self):
        clear()
        accessible_skills = list(self._all_skills.copy())
        temp_accessible_skills = dict()
        for i in range(len(accessible_skills)):
            temp_accessible_skills[i] = accessible_skills[i]
        temp_skills = dict()
        for i in range(1,self.__max_skills+1):
            print(temp_accessible_skills)
            match i:
                case 1:
                    res = int(input(f"Skill LvL 5: "))
                    temp_skills[temp_accessible_skills[res]] = 5
                case 2 | 3:
                    res = int(input(f"Skill LvL 4: "))
                    temp_skills[temp_accessible_skills[res]] = 4
                case 4 | 5 | 6:
                    res = int(input(f"Skill LvL 3: "))
                    temp_skills[temp_accessible_skills[res]] = 3
                case _:
                    res = int(input(f"Skill LvL 2: "))
                    temp_skills[temp_accessible_skills[res]] = 2
            del temp_accessible_skills[res]
        self._current_skills = temp_skills

    def change_skills(self, old_skill, new_skill):
        clear()
        if new_skill in self._all_skills and new_skill not in self._current_skills:
            if old_skill in self._current_skills:
                self._current_skills[new_skill] = self._current_skills.pop(old_skill)
            else:
                print(f"Not Fount Skills: [{old_skill}]")
        else:
            print(f"Not Fount Skills: [{new_skill}]")

    def skills_status(self):
        clear()
        message = ""
        for key,value in self._current_skills.items():
            message += f"{key}:{value} [LvL] | "
        print(message,"\n")
