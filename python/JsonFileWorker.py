from FileWorkerComponents import *
from tabulate import tabulate
from Corrector import lowers
from Error import FoundError,DuplicateError,AttributesError
import datetime
import os
clear = lambda: os.system('cls')


class JsonFileWorker:
    def __init__(self):
        self.config_name = "Config"
        self.objects_name = "Objects"
        self.bases_name = "Base"

        self.__format = ".json"
        self.__base_json_path = "../../assets/jsons/"
        self.__backup_json_path = "../../assets/backup/"
        self.__recovery_json_path = "../../assets/recovery/"

        self.__datas = dict()
        self.__settings = dict()
        self.__category_types = dict()

        self._config_path = f"{self.__base_json_path}{self.config_name}{self.__format}"
        self._objects_path = f"{self.__base_json_path}{self.objects_name}{self.__format}"
        self._bases_path = f"{self.__base_json_path}{self.bases_name}{self.__format}"

        self._backup_config_path = f"{self.__backup_json_path}Backup_{self.config_name}{self.__format}"
        self._backup_objects_path = f"{self.__backup_json_path}Backup_{self.config_name}{self.__format}"
        self._backup_bases_path = f"{self.__backup_json_path}Backup_{self.config_name}{self.__format}"

        self._recovery_config_path = f"{self.__recovery_json_path}Recovery_{self.config_name}{self.__format}"
        self._recovery_objects_path = f"{self.__recovery_json_path}Recovery_{self.objects_name}{self.__format}"
        self._recovery_bases_path = f"{self.__recovery_json_path}Recovery_{self.bases_name}{self.__format}"

        self._all = set()
        self._items = set()
        self.potions = set()
        self._abilities = set()
        self._wears = set()
        self._info = set()

        self.__packing_status = False
        self.datas_status = False

    # Objects Methods

    def __get_item_index(self, obj_name: str, category: str, types: str):
        index = 0
        for item in self.__datas[category][types]:
            if item["title"] == obj_name:
                return index
            else:
                index += 1

    def __get_all_items(self):
        items = set()
        datas = self.__datas["objects"]
        keys = [key for key in datas]
        for key in keys:
            for item in datas[key]:
                items.add(item["title"])
        return items

    def __packing_objects(self, message: str = None):
        print(message) if message else None
        items = self.get_all_objects(category="objects", types="items")
        potions = self.get_all_objects(category="objects", types="potions")
        weapons = self.get_all_objects(category="objects", types="weapons")
        equips = self.get_all_objects(category="objects", types="equips")
        abilities = self.get_all_objects(category="base", types="abilities")

        races = self.get_all_objects(category="base", types="races")
        classes = self.get_all_objects(category="base", types="class")
        profs = self.get_all_objects(category="base", types="profs")
        specs = self.get_all_objects(category="base", types="specs")
        rels = self.get_all_objects(category="base", types="religions")
        ranks = self.get_all_objects(category="base", types="ranks")

        res = 11 if items and weapons and equips and abilities and races and classes and profs and specs and rels and ranks and potions else -11

        if res == 11:
            self._items = items | weapons | equips
            self.potions = potions
            self._abilities = abilities
            self._wears = weapons | equips
            self._info = races | classes | profs | specs | rels | ranks
            self._all = self._info | self._abilities | self._items
            self.__packing_status = True

    # Objects Methods

    def get_object(self, obj_name:str, category:str = None, types:str = None) -> dict:
        objs = list()
        key = 0
        if category is None and types is None:
            if self.__settings["use_start_witch"] is True:
                for category in self.__datas:
                    for types in self.__datas[category]:
                        index = 0
                        for item in self.__datas[category][types]:
                            if item["title"].startswith(obj_name):
                                objs.append({"key": key, "title": item["title"], "path": f"{category}/{types}/{index}"})
                                key += 1
                            index += 1
                if len(objs) == 1:
                    path = path_create(objs, 0)
                    return self.__datas[path[0]][path[1]][int(path[2])]
                elif len(objs) == 0:
                    raise FoundError(f"Object [{obj_name}]")
                else:
                    print_array(objs)
                    key = int(input("key item: "))
                    path = path_create(objs, key)
                    return self.__datas[path[0]][path[1]][int(path[2])]
            else:
                if obj_name in self._all:
                    for category in self.__datas:
                        for types in self.__datas[category]:
                            for item in self.__datas[category][types]:
                                if item["title"] == obj_name:
                                    return item
                else:
                    raise FoundError(obj_name)
        elif category is not None and types is None:
            if self.__settings["use_start_witch"] is True:
                for types in self.__datas[category]:
                    index = 0
                    for item in self.__datas[category][types]:
                        if item["title"].startswith(obj_name):
                            objs.append({"key": key, "title": item["title"], "path": f"{category}/{types}/{index}"})
                            key += 1
                        index += 1
                if len(objs) == 1:
                    path = path_create(objs, 0)
                    return self.__datas[path[0]][path[1]][int(path[2])]
                elif len(objs) == 0:
                    raise FoundError(obj_name)
                else:
                    print_array(objs)
                    key = int(input("key item: "))
                    path = path_create(objs, key)
                    return self.__datas[path[0]][path[1]][int(path[2])]
            else:
                if obj_name in self._all:
                    for types in self.__datas[category]:
                        for item in self.__datas[category][types]:
                            if item["title"] == obj_name:
                                return item
                else:
                    raise FoundError(f"Object [{obj_name}]")
        else:
            if self.__settings["use_start_witch"] is True:
                index = 0
                for item in self.__datas[category][types]:
                    if item["title"].startswith(obj_name):
                        objs.append({"key": key, "title": item["title"], "path": f"{category}/{types}/{index}"})
                        key += 1
                    index += 1
                if len(objs) == 1:
                    path = path_create(objs, 0)
                    return self.__datas[path[0]][path[1]][int(path[2])]
                elif len(objs) == 0:
                    raise FoundError(f"Object [{obj_name}]")
                else:
                    print_array(objs)
                    key = int(input("key item: "))
                    path = path_create(objs, key)
                    return self.__datas[path[0]][path[1]][int(path[2])]
            else:
                if obj_name in self._all:
                    for item in self.__datas[category][types]:
                        if item["title"] == obj_name:
                            return item
                else:
                    raise FoundError(f"Object [{obj_name}]")

    def get_all_objects(self, category: str, types: str):
        temp_datas = set()
        for item in self.__datas[category][types]:
            temp_datas.add(item["title"])
        return temp_datas

    def read_object(self, category: str = None, types: str = None):
        clear()
        category = None if category == "" else category
        types = None if types == "" else types
        header = ["title"]
        body = list()
        if category is not None:
            header += [head for head in self.__datas[category][types][0]["attributes"].keys()]
            for item in self.__datas[category][types]:
                body.append([item["title"]] + [attribute for attribute in item["attributes"].values()])
            print(tabulate(body, headers=header),"\n")
        else:
            for category in [key for key in self.__datas.keys()]:
                for types in self.__datas[category]:
                    print(f"\n================[{category}][{types}]==================")
                    header = ["title"]
                    body = list()
                    for item in self.__datas[category][types]:
                        for atr in [i for i in item["attributes"].keys()]:
                            if atr not in header:
                                header.append(atr)
                    for item in self.__datas[category][types]:
                        temp_list = list()
                        for atr in header:
                            if atr == "title":
                                temp_list.append(item["title"])
                            elif atr not in item["attributes"]:
                                temp_list.append(0)
                            else:
                                temp_list.append(item["attributes"][atr])
                        body.append(temp_list)
                    print(tabulate(body, headers=header), "\n")

    def create_object(self, obj_name: str, attribute, category: str, types: str):
        obj_name = lowers(obj_name)
        if obj_name not in self._all:
            attribute = dict(obj.split("=") for obj in attribute.split("/"))
            keys = set(key for key in attribute.keys())
            if "cost" in keys and "weight" in keys:
                attribute["weight"] = float(attribute["weight"])
                attribute["cost"] = int(attribute["cost"])
                for key in keys:
                    if key != "weight" and key != "cost":
                        if attribute[key].isalpha() is True:
                            attribute[key] = lowers(attribute[key])
                        elif attribute[key].isdigit() is True:
                            attribute[key] = int(attribute[key])
                        elif "." in attribute[key] and attribute[key].endswith(".") is False:
                            attribute[key] = float(attribute[key])
                        else:
                            raise "Error!"
                obj = {"title": obj_name, "attributes": attribute}
                self.__datas[category][types].append(obj)
                self._all.add(obj_name)
            else:
                raise AttributesError(f"Attributes: [Cost / Weight]")
        else:
            raise DuplicateError(f"Object: [{obj_name}]")

    def change_object(self, obj_name: str, attribute, category: str, types: str):
        if obj_name in self._all:
            attribute = dict(obj.split("=") for obj in attribute.split("/"))
            keys = set(key for key in attribute.keys())
            if "cost" in keys and "weight" in keys:
                attribute["weight"] = float(attribute["weight"])
                attribute["cost"] = int(attribute["cost"])
            for key in keys:
                if key != "weight" and key != "cost":
                    if attribute[key].isalpha() is True:
                        attribute[key] = lowers(attribute[key])
                    elif attribute[key].isdigit() is True:
                        attribute[key] = int(attribute[key])
                    elif "." in attribute[key] and attribute[key].endswith(".") is False:
                        attribute[key] = float(attribute[key])
                    else:
                        raise "Error!"
                else:
                    if attribute[key].isdigit() is True:
                        attribute[key] = int(attribute[key])
                    elif "." in attribute[key] and attribute[key].endswith(".") is False:
                        attribute[key] = float(attribute[key])
                    else:
                        raise "Error!"
            index = self.__get_item_index(obj_name, category, types)
            obj = self.__datas[category][types][index]
            obj["attributes"].update(attribute)
            print(f"Object:[{obj_name}] Successful Edit")
        else:
            raise FoundError(f"Object: [{obj_name}]")

    def del_object(self, obj_name: str, category: str = None, types: str = None):
        if category is None and types is None:
            objs = list()
            key = 0
            for category in self.__datas:
                for types in self.__datas[category]:
                    index = 0
                    for item in self.__datas[category][types]:
                        title = item["title"]
                        if title.startswith(obj_name):
                            objs.append({"key": key, "title": item["title"], "path": f"{category}/{types}/{index}"})
                            key += 1
                        index += 1
            if len(objs) < 1:
                print(objs[0])
            else:
                for i in objs:
                    print(i)
                item = int(input("key item: "))
                path = None
                for obj in objs:
                    if obj["key"] == item:
                        path = obj["path"].split("/")
                del self.__datas[path[0]][path[1]][int(path[2])]
        else:
            index = 0
            for item in self.__datas[category][types]:
                if item["title"] == obj_name:
                    del self.__datas[category][types][index]
                    return print(f"Del Object:[{obj_name}] Completed!")
                else:
                    index += 1
        raise FoundError(f"Object: [{obj_name}]")

    # Settings Methods

    def change_settings(self,settings_name: str, attribute: str):
        if settings_name in self.__settings:
            if type(self.__settings[settings_name]) is bool and attribute == "true" or attribute == "false":
                self.__settings[settings_name] = True if attribute == "true" else False
            elif attribute.endswith("%") and settings_name == "factor_level_up_exp":
                self.__settings[settings_name] = attribute
            elif attribute.isdigit() and attribute != "secret_code" or attribute != "lang" or attribute != "version":
                self.__settings[settings_name] = int(attribute)
            else:
                if settings_name != "level_up":
                    self.__settings[settings_name] = attribute
                else:
                    print(f"You Can't Change This: [{settings_name}]")
        else:
            print(f"Fount Error Settings: [{settings_name}]\n")

    def get_setting(self, setting_name: str):
        if setting_name in self.__settings:
            return self.__settings[setting_name]
        else:
            raise FoundError(f"Setting [{setting_name}]!")

    def show_settings(self):
        clear()
        header = ["title","value"]
        body = []
        for key,value in self.__settings.items():
            body.append([key,value])
        print(tabulate(body, headers=header), "\n")

    # Start

    def start(self):
        settings = load_datas(path=self._config_path, message="Loading Files...Config.json")
        set_log = "Loading Files [Config.json] Completed!" if settings else "Loading Files [Config.json] Failed!"

        bases = load_datas(path=self._bases_path, utf_support=settings["utf-8"] if settings else False, message="Loading Files...Base.json")
        base_log = "Loading Files [Base.json] Completed!" if bases else "Loading Files [Bases.json] Failed!"

        objects = load_datas(path=self._objects_path, utf_support=settings["utf-8"] if settings else False, message="Loading Files...Objects.json")
        obj_log = "Loading Files [Objects.json] Completed!" if objects else "Loading Files [Objects.json] Failed!"

        if bases and objects and settings:
            self.__datas = dict(**bases, **objects)
            self.__settings = settings
            self.__packing_objects("Packing Objects...")
            pack_log = "Packing Objects Completed!" if self.__packing_status else "Packing Objects Failed!"
            if self.__packing_status:
                self.datas_status = True
                print(f"{base_log}\n{obj_log}\n{set_log}\n{pack_log}\n")
                write_log(logs=[base_log, obj_log,set_log, pack_log,str(datetime.datetime.now())])
            else:
                print(f"{base_log}\n{obj_log}\n{set_log}\n{pack_log}\n")
                write_log(logs=[base_log,obj_log,set_log,pack_log,str(datetime.datetime.now())])
        else:
            print(f"{base_log}\n{obj_log}\n{set_log}")
            print("Failed to load the necessary data to work with files and the program itself!")
            command = input("Try to recover files? [Y/n]: ")
            match command:
                case "Y" | "y": self.__recovery()
                case _: print("System Error!\n")

    def __recovery(self):
        objects = settings = bases = None
        base_log = obj_log = set_log = ""
        if os.path.exists(self._bases_path) is False:
            bases = load_datas(path=self._recovery_bases_path, message="Recovery [Base.json] Files...")
            base_log = "Recovery Bases Completed!" if bases else "Recovery Bases Failed!"
        if os.path.exists(self._objects_path) is False:
            objects = load_datas(path=self._recovery_objects_path, message="Recovery [Objects.json] Files...")
            obj_log = "Recovery Objects Completed!" if objects else "Recovery Objects Failed!"
        if os.path.exists(self._config_path) is False:
            settings = load_datas(path=self._recovery_config_path, message="Recovery [Config.json] Files...")
            set_log = "Recovery Config Completed!" if settings else "Recovery Config Failed!"
        write_log(logs=[base_log, obj_log, set_log, str(datetime.datetime.now())])
        match bases, objects, settings:
            case None: print("Failed Recovery Files!")
            case _:
                print("All Files Recovery Successfully")
                self.__datas = dict(**bases, **objects)
                self.__settings = settings
                self.datas_status = True

    def __backup(self):
        write_datas(path=self._backup_bases_path, datas=load_datas(self._bases_path), message="Backup Files...")
        write_datas(path=self._backup_objects_path, datas=load_datas(self._objects_path), message="Backup Files...")
        write_datas(path=self._backup_config_path, datas=load_datas(self._config_path), message="Backup Files...")

    def __all_save(self):
        write_datas(path=self._bases_path, datas={"base":self.__datas.__getitem__("base")}, utf_support=False if self.get_setting("utf-8") else True, message="Updating [Bases.json] Files...")
        write_datas(path=self._objects_path, datas={"objects":self.__datas.__getitem__("objects")}, utf_support=False if self.get_setting("utf-8") else True, message="Updating [Objects.json] Files...")
        write_datas(path=self._config_path, datas=self.__settings, message="Updating [Config.json] Files...")

    def shut_down(self, backup: bool = True):
        if self.__settings["use_backup"] or backup:
            self.__backup()
            self.__all_save()
        else:
            command = input("Do you want to make a backup procedure? [Y/n]: ")
            if command == "Y":
                self.__backup()
                self.__all_save()
            else:
                self.__all_save()
        print("All Files Was Updated Completed!")

    def load_backup(self):
        print("Loading Backup Files...")
        bases = load_datas(path=self._backup_bases_path) if os.path.exists(self._backup_bases_path) else None
        objects = load_datas(path=self._backup_objects_path) if os.path.exists(self._backup_objects_path) else None
        settings = load_datas(path=self._backup_config_path) if os.path.exists(self._backup_config_path) else None
        match bases, objects, settings:
            case None: raise "Error!"
            case _:
                self.__datas = dict(**bases, **objects)
                self.__settings = settings
                print("Loading Backup Completed!")
