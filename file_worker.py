import json
import pickle
import sys
import os
os.chdir(sys.path[0])

class CheckFiles:
    def __init__(self):pass

    @staticmethod
    def __check_json_constants():
        r"""Проверяет наличие файла Constants_config.json.
        Если не находит, то создаёт в папке Json_files.
        В дополнении, если он его находит, то проверяет, что его размер больше 230."""

        if os.path.exists ("Assets/Json_files/Constants_config.json"):
            size = os.path.getsize("Assets/Json_files/Constants_config.json")
            if size < 230:
                with open("Assets/Json_files/Constants_config.json", "w") as file:
                    Constants = {
                        "constants":{
                            "max_stats":[],
                            "min_stats":[],
                            "races":[],
                            "class":[],
                            "class_bonus": [],
                            "profs":[],
                            "specs":[],
                            "skills":[],
                            "skills_bonus":[],
                            "abilities":[]
                        }
                    }
                    json.dump(Constants, file, indent=2)
                    print ("File Constants Was Resets")

            else: pass

        else:
            with open ("Assets/Json_files/Constants_config.json", "w", encoding="utf-8") as file:
                Constants = {
                    "constants":{
                        "max_stats":[],
                        "min_stats":[],
                        "races":[],
                        "class":[],
                        "class_bonus":[],
                        "profs":[],
                        "specs":[],
                        "skills":[],
                        "skills_bonus":[],
                        "weights":[]
                    }
                }
                json.dump(Constants, file, indent=2)
                print ("File Constants Was Created")

    @staticmethod
    def __check_json_objects():
        r"""Проверяет наличие файла Objects_config.json.
        Если не находит, то создаёт в папке Json_files
        В дополнении, если он его находит, то проверяет, что его размер больше 145."""

        if os.path.exists("Assets/Json_files/Objects_config.json"):
            size = os.path.getsize("Assets/Json_files/Objects_config.json")
            if size < 145:
                with open ("Assets/Json_files/Objects_config.json","w") as file:
                    data = {
                        "objects":{
                            "items":[],
                            "potions":[],
                            "artifacts":[],
                            "materials":[],
                            "equips":[],
                            "abilities":[]
                        }
                    }
                    json.dump(data ,file, indent=2)
                    print("File Object Config Was Resets")

            else: pass

        else:
            with open("Assets/Json_files/Objects_config.json", "w") as file:
                data = {
                    "objects":{
                        "items":[],
                        "potions":[],
                        "artifacts":[],
                        "materials":[],
                        "equips":[],
                        "weapons":[]
                    }
                }
                json.dump(data, file, indent=2)
                print("File Object Config Was Created")

    @staticmethod
    def __check_json_lite_solid_core():
        r"""Проверяет наличие файла Lite_Solid_Core_Config.json.
        Если не находит, то создаёт в папке Json_files"""

        if os.path.exists("Assets/Json_files/Lite_Solid_Core_Config.json"):
            size = os.path.getsize("Assets/Json_files/Lite_Solid_Core_Config.json")
            if size < 145:
                with open ("Assets/Json_files/Lite_Solid_Core_Config.json","w") as file:
                    data = {
                        "configuration":{
                            "inventory_size": 14,
                            "equipment_size": 12,
                            "max_skills":9,
                            "max_abilities":12,
                            "max_eqip": 10,
                            "lang":"Ru"
                        }
                    }
                    json.dump(data ,file, indent=2)
                    print("File Lite_Solid_Core Config Was Resets")

            else: pass

        else:
            with open("Assets/Json_files/Lite_Solid_Core_Config.json", "w") as file:
                data = {
                    "configuration":{
                        "inventory_size":14,
                        "equipment_size":12,
                        "max_skills":9,
                        "max_abilities":12,
                        "max_eqip":10,
                        "lang":"Ru"
                    }
                }
                json.dump(data, file, indent=2)
                print("File Lite_Solid_Core Config Was Created")

    def checker_json_files(self):
        self.__check_json_lite_solid_core()
        self.__check_json_constants()
        self.__check_json_objects()

