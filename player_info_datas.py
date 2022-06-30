import formulas
from random import randint
from file_worker import *

_config = LSC.get_config()
_items = JFO.get_object()

_weapons = JFO.get_object("weapons")
_equips = JFO.get_object("equips")
_wears = _weapons | _equips


_races = JFC.get_constants("races")
_classes = JFC.get_constants("class")
_profs = JFC.get_constants("profs")
_specs = JFC.get_constants("specs")
_rels = JFC.get_constants("religions")
_ranks = JFC.get_constants("ranks")

_info = _races | _classes | _profs | _specs | _rels | _ranks

_abilities = JFC.get_constants("abilities")


class Character:
    def __init__(self, name, race, clas, prof, spec, rel):
        self.info = {"имя":name, "раса":race, "класс":clas, "профессия":prof, "специализация":spec, "религия":rel,"ранг":"x"}
        self.char = {"здоровье":None,"мана":None,"выносливость":None,"защита":None,"урон":None}
        self.constant_char = {"здоровье":None,"мана":None,"выносливость":None,"защита":None,"урон":None}


    def __change_name(self, new_name):
        nn = new_name
        while True:
            if " " in new_name:
                new_name.replace(" ", "")
            else:
                break
        if new_name.isalpha() == True and len(new_name) > 2:
            self.info.update(имя=nn)
        else:
            print(f"Error: {nn} incorrect name")

    def __change_race(self, new_race):
        if new_race in _races:
            self.info.update(раса=new_race)
        else:
            print(f"Error: {new_race} incorrect name")

    def __change_clas(self, new_clas):
        if new_clas in _classes:
            self.info.update(класс=new_clas)
        else:
            print(f"Error: {new_clas} incorrect name")

    def __change_prof(self, new_prof):
        if new_prof in _profs:
            self.info.update(профессия=new_prof)
        else:
            print(f"Error: {new_prof} incorrect name")

    def __change_spec(self, new_spec):
        if new_spec in _specs:
            self.info.update(специализация=new_spec)
        else:
            print(f"Error: {new_spec} incorrect name")

    def __change_rel(self, new_rel):
        if new_rel in _rels:
            self.info.update(религия=new_rel)
        else:
            print(f"Error: {new_rel} incorrect name")

    def __change_rank(self, new_rank):
        if new_rank in _ranks:
            self.info.update(ранг=new_rank)
        else:
            print(f"Error: {new_rank} incorrect name")


    def get_info(self):
        return self.info

    def __get_name(self):
        return self.info["имя"]

    def __get_race(self):
        return self.info["раса"]

    def __get_clas(self):
        return self.info["класс"]

    def __get_prof(self):
        return self.info["профессия"]

    def __get_spec(self):
        return self.info["специализация"]

    def __get_rel(self):
        return self.info["религия"]

    def __get_rank(self):
        return self.info["ранг"]


    def __get_char(self):
        return self.char

    def __get_constant_char(self):
        return self.constant_char


    name = property(__get_name, __change_name)
    race = property(__get_race, __change_race)
    clas = property(__get_clas, __change_clas)
    prof = property(__get_prof, __change_prof)
    spec = property(__get_spec, __change_spec)
    rel = property(__get_rel, __change_rel)
    rank = property(__get_rank, __change_rank)


class Skills:

    def __init__(self):
        self.max_skills = _config["max_skills"]
        self.skills = dict()
        self.all_skills = JFC.get_constants("skills")
        #self.default = {"телосложение": None, "мастерство": None, "мудрость": None, "сила": None, "выносливость": None}

    def set_skills(self):
        user_skills = [input(f"{i} Скилл: ").lower() for i in range(1, 10)]
        #user_skills = ["сила", "торговля", "мудрость", "внимательность", "очарование", "обман", "телосложение", "поглощение", "адаптивность"]
        sets = set (user_skills)
        count = 0
        try:
            if len(sets) == self.max_skills:
                for skill in user_skills:
                    if skill in self.all_skills:
                        count += 1
                    else: raise KeyError(f"{skill}: wasn't found in all skills")
            else: raise SyntaxError(f"{user_skills} != 9")

            if count == 9:
                self.skills = {
                    user_skills[0]:5, user_skills[1]:4,
                    user_skills[2]:4, user_skills[3]:3,
                    user_skills[4]:3, user_skills[5]:3,
                    user_skills[6]:2, user_skills[7]:2,
                    user_skills[8]:2
                }

                for i in self.skills:
                    _config[i] = self.skills[i]
        except:
            pass

        else:
            print("Способности соответствуют списку способностей")
            return True

    def change_skills(self, old_skill, new_skill):
        if new_skill in self.all_skills and new_skill not in self.skills:

            if old_skill in self.skills:
                self.skills[new_skill] = self.skills.pop(old_skill)

                for i in self.skills:
                    _config[i] = self.skills[i]

            else: raise KeyError (f"{old_skill}: wasn't found")

        else: raise KeyError(f"{new_skill}: wasn't found")

