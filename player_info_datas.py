from random import *
import constants
import formuls
import items

class Data:
    def __init__(self, name, race, clas, prof, spec):
        self.Name = name
        self.Race = race
        self.Clas = clas
        self.Prof = prof
        self.Spec = spec
        self.Rel = "Сихритизм"
        self.Rank = "X"

    def data_info(self):
        pass

    def __set_mame(self, NewName):
        try:
            if NewName.isalpha():
                self.Name = NewName
        except AttributeError:
            print("Ваше имя не может состоять из цифр")
    def __get_name(self):
        return self.Name

    def __set_race(self, NewRace):
        if NewRace in constants.Races.keys():
            self.Race = NewRace
        else:
            print("Вы вписали несуществующую расу")
    def __get_race(self):
        return self.Race

    def __set_clas(self, NewClas):
        if NewClas in constants.Class.keys():
            self.Clas = NewClas
        else:
            print("Вы вписали несуществующий класс")
    def __get_clas(self):
        return self.Clas

    def __set_prof(self, NewProf):
        if NewProf in constants.Profs.keys():
            self.Prof = NewProf
        else:
            print("Вы вписали несуществующую профессию")
    def __get_prof(self):
        return self.Prof

    def __set_spec(self, NewSpec):
        if NewSpec in constants.Specs:
            self.Spec = NewSpec
        else:
            print("Вы вписали несуществующую специализацию")
    def __get_spec(self):
        return self.Spec

    def __set_rel(self, NewRel):
        if NewRel in constants.Religions:
            self.Rel = NewRel
        else:
            print("Вы вписали несуществующую религию")
    def __get_rel(self):
        return self.Rel

    def __set_rank(self, NewRank):
        if NewRank in constants.Ranks:
            self.Rank = NewRank
        else:
            print("Вы вписали несуществующий ранг")
    def __get_rank(self):
        return self.Rank

    name = property(__get_name, __set_mame)
    race = property(__get_race, __set_race)
    clas = property(__get_clas, __set_clas)
    prof = property(__get_prof, __set_prof)
    spec = property(__get_spec, __set_spec)
    rank = property(__get_rank, __set_rank)

class Skills:

    def __init__(self):
        self.MaxSkills = 9
        self.Skills = dict()
        self.Body = 1
        self.Master = 1
        self.Brein = 1
        self.Power = 1
        self.Dexterity = 1

    def set_skills(self):
        #lstskills = input("9 Скилов через пробел: ").lower().title().split()
        lstskills = ["Торговля", "Мастерство", "Сила", "Телосложение", "Очарование", "Воля", "Ловкость", "Ресурсы", "Благословение"]
        count = 0
        lenlstskills = set(lstskills)
        if len(lenlstskills) == self.MaxSkills:
            for i in lstskills:
                if i in constants.Skills.keys():
                    count +=1
                    if count == 9:
                        print("Все навыки соответствуют константному списку навыков!")
                        self.Skills = {
                            lstskills[0]: 4,
                            lstskills[1]: 3,
                            lstskills[2]: 3,
                            lstskills[3]: 2,
                            lstskills[4]: 2,
                            lstskills[5]: 2,
                            lstskills[6]: 1,
                            lstskills[7]: 1,
                            lstskills[8]: 1}
                        return True
                else:
                    count -= 1
        else:
            print("Вы ввели меньше 9 навыков или вовсе несуществующие навыки или же, навыки повторяются")

    def ref_skills(self):
        if "Мудрость" in self.Skills:
            self.Brein = self.Skills["Мудрость"]
        else:
            pass
        if "Телосложение" in self.Skills:
            self.Body = self.Skills["Телосложение"]
        else:
            pass
        if "Сила" in self.Skills:
            self.Power = self.Skills["Сила"]
        else:
            pass
        if "Ловкость" in self.Skills:
            self.Dexterity = self.Skills["Ловкость"]
        else:
            pass
        if "Мастерство" in self.Skills:
            self.Master = self.Skills["Мастерство"]
        else:
            pass

    """
    def set_skills(self, lstskills):
        #lstskills = ["Изобретательность", "Мастерство", "Сила", "Телосложение", "Очарование", "Воля", "Ловкость", "Ресурсы", "Благословение"]
        count = 0
        lenlstskills = set(lstskills)
        if len(lenlstskills) == self.MaxSkills:
            for i in lstskills:
                if i in constants.Skills.keys():
                    count +=1
                    if count == 9:
                        print("Все навыки соответствуют константному списку навыков!")
                        self.Skills = {
                            lstskills[0]:4,
                            lstskills[1]:3,
                            lstskills[2]:3,
                            lstskills[3]:2,
                            lstskills[4]:2,
                            lstskills[5]:2,
                            lstskills[6]:1,
                            lstskills[7]:1,
                            lstskills[8]:1}
                        return True
                else:
                    count -= 1
        else:
            print("Вы ввели меньше 9 навыков или вовсе несуществующие навыки или же, навыки повторяются")
    """
    def __change_skills(self, NewSkill):
        if NewSkill in constants.Skills.keys():
            Skill = input("Напишите название скила, который хотите заменить: ")
            if Skill in self.Skills.keys():
                self.Skills[NewSkill] = self.Skills.pop(Skill)
            else:
                print("Вы не можете заменить этот скил, так как его нету у персонажа.")
        else:
            print("Новый скилл не соответствует константам скилов!")

    def __get_skills(self):
        return self.Skills

    skil = property(__get_skills, __change_skills)