class JsonFilesConstants:
    def __init__(self):
        self.__Constants_Elements = set() #elements_name
        self.__Constants_Elements_Bonus = set() #elements_bonus_name
        self.__Constants = set() #constants_name

    @staticmethod
    def __load_datas():
        with open("Assets/Json_files/Constants_config.json", "r", encoding="utf-8") as file:
            return json.load(file)

    def __load_constants(self):
        datas = self.__load_datas()

        for const in datas["constants"]:
            self.__Constants.add(const)

    def __load_constants_element(self, constant_name, element_name):
        datas = self.__load_datas()
        index = 0

        if constant_name in self.__Constants:
            self.__Constants_Elements.clear()
            for item in datas["constants"][constant_name]:
                self.__Constants_Elements.add(item.get("element_name"))

            if element_name in self.__Constants_Elements:
                self.__Constants_Elements_Bonus.clear ()
                for item in datas["constants"][constant_name]:
                    if item.get ("element_name") == element_name:
                        array = set (datas["constants"][constant_name][index]["element_bonus"].keys ())
                        self.Constants_Elements_Bonus = array
                        return index
                    else:
                        index += 1

        elif constant_name is None or constant_name == "":
            self.__Constants_Elements.clear()
            for const in datas["constants"]:
                for item in datas["constants"][const]:
                    self.__Constants_Elements.add(item.get("element_name"))


    def read_constant(self, constant_name=None, element_name=None):
        datas = self.__load_datas()
        self.__load_constants()
        index = self.__load_constants_element(constant_name, element_name)
        count = 0

        if constant_name is None or constant_name == "":

            if element_name is None or element_name == "":
                for const in datas["constants"]:
                    for item in datas["constants"][const]:
                        count += 1
                        print(f"{const}:{item}")
                print("count:",count)

            elif element_name in self.__Constants_Elements:
                for const in datas["constants"]:
                    for item in datas["constants"][const]:
                        if item.get("element_name") == element_name:
                            count += 1
                            print(f"{const}:{item}")
                print("count:",count)

            else: raise KeyError (f"{element_name}: wasn't found")

        elif constant_name in self.__Constants:

            if element_name is None or element_name == "":
                for item in datas["constants"][constant_name]:
                    count += 1
                    print (f"{constant_name}:{item}")
                print("count:",count)

            elif element_name in self.__Constants_Elements:
                print(f"{constant_name}:{datas['constants'][constant_name][index]}")

            else:
                raise KeyError (f"{element_name}: wasn't found")

        else: raise KeyError(f"{constant_name}: wasn't found")


    def add_constant_element(self, constant_name, element_name, element_bonus_name, var_bonus):
        self.__load_constants()

        if constant_name in self.__Constants:

            self.__load_constants_element(constant_name, element_name)

            if element_name not in self.__Constants_Elements:

                if type(element_bonus_name) is str and var_bonus >= 0:
                    datas = self.__load_datas()
                    datas["constants"][constant_name].append({"element_name":element_name, "element_bonus":{element_bonus_name:var_bonus}})
                    with open("Assets/Json_files/Constants_config.json","w",encoding="utf-8") as file:
                        json.dump(datas, file, indent=2, ensure_ascii=False)
                    print(f"{element_name}: added successfully")

                else:
                    raise SyntaxError (f"{element_bonus_name}: not be int|float and {var_bonus}: not be str|<0")

            else:
                raise SyntaxError (f"{element_name}: already exists")

        else:
            raise KeyError(f"{constant_name}: wasn't found")

    def add_constant_bonus(self, constant_name, element_name, element_bonus_name, var_bonus):
        self.__load_constants()

        if constant_name in self.__Constants:

            index = self.__load_constants_element(constant_name, element_name)

            if element_name in self.__Constants_Elements and element_bonus_name not in self.Constants_Elements_Bonus:

                if type(element_bonus_name) is str and var_bonus >= 0:
                    datas = self.__load_datas()
                    datas["constants"][constant_name][index]["element_bonus"].update({element_bonus_name:var_bonus})
                    with open("Assets/Json_files/Constants_config.json","w",encoding="utf-8") as file:
                        json.dump(datas, file, indent=2, ensure_ascii=False)
                    print(f"{element_bonus_name}: added successfully")

                else:
                    raise SyntaxError (f"{element_bonus_name}:not be int|float and {var_bonus}: not be str|<0")

            else:
                raise SyntaxError (f"{element_name}: already exists")

        else:
            raise KeyError(f"{constant_name}: wasn't found")


    def get_constants(self, constant_name=None, element_name=None, element_bonus_name=None):
        datas = self.__load_datas()
        self.__load_constants()
        lst = list()

        if constant_name in self.__Constants:

            index = self.__load_constants_element(constant_name, element_name)

            if element_name is None or element_name == "":
                for item in datas["constants"][constant_name]:
                    lst.append (item.get("element_name"))
                array = set(lst)
                return array

            elif element_name in self.__Constants_Elements:

                if element_bonus_name is None or element_bonus_name == "":
                    return datas["constants"][constant_name][index]["element_bonus"]

                elif element_bonus_name in self.Constants_Elements_Bonus:
                    return datas["constants"][constant_name][index]["element_bonus"][element_bonus_name]

                else:
                    raise KeyError (f"{element_bonus_name}: wasn't found")

            else:
                raise KeyError(f"{element_name}: wasn't found")

        elif constant_name is None or constant_name == "":
            for const in datas["constants"]:
                for item in datas["constants"][const]:
                    lst.append(item.get("element_name"))
            array = set(lst)
            return array
        else:
            raise KeyError(f"{constant_name}: wasn't found")


    def change_constant_element(self, constant_name, element_name, element_bonus_name, var_bonus):
        self.__load_constants()

        if constant_name in self.__Constants:

            index = self.__load_constants_element(constant_name, element_name)

            if element_name in self.__Constants_Elements and element_bonus_name in self.Constants_Elements_Bonus:

                if var_bonus >= 0:
                    datas = self.__load_datas()
                    datas["constants"][constant_name][index]["element_bonus"][element_bonus_name] = var_bonus
                    with open ("Assets/Json_files/Constants_config.json","w",encoding="utf-8") as file:
                        json.dump(datas,file,indent=2,ensure_ascii=False)
                    print(f"{element_bonus_name}: changed successfully")

                else:
                    raise SyntaxError (f"{var_bonus}: not be str|<0")

            else:
                raise SyntaxError (f"{element_name}|{element_bonus_name}: wasn't found")

        else:
            raise SyntaxError(f"{constant_name}: wasn't found")


    def del_constant(self, constant_name, element_name, element_bonus_name=None):
        self.__load_constants()

        if constant_name in self.__Constants:

            index = self.__load_constants_element(constant_name, element_name)

            if element_name in self.__Constants_Elements:
                datas = self.__load_datas()

                if element_bonus_name is None or element_bonus_name == "":
                    del datas["constants"][constant_name][index]
                    with open ("Assets/Json_files/Constants_config.json","w",encoding="utf-8") as file:
                        json.dump (datas,file,indent=2,ensure_ascii=False)
                    print (f"{element_name}: successfully removed")

                elif element_bonus_name in self.Constants_Elements_Bonus:
                    del datas["constants"][constant_name][index]["element_bonus"][element_bonus_name]
                    with open ("Assets/Json_files/Constants_config.json","w",encoding="utf-8") as file:
                        json.dump (datas,file,indent=2,ensure_ascii=False)
                    print (f"{element_bonus_name}: successfully removed")

                else:
                    raise KeyError(f"{element_bonus_name} wasn't found")

            else:
                raise KeyError (f"{element_name}: wasn't found")

        else:
            raise KeyError (f"{constant_name}: wasn't found")