class Abilities:

    def __init__(self):
        self.max_abilities = _config["max_abilities"]
        self.abilities = {}

    def add_abilities(self, new_abilities):
        if  len(self.abilities) < self.max_abilities and new_abilities not in self.abilities:
            if new_abilities in _abilities:
                self.abilities[new_abilities] = JFC.get_constants("abilities", new_abilities)

            else: print(f"{new_abilities}: wasn't found")

        else:
            print("Вы больше не можете изучать новые способности или вы уже её изучили!")

    def change_abilities(self, old_abilities, new_abilities):
        if new_abilities in _abilities and new_abilities not in self.abilities:

            if old_abilities in self.abilities:
                self.abilities[new_abilities] = self.abilities.pop(old_abilities)

            else: raise KeyError (f"{old_abilities}: wasn't found")

        else: raise KeyError(f"{new_abilities}: wasn't found")

    def del_abilities(self, abilities_name):
        pass

class Capability(Character, Skills, Abilities):
    def __init__(self, name, race, clas, prof, spec, rel):
        Abilities.__init__(self)
        Skills.__init__(self)
        Character.__init__(self, name, race, clas, prof, spec, rel)

    def set_char(self):
        self.char.update(здоровье=formulas.Calc_Hp(JFC.get_constants("characteristics","здоровье", "минимальное"),
                                                        _config["body"],
                                                        JFC.get_constants("profs", self.info["профессия"], "бонус"),
                                                        JFC.get_constants("specs", self.info["специализация"], "бонус"),
                                                        JFC.get_constants("races", self.info["раса"], "бонус"),
                                                        JFC.get_constants("class", self.info["класс"], "бонус"),
                                                        self.info["класс"]))

        self.char.update(выносливость=formulas.Calc_Sm(JFC.get_constants("characteristics", "выносливость", "минимальное"),
                                                        _config["dexterity"],
                                                        JFC.get_constants("profs",self.info["профессия"],"бонус"),
                                                        JFC.get_constants("specs",self.info["специализация"],"бонус"),
                                                        JFC.get_constants("races",self.info["раса"],"бонус"),
                                                        JFC.get_constants("class",self.info["класс"],"бонус"),
                                                        self.info["класс"]))

        self.char.update(мана=formulas.Calc_Mp(JFC.get_constants("characteristics", "мана", "минимальное"),
                                                        _config["wisdom"],
                                                        JFC.get_constants("profs",self.info["профессия"],"бонус"),
                                                        JFC.get_constants("specs",self.info["специализация"],"бонус"),
                                                        JFC.get_constants("races",self.info["раса"],"бонус"),
                                                        JFC.get_constants("class",self.info["класс"],"бонус"),
                                                        self.info["класс"]))

        self.char.update(защита=formulas.Calc_Df(JFC.get_constants("characteristics", "защита", "минимальное"),
                                                       _config["body"],
                                                       JFC.get_constants("class",self.info["класс"], "бонус"),
                                                       self.info["класс"]))

        self.char.update(урон=formulas.Calc_Dmg(JFC.get_constants("characteristics", "урон", "минимальное"),
                                                      _config["mastery"],
                                                      _config["power"],
                                                      _config["wisdom"],
                                                      self.info["класс"]))

        self.constant_char.update(
            здоровье=self.char["здоровье"],
            мана=self.char["мана"],
            выносливость=self.char["выносливость"],
            защита=self.char["защита"],
            урон=self.char["урон"])