class Abilities:

    def __init__(self):
        self.MaxAbilitiesSize = 12
        self.slot_limit = 0
        self.Abilities = {}

    def add_abilitie(self, abilities_name):
        if self.slot_limit < self.MaxAbilitiesSize:
            self.Abilities[abilities_name] = constants.Abilities.get(abilities_name)
            self.slot_limit += 1
        else:
            print("Вы больше не можете изучать новые способности!")

    def get_abilitie(self):
        return self.Abilities

class Storage:

    def __init__(self):
        self.inventory_weight = 0 #не трогать! в неё записывается общий размер всех предметов из инвентаря, а потом сравнивается с максимальным размером инвентаря inventory_size
        self.equipment_weight = 0 #не трогать! в неё записывается общий размер всех предметов из снаряжения, а потом сравнивается с максимальным размером инвентаря equipment_size

        self.inventory = {} #не трогать!
        self.inventory_size = 14 #Можно трогать

        self.equipment_size = 12 #Можно трогать
        self.equipment = {} #не трогать!
        self.slot_limit = 10 #Можно трогать. Отвечает за максимальное кол-во обмундирования в equipment

    def add_item(self, stor, item_name, item_amount):
        if stor == "/Add Item":
            if item_name in items.Objects and item_amount != 0:
                weight = self.inventory_weight + item_amount * items.All_Items[item_name]["weight"]
                if weight <= self.inventory_size:
                    try:
                        res = -1 * self.inventory[item_name]["amount"]
                        if res <= item_amount:
                            self.inventory[item_name] = {
                                "amount": self.inventory[item_name]["amount"] + item_amount,
                                "weight": (self.inventory[item_name]["amount"] + item_amount) * items.All_Items[item_name]["weight"],
                                "cost": items.All_Items[item_name]["cost"]
                            }
                            self.inventory_weight = weight
                            print(f"Update:{item_name}")
                        else: print("Error item_amount+")
                    except KeyError:
                        if item_amount < 0:
                            print("Error item_amount")
                        else:
                            self.inventory[item_name] = {
                                "amount": item_amount,
                                "weight": items.All_Items[item_name]["weight"] * item_amount,
                                "cost": items.All_Items[item_name]["cost"]
                            }
                            self.inventory_weight = weight
                            print(f"New:{item_name}")
                    finally:
                        try:
                            if self.inventory[item_name]["amount"] <= 0:
                                del self.inventory[item_name]
                                print(f"Del:{item_name}")
                        except KeyError:
                            print(f"this item is not defined in the inventory: {item_name}")
                else:
                    print("You need more free weight")
            else:
                print(f"Unknown Item: {item_name}")
        elif stor == "/Add Equip":
            if item_name in items.Equip and item_amount != 0:
                weight = self.equipment_weight + item_amount * items.Equip[item_name]["weight"]
                if weight <= self.equipment_size:
                    try:
                        res = -1 * self.equipment[item_name]["amount"]
                        if res <= item_amount and self.slot_limit != 0:
                            self.equipment[item_name] = {
                                "amount": self.equipment[item_name]["amount"] + item_amount,
                                "weight": (self.equipment[item_name]["amount"] + item_amount) * items.Equip[item_name]["weight"],
                                "cost": items.Equip[item_name]["cost"]
                            }
                            self.slot_limit = self.slot_limit - item_amount
                            self.equipment_weight = weight
                            print(f"Update:{item_name}")
                        else: print("Error item_amount+ or equipment is more than 10")
                    except KeyError:
                        if item_amount < 0 or self.slot_limit == 0:
                            print("Error item_amount+")
                        else:
                            self.equipment[item_name] = {
                                "amount": item_amount,
                                "weight": items.Equip[item_name]["weight"] * item_amount,
                                "cost": items.Equip[item_name]["cost"]
                            }
                            self.slot_limit -= item_amount
                            self.equipment_weight = weight
                            print(f"New:{item_name}")
                    finally:
                        try:
                            if self.equipment[item_name]["amount"] <= 0:
                                del self.equipment[item_name]
                                print(f"Del:{item_name}")
                        except KeyError:
                            print(f"this item is not defined in the inventory: {item_name} or equipment is more than 10")
                else:
                    print("You need more free weight or equipment is more than 10")
            else:
                print(f"Unknown Item: {item_name}")
        else: print("Unknown Command")

    def del_item(self, stor, item_name):
        if stor == "/Del Equip":
            if item_name in self.equipment:
                self.equipment_weight -= self.equipment[item_name]["weight"]
                self.slot_limit += self.equipment[item_name]["amount"]
                del self.equipment[item_name]
                print(f"Del: {item_name}")
            else: print("Unknown equip")
        elif stor == "/Del Item":
            if item_name in self.inventory:
                self.inventory_weight -= self.inventory[item_name]["weight"]
                del self.inventory[item_name]
                print(f"Del: {item_name}")
            else: print("Unknown item")
        else: print("Unknown Command")

    def replace_item(self, stor, item_name):
        if stor == "/Replace Equip":
            if item_name in self.equipment:
                print("No Work")
        elif stor == "/Wear Equip":
            print ("No Work")
        else: print("Unknown Command")

    def get_equipment(self):
        print(f"{self.equipment_weight}: {self.equipment}")

    def get_inventory(self):
        print(f"{self.inventory_weight}: {self.inventory}")