class JsonFilesObjects:
    def __init__(self):
        self.__Items = set() #items_name
        self.__Items_Bonus = set() #items_bonus_name
        self.__Objects = set() #objects_name

    @staticmethod
    def __load_datas():
        with open("Assets/Json_files/Objects_config.json","r",encoding="utf-8") as file:
            return json.load(file)

    def __load_objects(self):
        datas = self.__load_datas()

        for obj in datas["objects"]:
            self.__Objects.add(obj)

    def __load_items(self, object_name, item_name):
        datas = self.__load_datas()
        index = 0

        if object_name in self.__Objects:
            self.__Items.clear()
            for item in datas["objects"][object_name]:
                self.__Items.add(item.get("item_name"))

            if item_name in self.__Items:
                self.__Items_Bonus.clear()
                for item in datas["objects"][object_name]:
                    if item.get("item_name") == item_name:
                        array = set (datas["objects"][object_name][index]["item_stats"].keys())
                        self.__Items_Bonus = array
                        return index
                    else:
                        index += 1

        elif object_name is None or object_name == "":
            self.__Items.clear()
            for const in datas["objects"]:
                for item in datas["objects"][const]:
                    self.__Items.add(item.get("item_name"))

            if item_name in self.__Items:
                self.__Items_Bonus.clear()
                for obj in datas["objects"]:
                    index = 0
                    for item in datas["objects"][obj]:
                        if item.get("item_name") == item_name:
                            array = set(datas["objects"][obj][index]["item_stats"].keys())
                            self.__Items_Bonus = array
                            return obj, index
                        else:
                            index += 1


    def read_objects(self, object_name = None, item_name=None):
        datas = self.__load_datas()
        self.__load_objects()
        index = self.__load_items(object_name, item_name)
        count = 0

        if object_name is None or object_name == "":

            if item_name is None or item_name == "":
                for obj in datas["objects"]:
                    for item in datas["objects"][obj]:
                        count += 1
                        print(item)
                print("count: ",count)

            elif item_name in self.__Items:
                for const in datas["objects"]:
                    for item in datas["objects"][const]:
                        if item.get("item_name") == item_name:
                            count += 1
                            print(f"{const}:{item}")
                print("count:",count)

            else: raise KeyError(f"{item_name}: wasn't found")

        elif object_name in self.__Objects:

            if item_name is None or item_name == "":
                for item in datas["objects"][object_name]:
                    count += 1
                    print (f"{object_name}:{item}")
                print("count:",count)

            elif item_name in self.__Items: print(f"{object_name}:{datas['objects'][object_name][index]}")

            else: raise KeyError (f"{item_name}: wasn't found")

        else: raise KeyError(f"{object_name}: wasn't found")


    def add_object_element(self, object_name, item_name, item_stat, var_bonus):
        self.__load_objects()

        if object_name in self.__Objects:

            self.__load_items(object_name, item_name)

            if type(item_stat) is str and var_bonus >= 0:

                if item_name not in self.__Items:
                    datas = self.__load_datas()
                    datas["objects"][object_name].append({"item_name":item_name, "item_stats":{item_stat:var_bonus}})
                    with open ("Assets/Json_files/Objects_config.json","w",encoding="utf-8") as file:
                        json.dump (datas,file,indent=2,ensure_ascii=False)
                    print(f"{item_name}: added successfully")

                else:
                    raise KeyError(f"{item_name}: already exists")

            else:
                raise SyntaxError(f"{item_stat}: not be int|float and {var_bonus}: >= 0")

        else:
            raise KeyError(f"{object_name}: wasn't found")

    def add_object_bonus(self, item_name, item_stat, var_bonus):
        index = self.__load_items (None, item_name)

        if item_name in self.__Items and item_stat not in self.__Items_Bonus:

            if type (item_stat) is str and var_bonus >= 0:
                datas = self.__load_datas()
                datas["objects"][index[0]][index[1]]["item_stats"].update({item_stat:var_bonus})
                with open ("Assets/Json_files/Objects_config.json","w",encoding="utf-8") as file:
                    json.dump (datas,file,indent=2,ensure_ascii=False)
                print(f"{item_name}: added successfully")

            else:
                raise SyntaxError (f"{item_stat}: not be int|float and {var_bonus}: >= 0")

        else:
            raise KeyError (f"{item_name}: wasn't found or {item_stat}: already exists")


    def change_object_element(self, item_name, item_stat, var_bonus):
        index = self.__load_items(None, item_name)

        if item_name in self.__Items and item_stat in self.__Items_Bonus:

            if var_bonus >= 0:
                datas = self.__load_datas()
                datas["constants"][index[0]][index[1]]["item_stats"][item_stat] = var_bonus
                with open ("Assets/Json_files/Objects_config.json","w",encoding="utf-8") as file:
                    json.dump(datas,file,indent=2,ensure_ascii=False)
                print (f"{item_stat}: changed successfully")

            else:
                raise SyntaxError (f"{var_bonus}: not be str|<0")

        else:
            raise SyntaxError(f"{item_name}|{item_stat}: wasn't found")


    def get_object(self, object_name=None,item_name=None,item_stat=None):
        datas = self.__load_datas()
        self.__load_objects()
        index = self.__load_items (object_name,item_name)
        lst = list()

        if object_name in self.__Objects:


            if item_name in self.__Items:

                if item_stat is None or item_stat == "":
                    return datas["objects"][object_name][index]

                elif item_stat in self.__Items_Bonus:
                    return datas["objects"][object_name][index]["item_stats"][item_stat]

                elif item_stat == "all":
                    return datas["objects"][object_name][index]["item_stats"]

                else:
                    raise KeyError (f"{item_stat}: wasn't found")

            elif item_name is None or item_name == "":
                for obj in datas["objects"][object_name]:
                    lst.append(obj.get("item_name"))
                array = set(lst)
                return array
            else:
                raise KeyError(f"{item_name}: wasn't found")

        elif object_name is None or object_name == "":

            if item_name in self.__Items:

                if item_stat is None or item_stat == "":
                    return datas["objects"][index[0]][index[1]]

                elif item_stat in self.__Items_Bonus:
                    return datas["objects"][index[0]][index[1]]["item_stats"][item_stat]

                elif item_stat == "all":
                    return datas["objects"][index[0]][index[1]]["item_stats"]

                else:
                    raise KeyError (f"{item_stat}: wasn't found")

            elif item_name is None or item_name == "":
                for obj in datas["objects"]:
                    for item in datas["objects"][obj]:
                        lst.append (item.get ("item_name"))
                array = set (lst)
                return array

            else:
                raise KeyError (f"{item_name}: wasn't found")

        else:
            raise KeyError(f"{object_name}: wasn't found")


    def del_objects(self, item_name, item_stat=None):
        index = self.__load_items(None, item_name)

        if item_name in self.__Items:
            datas = self.__load_datas()

            if item_stat is None or item_stat == "":
                del datas["objects"][index[0]][index[1]]
                with open ("Assets/Json_files/Objects_config.json","w",encoding="utf-8") as file:
                    json.dump(datas,file,indent=2,ensure_ascii=False)
                print (f"{item_name}: successfully removed")

            elif item_stat in self.__Items_Bonus:
                del datas["objects"][index[0]][index[1]]["item_stats"][item_stat]
                with open("Assets/Json_files/Objects_config.json","w",encoding="utf-8") as file:
                    json.dump(datas,file,indent=2,ensure_ascii=False)
                print (f"{item_stat}: successfully removed")

            else:
                raise KeyError (f"{item_stat} wasn't found")

        else:
            raise KeyError (f"{item_name}: wasn't found")