class Inventory:
    def __init__(self):
        self.inventory_weight = 0
        self.inventory = {}
        self.inventory_size = _config["inventory_size"]
        self.inventory_cost = 0

    def add_item(self, item_name, item_amount):
        if item_name in _items:
            weight = self.inventory_weight + item_amount * JFO.get_object(None, item_name, "вес")
            if weight <= self.inventory_size:

                try:
                    amount = -1 * self.inventory[item_name]["количество"]
                    if amount <= item_amount:
                        self.inventory[item_name] = {
                            "количество": self.inventory[item_name]["количество"] + item_amount,
                            "вес": round((self.inventory[item_name]["количество"] + item_amount) * JFO.get_object(None, item_name, "вес"), 2),
                            "цена": JFO.get_object(None, item_name, "цена")
                        }
                        self.inventory_weight = round(weight,2)
                        self.inventory_cost += self.inventory[item_name]["цена"] * item_amount
                        print(f"Update: {item_name}")
                    else:
                        print(f"Error: {item_amount} < {amount}")

                except KeyError:
                    if item_amount <= 0:
                        raise ValueError(f"{item_amount} not be <= 0")
                    else:
                        self.inventory[item_name] = {
                            "количество": item_amount,
                            "вес": round(JFO.get_object(None, item_name, "вес") * item_amount, 2),
                            "цена": JFO.get_object(None, item_name, "цена")
                        }
                        self.inventory_weight = round(weight, 2)
                        self.inventory_cost += self.inventory[item_name]["цена"] * self.inventory[item_name]["количество"]
                        print(f"New: {item_name}")

                finally:
                    try:
                        if self.inventory[item_name]["количество"] <= 0:
                            self.inventory_cost -= self.inventory[item_name]["цена"] * self.inventory[item_name]["количество"]
                            del self.inventory[item_name]
                            print(f"Del: {item_name}")
                            return "0x0"
                        else:
                            return "0x0"
                    except KeyError:
                        print(f"{item_name}: wasn't found in the inventory")
                        return "0x1"
            else:
                print("you need more free weight")
                return "0x1"
        else:
            print(f"{item_name}: wasn't found")
            return "0x1"


    def read_inventory(self):
        print(f"Инвентарь: {self.inventory}")
        print(f"максимальный переносимый вес: {self.inventory_size}")
        print (f"Текущий переносимый вес: {self.inventory_weight}")
        print(f"Стоимость инвентаря: {self.inventory_cost}")

        return self.inventory, self.inventory_size, self.inventory_weight

    def del_item(self, item_name):
        if item_name in self.inventory:
            self.add_item(item_name, -self.inventory[item_name]["количество"])
        else:
            print (f"{item_name}: wasn't found in the inventory")

