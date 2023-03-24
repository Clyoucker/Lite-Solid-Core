from Error import LimitError,DuplicateError,FoundError
from FileWorker import db


class Abilities:
    def __init__(self):
        self.__max_abilities = db.get_setting(setting_name="max_abilities")
        self._abilities = dict()

    def add_abilities(self, abilities_name: str):
        db_abilities = db.get_object(obj_name=abilities_name, category="base", types="abilities")
        if len(self._abilities) <= self.__max_abilities:
            if abilities_name not in self._abilities:
                self._abilities[db_abilities["title"]] = {"attributes":db_abilities["attributes"]}
                print(f"New Abilities: [{db_abilities['title']}]")
            else:
                raise DuplicateError(f"Abilities: [{abilities_name}]")
        else:
            raise LimitError(f"Abilities Limit: [{len(self._abilities)} / {self.__max_abilities}]")

    def change_abilities(self, current_abilities: str, new_abilities: str):
        db_abilities = db.get_object(obj_name=new_abilities, category="base", types="abilities")
        if db_abilities["title"] not in self._abilities:
            if current_abilities in self._abilities:
                self._abilities[new_abilities] = self._abilities.pop(current_abilities)
                print(f"{current_abilities} Ability Has Been Changed To [{db_abilities['title']}]")
            else:
                raise FoundError(f"Abilities: [{current_abilities}]")
        else:
            raise DuplicateError(f"Abilities: [{new_abilities}]")

    def del_abilities(self, abilities_name: str):
        if abilities_name in self._abilities:
            del self._abilities[abilities_name]
        else:
            raise FoundError(f"Abilities: [{abilities_name}]")

    def abilities_status(self):
        print(f"\nAbilities: {self._abilities} | Max Abilities: {self.__max_abilities} | Current Abilities: {len(self._abilities)}")