class LiteSolidCoreConfig:
    def __init__(self):
        self.__Config = set()

    @staticmethod
    def __load_datas():
        with open("Assets/Json_files/Lite_Solid_Core_Config.json", "r") as file:
            return json.load(file)

    def __load_config(self):
        datas = self.__load_datas()
        self.__Config.clear()
        lst = list()

        for config in datas["configuration"]:
            lst.append(config)

        array = set(lst)
        self.__Config = array


    def read_config(self, config_name=None):
        datas = self.__load_datas()
        self.__load_config()

        if config_name is None or config_name == "":
            print(datas["configuration"].items())

        elif config_name in self.__Config:
            print(datas["configuration"][config_name])

        else:
            raise KeyError(f"{config_name}: wasn't found")


    def get_config(self, config_name=None):
        datas = self.__load_datas()
        self.__load_config()
        array = dict()

        if config_name is None or config_name == "":
            array.update(datas["configuration"])
            return array

        elif config_name in self.__Config:
            return datas["configuration"][config_name]

        else:
            raise KeyError(f"{config_name}: wasn't found")

class PickleFileUserDatas:
    def __init__(self):
        pass

    @staticmethod
    def check_pickle():
        if os.path.exists("Assets/User_datas/User_data.pickle"):
            return True
        else:
            raise FileNotFoundError("The user file wasn't found!")

    @staticmethod
    def load_pickle():
        with open("Assets/User_datas/User_data.pickle","rb") as file:
            print("File uploaded successfully")
            return pickle.load(file)


    def save_pickle(self, player):
        with open("Assets/User_datas/User_data.pickle","wb") as file:
            print("File saved successfully")
            pickle.dump(player, file)

CF = CheckFiles()
JFO = JsonFilesObjects()
JFC = JsonFilesConstants()
LSC = LiteSolidCoreConfig()
PFUD = PickleFileUserDatas()
CF.checker_json_files()