class Equipment:
    def __init__(self):
        self.equipment_weight = 0
        self.equipment = {}
        self.equipment_size = _config["equipment_size"]
        self.max_eqip = _config["max_eqip"]
        self.bonus = {"здоровье": 0, "мана": 0, "выносливость": 0, "защита": 0, "урон": 0, "вместимость": 0}


    def __auto_set_bonus(self, item_name, item_amount):
        bonus_name = JFO.get_object(None, item_name, "all")
        del bonus_name["цена"],bonus_name["вес"]

        item = [i for i in bonus_name]
        item = item[0]
        bonus = bonus_name[item]

        self.bonus[item] += bonus*item_amount


    def wear_equipment(self, item_name, item_amount):
        if item_name in _wears:
            weight = self.equipment_weight + item_amount * JFO.get_object(None, item_name, "вес")
            if weight <= self.equipment_size:

                try:
                    amount = -1 * self.equipment[item_name]["количество"]
                    if amount <= item_amount and self.max_eqip != 0:
                        self.equipment[item_name] = {
                            "количество": self.equipment[item_name]["количество"] + item_amount,
                            "вес": round((self.equipment[item_name]["количество"] + item_amount) * JFO.get_object(None, item_name, "вес"), 2),
                            "цена": JFO.get_object(None, item_name, "цена")
                        }
                        self.max_eqip -= item_amount
                        self.equipment_weight = round(weight, 2)
                        print (f"Update:{item_name}")
                    else:
                        print(f"Error: {item_amount} < {amount} or max_eqip = 0")

                except KeyError:
                    if item_amount < 0 or self.max_eqip == 0:
                        print(f"{item_amount}: <= 0 or max_eqip: = 0")
                    else:
                        self.equipment[item_name] = {
                            "количество": item_amount,
                            "вес": round(JFO.get_object(None, item_name, "вес") * item_amount, 2),
                            "цена": JFO.get_object(None, item_name, "цена")
                        }
                        self.max_eqip -= item_amount
                        self.equipment_weight = round(weight, 2)
                        print(f"{item_name}: Wearing")

                finally:
                    try:
                        if self.equipment[item_name]["количество"] <= 0:
                            del self.equipment[item_name]
                            print(f"Del:{item_name}")
                            self.__auto_set_bonus(item_name, item_amount)
                            return "0x0"
                        else:
                            self.__auto_set_bonus(item_name, item_amount)
                            return "0x0"
                    except KeyError:
                        print(f"{item_name}: wasn't found in the equipments")
                        return "0x1"
            else:
                print("You need more free weight or equipment = 0")
                return "0x1"
        else:
            print(f"{item_name}: wasn't found")
            return "0x1"


    def read_equipments(self):
        print(f"Снаряжение: {self.equipment}")
        print(f"максимальный переносимый вес: {self.equipment_size}")
        print (f"Текущий переносимый вес: {self.equipment_weight}")
        print (f"Количество оставшихся слотов под снаряжение: {self.max_eqip}")

    def del_equipments(self, item_name):
        if item_name in self.equipment:
            self.wear_equipment(item_name, -self.equipment[item_name]["количество"])
        else:
            print (f"{item_name}: wasn't found in the equipments")

class Storage(Inventory, Equipment):
    def __init__(self):
        Inventory.__init__(self)
        Equipment.__init__(self)

    def replace(self, item_name, item_amount, place):

        if place == "Inventory":
            if item_name in self.equipment:
                if item_amount <= self.equipment[item_name]["количество"]:
                    res = player.add_item(item_name, item_amount)
                    print(res)
                    if res == "0x0":
                        player.wear_equipment(item_name, -item_amount)
                    else:
                        print (f"Error: {item_name} failed to replace")

        elif place == "Equipment":
            if item_name in self.inventory and item_name in _wears:
                if item_amount <= self.inventory[item_name]["количество"]:
                    res = self.add_item(item_name, item_amount)
                    if res == "0x0":
                        self.add_item(item_name, -item_amount)
                    else:
                        print(f"Error: {item_name} failed to replace")
                else:
                    print(f"Error: {item_amount} inappropriate quantity")
            else:
                print(f"Error: {item_name} is not equipment")

        else:
            print(f"Error: {place} wasn't found")