class Player(Data):
    def __init__(self, name, race, clas, prof, spec):
        super().__init__(name, race, clas, prof, spec)
        self.Hp = None
        self.Mp = None
        self.Df = None
        self.Sm = None
        self.DMG = None
        self.Basis = {}
        self.constbas = []
        self.stats = {race: constants.Races[race], clas: constants.Class[clas], prof: constants.Profs[prof], spec: constants.Specs[spec]}
        self.abilities = Abilities()
        self.skills = Skills()
        self.storage = Storage()

    def set_char(self):
        self.Hp = constants.Min["MinHP"] + (self.skills.Body * ((self.stats[self.prof] * self.stats[self.Spec]) + (self.stats[self.race] * self.stats[self.clas])))
        self.Mp = constants.Min["MinMP"] + (self.skills.Brein * ((self.stats[self.prof] * self.stats[self.Spec]) + (self.stats[self.race] * self.stats[self.clas])))
        self.Sm = constants.Min["MinSM"] + (self.skills.Dexterity * ((self.stats[self.prof] * self.stats[self.Spec]) + (self.stats[self.race] * self.stats[self.clas])))
        self.Df = constants.Min["MinDF"] + self.skills.Brein
        self.DMG = constants.Min["MinDMG"] + self.skills.Master * self.skills.Dexterity * self.skills.Power * self.skills.Brein
        if self.clas == "Маг":
            self.Hp = int(self.Hp / 1.4)
            self.Mp = int(self.Mp * 1.3)
            self.Sm = int(self.Sm / 1.3)
            self.Df = int(self.Df * 1.1)
            self.DMG = int(self.DMG * 1.2)
        elif self.clas == "Воин":
            self.Hp = int(self.Hp * 1.4)
            self.Mp = int(self.Mp / 1.3)
            self.Sm = int(self.Sm * 1.3)
            self.Df = int(self.Df * 1.2)
        elif self.clas == "Стрелок":
            self.Hp = int(self.Hp / 1.4)
            self.Mp = int(self.Mp * 1.2)
            self.Sm = int(self.Sm * 1.2)
            self.Df = int(self.Df * 1.2)
            self.DMG = int(self.DMG * 1.3)
        elif self.clas == "Никто":
            self.Hp = constants.Min["MinHP"]
            self.Mp = constants.Min["MinMP"]
            self.Sm = constants.Min["MinSM"]
            self.Df = int(self.Df * 1.4)
            self.DMG = int(self.DMG * 1.5)
        else:
            print("Ваш класс не обнаружен в константах, но даже так, характеристики будут расчитаны, но только рандомно!")
            self.Hp = int(self.Hp * randint(1, 3))
            self.Mp = int(self.Mp * randint(1, 3))
            self.Sm = int(self.Sm * randint(1, 3))
            self.Df = int(self.Df * randint(1, 3))
            self.DMG = int(self.DMG * randint(1, 3))
        self.Basis = {"Hp": self.Hp, "Mp": self.Mp, "Sm": self.Sm, "Df": self.Df, "Dmg": self.DMG}
        self.constbas = [self.Hp, self.Mp, self.Sm, self.Df, self.DMG]

    def ref_char_bonus(self):
        self.Basis["Hp"] = self.constbas[0] + self.equipment.EqipBonus["HP"]
        self.Basis["Mp"] = self.constbas[1] + self.equipment.EqipBonus["MP"]
        self.Basis["Sm"] = self.constbas[2] + self.equipment.EqipBonus["SM"]
        self.Basis["Df"] = self.constbas[3] + self.equipment.EqipBonus["DF"]
        self.Basis["Dmg"] = self.constbas[4] + self.equipment.EqipBonus["DMG"]
        self.inventory.MaxInventoryWeightSize = 14 + self.equipment.EqipBonus["Weight"]
        self.equipment.MaxEqipWeightSize = 12 + self.equipment.EqipBonus["Weight"]

    def ref_char(self):
        if self.Hp > self.Basis["Hp"]:
            self.Hp = self.Basis["Hp"]
        if self.Mp > self.Basis["Mp"]:
            self.Mp = self.Basis["Mp"]
        if self.Sm > self.Basis["Sm"]:
            self.Sm = self.Basis["Sm"]

    def sell(self, item_name, item_amount):
        if item_name in self.storage.inventory and 1 <= item_amount <= self.storage.inventory[item_name]["amount"]:
            while True:
                try:
                    if "Торговля" in self.skills.Skills:
                        res = formuls.Sell(self.storage.inventory[item_name]["cost"], self.storage.inventory["Деньги"]["amount"], item_amount, self.skills.Skills["Торговля"], constants.SkillsBonus["Торговля"]["Продажа"])
                        if res == "Error":
                            pass
                        else:
                            res = res - self.storage.inventory["Деньги"]["amount"]
                            self.storage.add_item("/Add Item", "Деньги", res)
                            self.storage.add_item("/Add Item", item_name, -item_amount)
                    else:
                        res = self.storage.inventory["Деньги"]["amount"] + items.All_Items[item_name]["cost"] * item_amount
                        if res == "Error":
                            pass
                        else:
                            res = res - self.storage.inventory["Деньги"]["amount"]
                            self.storage.add_item("/Add Item", "Деньги", res)
                            self.storage.add_item("/Add Item", item_name, -item_amount)
                    break
                except KeyError:
                    self.storage.add_item("/Add Item", "Деньги", 1)
        else:
            print("Вы пытаетесь продать предмет, которого у вас нету или вы продаёте предмет в большем/меньшем колличестве, в котором он у вас есть!")

    def buy(self, item_name, item_amount):
        if item_name in items.Objects and item_amount >= 1:
            try:
                if "Торговля" in self.skills.Skills:
                    res = formuls.Buy(self.storage.inventory[item_name]["cost"], self.storage.inventory["Деньги"]["amount"], item_amount, self.skills.Skills["Торговля"], constants.SkillsBonus["Торговля"]["Покупка"])
                    weight = self.storage.inventory[item_name]["weight"] + items.All_Items[item_name]["weight"] * item_amount
                    if res == "Error" or weight > self.storage.inventory_size:
                        pass
                    elif res >= 0:
                        res = res - self.storage.inventory["Деньги"]["amount"]
                        self.storage.add_item("/Add Item", "Деньги", res)
                        self.storage.add_item("/Add Item", item_name, item_amount)
                    else:
                        print(f"Вам не хватает денег: [{-1*res}]")
                else:
                    res = self.storage.inventory["Деньги"]["amount"] - self.storage.inventory[item_name]["cost"]
                    if res >= 0:
                        res = res - self.storage.inventory["Деньги"]["amount"]
                        self.storage.add_item("/Add Item", "Деньги", res)
                        self.storage.add_item("/Add Item", item_name, item_amount)
                    else:
                        print(f"Вам не хватает денег: [{-1*res}]")
            except KeyError:
                print("У вас нету денег!")
        else:
            print("Вы пытаетесь купить предмет, которого не существует или вы вписали отрицательное значение!")

    def get_char(self):
        print(f"HP:{self.Hp} | MP:{self.Mp} | SM:{self.Sm} | DF:{self.Df} | DMG:{self.DMG}")

    def learn(self, learn_name):
        if learn_name in constants.Abilities:
            if "Мудрость" in self.skills.Skills:
                res = formuls.Learn(constants.Skills["Мудрость"], self.clas, self.skills.Skills["Мудрость"], constants.SkillsBonus["Мудрость"])
                if res == "Успеx":
                    self.abilities.add_abilitie(learn_name)
                    print(f"Вам удалось изучить: [{learn_name}]")
                else:
                    print(f"Вам не удалось изучить: [{learn_name}]")
            else:
                res = formuls.Learn(constants.Skills["Мудрость"], self.clas, 0, 0)
                if res == "Успеx":
                    self.abilities.add_abilitie(learn_name)
                    print(f"Вам удалось изучить: [{learn_name}]")
                else:
                    print(f"Вам не удалось изучить: [{learn_name}]")

    def block(self, damage):
        if 0<= damage <= 999:
            if "Сила" in self.skills.Skills:
                res = formuls.Сommon_Success(constants.Skills["Сила"], self.skills.Skills["Сила"], constants.SkillsBonus["Сила"]["Блок"])
                if res == "Успеx":
                    print("Урон не получен")
                else:
                    self.Hp -= damage
                    print(f"HP:[{self.Hp}]")
            else:
                res = formuls.Сommon_Success(constants.Skills["Сила"], 0, 0)
                if res == "Успех":
                    print("Урон не получен")
                else:
                    self.Hp -= damage
                    print(f"HP:[{self.Hp}]")
        else:
            print("Урон не может быть отрицательным или выше 999")

    def craft(self, item_name, item_amount):
        if item_name in items.Objects and 1 <= item_amount <= 8:
            if "Изобретательность" in self.skills.Skills:
                res = formuls.Сommon_Success(constants.Skills["Изобретательность"], self.skills.Skills["Изобретательность"], constants.SkillsBonus["Изобретательность"])
                if res == "Успеx":
                    self.storage.add_item("/Add Item", item_name, item_amount)
                else:
                    print("Вместо предметов у вас вышел лишь металалом")
                    self.storage.add_item("/Add Item", "Металалом", randint(1, 6))
            else:
                res = formuls.Сommon_Success(constants.Skills["Изобретательность"], 0, 0)
                if res == "Успеx":
                    self.storage.add_item("/Add Item", item_name, item_amount)
                else:
                    print("Вместо предметов у вас вышел лишь металалом")
                    self.storage.add_item("/Add Item", "Металалом", randint(1, 6))

        else:
            print("Вы где-то допустили ошибку!")

    def dodge(self, damage):
        if 0<= damage <= 999:
            if "Ловкость" in self.skills.Skills:
                res = formuls.Сommon_Success(constants.Skills["Ловкость"], self.skills.Skills["Ловкость"], constants.SkillsBonus["Ловкость"])
                if res == "Успеx":
                    print("Вы смогли увернуться")
                else:
                    self.hp = damage
                    print(f"HP:[{self.hp}]")
            else:
                res = formuls.Сommon_Success(constants.Skills["Ловкость"], 0, 0)
                if res == "Успех":
                    print("Вы смогли увернуться")
                else:
                    self.hp = damage
                    print(f"HP:[{self.hp}]")
        else:
            print("Урон не может быть отрицательным или выше 999")

    def steal(self, item_name, item_amount):
        if 1 <= item_amount <= 640:
            if "Воровство" in self.skills.Skills:
                res = formuls.Сommon_Success(constants.Skills["Воровство"], self.skills.Skills["Воровство"], constants.SkillsBonus["Воровство"])
                if res == "Успеx":
                    self.storage.add_item("/Add Item", item_name, item_amount)
                else:
                    print("Вам не удалось украсть предмет")
            else:
                res = formuls.Сommon_Success(constants.Skills["Воровство"], 0, 0)
                if res == "Успех":
                    self.storage.add_item("/Add Item", item_name, item_amount)
                else:
                    print("Вам не удалось украсть предмет")
        else:
            print("Вы либо пытались украсть отрицательное число предметов, либо слишком много за раз!")

    def hack(self, item_name):
        if item_name in items.Objects:
            if "Взлом" in self.skills.Skills:
                res = formuls.Сommon_Success(constants.Skills["Внимательность"], self.skills.Skills["Взлом"], constants.SkillsBonus["Взлом"])
                if res == "Успеx":
                    print(f"Вам удалось взломать: [{item_name}]")
                else:
                    print("Вам не удалось взломать объект")
            else:
                res = formuls.Сommon_Success(constants.Skills["Внимательность"], 0, 0)
                if res == "Успех":
                    print(f"Вам удалось взломать: [{item_name}]")
                else:
                    print("Вам не удалось взломать объект")
        else:
            print("Вы не можете взломать то, что логически не поддаётся взлому ")

    def check(self):
        if "Внимательность" in self.skills.Skills:
            res = formuls.Сommon_Success(constants.Skills["Внимательность"], self.skills.Skills["Внимательность"], constants.SkillsBonus["Внимательность"])
            if res == "Успеx":
                print("Вы что-то заметили")
            else:
                print("Вы ничего не обнаружили")
        else:
            res = formuls.Сommon_Success(constants.Skills["Внимательность"], 0, 0)
            if res == "Успех":
                print("Вы что-то заметили")
            else:
                print("Вы ничего не обнаружили")

    def proof(self):
        if "Социальность" in self.skills.Skills:
            res = formuls.Сommon_Success(constants.Skills["Социальность"], self.skills.Skills["Социальность"], constants.SkillsBonus["Социальность"])
            if res == "Успеx":
                print("Вам доверяют")
            else:
                print("Вы вызываете подозрение")
        else:
            res = formuls.Сommon_Success(constants.Skills["Социальность"], 0, 0)
            if res == "Успех":
                print("Вам доверяют")
            else:
                print("Вы вызываете подозрение")

    def get_player(self):
        pass





"""
player2 = Player("User-Test", "Человек", "Воин", "Паладин", "Авангард")
player2.skills.set_skills()
player2.skills.ref_skills()
player2.set_char()
player2.storage.add_item("/Add Item", "Снежные Сапоги", 5)
player2.storage.add_item("/Add Item", "Колчан", 5)
player2.storage.get_inventory()
player2.storage.add_item("/Add Equip", "Снежные Сапоги", 5)
player2.storage.add_item("/Add Equip", "Колчан", 5)
player2.sell("Снежные Сапоги", 5)
player2.storage.get_inventory()
player2.sell("Деньги", 2461)
player2.storage.get_inventory()
"""