class Player(Storage, Capability):
    def __init__(self, name, race, clas, prof, spec, rel):
        Storage.__init__(self)
        Capability.__init__(self, name, race, clas, prof, spec, rel)
        self.live = True
        self.success = False
        self.count = 0


    def sell(self, item_name, item_amount):
        if item_name in self.inventory and 1 <= item_amount <= self.inventory[item_name]["количество"]:
            while True:
                try:
                    if "торговля" in self.skills:
                        res = formulas.Sell(self.inventory[item_name]["цена"], self.inventory["деньги"]["количество"], item_amount, self.skills["торговля"], JFC.get_constants("торговля","продажа"))
                        if res is not None:
                            res = res - self.inventory["деньги"]["количество"]
                            self.add_item("деньги", res)
                            self.add_item(item_name, -item_amount)
                    else:
                        res = self.inventory["деньги"]["количество"] + JFO.get_object(None, item_name, "цена")* item_amount
                        if res is not None:
                            res = res - self.inventory["деньги"]["количество"]
                            self.add_item("деньги", res)
                            self.add_item(item_name, -item_amount)
                    break
                except KeyError:
                    self.add_item("деньги", 1)
        else:
            print("Вы пытаетесь продать предмет, которого у вас нету или вы продаёте предмет в большем/меньшем колличестве, в котором он у вас есть в действительности!")

    def buy(self,item_name, item_amount):
        if item_name in _items and item_amount >= 1:
            weight = self.inventory_weight + self.inventory[item_name]["вес"] + JFO.get_object (None,item_name, "вес") * item_amount
            if weight <= self.inventory_weight:
                try:
                    if "торговля" in self.skills:
                        res = formulas.Buy (self.inventory[item_name]["цена"],self.inventory["деньги"]["количество"], item_amount,self.skills["торговля"],JFC.get_constants ("торговля","покупка"))
                        if res >= 0:
                            if weight <= self.inventory_weight:
                                res = res - self.inventory["деньги"]["количество"]
                                self.add_item("деньги",res)
                                self.add_item(item_name, item_amount)
                            else:
                                print (f"Вам не хватает места: [{weight - self.inventory_weight}Кг]")
                        else:
                            print (f"Вам не хватает денег: [{-1 * res}]")
                    else:
                        res = self.inventory["деньги"]["вес"] - self.inventory[item_name]["цена"]
                        if res >= 0:
                            if weight <= self.inventory_weight:
                                res = res - self.inventory["деньги"]["количество"]
                                self.add_item ("деньги",res)
                                self.add_item (item_name,item_amount)
                            else:
                                print (f"Вам не хватает места: [{weight - self.inventory_weight}Кг]")
                        else:
                            print (f"Вам не хватает денег: [{-1 * res}]")
                except KeyError:
                    print ("У вас нету денег!")
            else:
                print(f"Вам не хватает места: [{weight-self.inventory_weight}Кг]")
        else:
            print("Вы пытаетесь купить предмет, которого не существует или вы вписали отрицательное значение!")

    def craft(self, item_name, item_amount):
        if item_name in _items and item_amount >= 1:
            try:
                if "мудрость" in self.skills:
                    res = formulas.Сommon(JFC.get_constants("skills","изобретательность","бонус"), self.skills["изобретательность"]+1)
                else:
                    res = formulas.Сommon(JFC.get_constants("skills","изобретательность","бонус"), self.skills["изобретательность"])
            except KeyError:
                res = formulas.Сommon(JFC.get_constants("skills","изобретательность","бонус"), 0)
            finally:
                if res is True:
                    try:
                        weight = self.inventory_weight + self.inventory[item_name]["вес"] + JFO.get_object(None, item_name, "вес") * item_amount
                        if weight <= self.inventory_weight:
                            self.add_item(item_name,item_amount)
                        else:
                            print(f"Вам не хватает места: [{weight - self.inventory_weight}Кг]")
                    except KeyError:
                        print(f"{item_name} wasn't found in Objects_config.json")
                else:
                    print("Вместо предмета у вас вышел лишь металалом")
                    try:
                        weight = self.inventory_weight + JFO.get_object("materials", "металалом", "вес") * randint(1, 6)
                        if weight <= self.inventory_weight:
                            self.add_item(item_name,item_amount)
                        else:
                            print(f"Вам не хватает места: [{weight - self.inventory_weight}Кг] для металлолома")
                    except KeyError:
                        print("металалом: wasn't found in Objects_config.json")
        else:
            print("Вы где-то допустили ошибку!")


    def learn(self, learn_name):
        if learn_name in _abilities:
            if "мудрость" in self.skills:
                res = formulas.Learn(JFC.get_constants("skills","мудрость", "бонус"), JFC.get_constants("class_bonus", self.info["класс"], "мудрость"), self.skills["мудрость"], self.info["класс"])
                if res is True:
                    self.add_abilities(learn_name)
                    print(f"Вам удалось изучить: [{learn_name}]")
                else:
                    print(f"Вам не удалось изучить: [{learn_name}]")
            else:
                res = formulas.Learn(JFC.get_constants("skills","мудрость", "бонус"), JFC.get_constants("class_bonus", self.info["класс"], "мудрость"), 1, self.info["класс"])
                if res is True:
                    self.add_abilities(learn_name)
                    print(f"Вам удалось изучить: [{learn_name}]")
                else:
                    print(f"Вам не удалось изучить: [{learn_name}]")

    def block(self, damage):
        if damage >= 0:
            try:
                res = formulas.Сommon(JFC.get_constants("skills", "сила", "бонус"), self.skills["сила"])
            except KeyError:
                res = formulas.Сommon (JFC.get_constants("skills","сила","бонус"), 0)
            finally:
                if res is True:
                    print("Урон не получен")
                else:
                    damage = damage - self.char["защита"]
                    if damage > 0:
                        hp = self.char["здоровье"] - damage
                        if hp > 0:
                            self.char.update(здоровье=hp)
                        else:
                            self.char.update(здоровье=hp)
                            self.live = False
                            print("Вы умерли, так как получили критический урон")
                    else:
                        print("Урон не получен")
        else:
            print("Урон не может быть отрицательным!")

    def dodge(self, damage):
        if damage >= 0:
            try:
                res = formulas.Сommon(JFC.get_constants("skills", "выносливость", "бонус"),self.skills["выносливость"])
            except KeyError:
                res = formulas.Сommon (JFC.get_constants ("skills","выносливость","бонус"), 0)
            finally:
                if res is True:
                    print("Вы смогли увернуться")
                else:
                    damage = damage - self.char["защита"]
                    if damage > 0:
                        hp = self.char["здоровье"] - damage
                        if hp > 0:
                            self.char.update (здоровье=hp)
                        else:
                            self.char.update (здоровье=hp)
                            self.live = False
                    else:
                        print ("Вы не смогли увернуться, но благодаря защите, урон был нивелирован")
        else:
            print("Урон не может быть отрицательным!")

    def proof(self, hindrance):
        try:
            self.success = formulas.Сommon(JFC.get_constants("skills","социальность","бонус")+self.count, self.skills["социальность"], hindrance)
        except KeyError:
            self.success = formulas.Сommon(JFC.get_constants ("skills","социальность","бонус")+self.count, hindrance)
        finally:
            if self.success is True:
                self.count = 0
                print("Вам доверяют")
            else:
                self.count += 2.5
                print("Вы вызываете подозрение")

    def hack(self, hindrance=0):
        try:
            if "мудрость" or "адаптивность" in self.skills:
                self.success = formulas.Сommon(JFC.get_constants("skills","взлом","бонус")+self.count, hindrance, self.skills["взлом"]+1)
            else:
                self.success = formulas.Сommon(JFC.get_constants("skills","взлом","бонус")+self.count, hindrance, self.skills["взлом"])
        except KeyError:
            if "мудрость" or "адаптивность" in self.skills:
                self.success = formulas.Сommon(JFC.get_constants("skills","взлом","бонус")+self.count, hindrance, _config["hack"])
            else:
                self.success = formulas.Сommon(JFC.get_constants ("skills","взлом","бонус")+self.count, hindrance,)
        finally:
            if self.success is True:
                self.count = 0
                print (f"Вам удалось взломать объект")
            else:
                self.count += 2.5
                print (f"Вам не удалось взломать объект")

    def check(self, hindrance):
        try:
            if "кошачий глаз" in self.skills:
                self.success = formulas.Сommon(JFC.get_constants("skills","внимательность","бонус")+self.count, hindrance, self.skills["внимательность"]+1)
            else:
                self.success = formulas.Сommon(JFC.get_constants("skills","внимательность","бонус")+self.count, hindrance, self.skills["внимательность"])
        except KeyError:
            if "кошачий глаз" in self.skills:
                self.success = formulas.Сommon(JFC.get_constants("skills","внимательность","бонус")+self.count, hindrance, 1.5)
            else:
                self.success = formulas.Сommon(JFC.get_constants("skills","внимательность","бонус")+self.count, hindrance)
        finally:
            if self.success is True:
                self.count = 0
                print("Вы что-то подозреваете")
            else:
                self.count += 2.5
                print("Вы ничего не подозреваете")

    def steal(self, item_name, item_amount, hindrance=0):
        if item_name in _items:
            try:
                self.success = formulas.Сommon(JFC.get_constants("skills","воровство","бонус") + self.count, self.skills["воровство"], hindrance)
            except KeyError:
                self.success = formulas.Сommon (JFC.get_constants ("skills","воровство","бонус") + self.count, hindrance)
            finally:
                if self.success is True:
                    self.count = 0
                    self.add_item(item_name, item_amount)
                else:
                    self.count += 2.5
                    print ("Вам не удалось украсть предмет")
        else:
            print (f"{item_name}: wasn't found in Objects_config.json")


"""
player = Player("User-Test", "человек", "воин", "наёмник", "смешенный", "сихритизм")
player.set_skills()
player.set_char()
"""