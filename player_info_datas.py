import constants


class Data():
    def __init__(self, name, race, clas, prof, spec):
        self.Name = name
        self.Race = race
        self.Clas = clas
        self.Prof = prof
        self.Spec = spec
        self.Rel = "Сихритизм"
        self.Rank = "X"
    def data_info(self):
        print(self.name, self.Race, self.Clas, self.Prof, self.Spec, self.Rel, self.Rank)

    def set_mame(self, NewName):
        try:
            if NewName.isalpha():
                self.Name = NewName
        except AttributeError:
            print("Ваше имя не может состоять из цифр")
    def get_name(self):
        return self.Name

    def set_race(self, NewRace):
        if NewRace in constants.Races.keys():
            self.Race = NewRace
        else:
            print("Вы вписали несуществующую расу")
    def get_race(self):
        return self.Race

    def set_clas(self, NewClas):
        if NewClas in constants.Class.keys():
            self.Clas = NewClas
        else:
            print("Вы вписали несуществующий класс")
    def get_clas(self):
        return self.Clas

    def set_prof(self, NewProf):
        if NewProf in constants.Profs.keys():
            self.Prof = NewProf
        else:
            print("Вы вписали несуществующию профессию")
    def get_prof(self):
        return self.Prof

    def set_rank(self, NewRank):
        if NewRank in constants.Ranks:
            self.Rank = NewRank
        else:
            print("Вы вписали несуществующий ранг")
    def get_rank(self):
        return self.Rank

    name = property(get_name, set_mame)
    race = property(get_race, set_race)
    clas = property(get_clas, set_clas)
    prof = property(get_prof, set_prof)
    rank = property(get_rank, set_rank)

class Characteristics():

    def __init__(self):
        self.Hp = 100
        self.Mp = 40
        self.Sm = 60
        self.DF = 4
        self.DMG = 20

    def set_hp(self, NewHp):
        pass

    def set_mp(self, NewMp):
        pass

    def set_sm(self, NewSm):
        pass

    def set_df(self, NewDf):
        pass

    def set_dmg(self, NewDmg):
        pass

    def data_characteristics(self):
        print(self.__dict__)
"""
class Data():
    def __init__(self, name, race, clas, prof, spec, rel):
        self.Name = name
        self.Race = race
        self.Clas = clas
        self.Prof = prof
        self.Spec = spec
        self.Rel = rel
        self.Rank = "X"
    def data_info(self):
        print(self.__dict__)

    def set_mame(self, NewName):
        try:
            if NewName.isalpha():
                self.Name = NewName
        except AttributeError:
            print("Ваше имя не может состоять из цифр")
    def get_name(self):
        return self.Name

    def set_race(self, NewRace):
        if NewRace in constants.Races.keys():
            self.Race = NewRace
        else:
            print("Вы вписали несуществующую расу")
    def get_race(self):
        return self.Race

    def set_clas(self, NewClas):
        if NewClas in constants.Class.keys():
            self.Clas = NewClas
        else:
            print("Вы вписали несуществующий класс")
    def get_clas(self):
        return self.Clas

    def set_prof(self, NewProf):
        if NewProf in constants.Profs.keys():
            self.Prof = NewProf
        else:
            print("Вы вписали несуществующию профессию")
    def get_prof(self):
        return self.Prof

    def set_rank(self, NewRank):
        if NewRank in constants.Ranks:
            self.Rank = NewRank
        else:
            print("Вы вписали несуществующий ранг")
    def get_rank(self):
        return self.Rank

    name = property(get_name, set_mame)
    race = property(get_race, set_race)
    clas = property(get_clas, set_clas)
    prof = property(get_prof, set_prof)
    rank = property(get_rank, set_rank)
"""

class Skills():

    def __init__(self):
        self.MaxSkills = 9
        self.Skills = dict()

    def set_skills(self):
        lstskills = input("9 Скилов через пробел: ").lower().title().split()
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

    def get_skills(self):
        print(self.Skills)

class Inventory():

    def __init__(self):
        self.__AllInventoryWeightSize = 0
        self.MaxInventoryWeightSize = 14
        self.__Inventory = {}

    def add_item(self, item_name, item_amount):
        if item_name in constants.ItemsWeights.keys():
            try:
                Size = self.__AllInventoryWeightSize + item_amount * constants.ItemsWeights[item_name]
                if Size <= self.MaxInventoryWeightSize:
                    self.__Inventory[item_name] = {"Количество": item_amount+self.__Inventory[item_name]["Количество"], "Вес": (item_amount+self.__Inventory[item_name]["Количество"]) * constants.ItemsWeights[item_name]}
                    self.__AllInventoryWeightSize = Size
                    if self.__Inventory[item_name]["Количество"] <= 0:
                        del self.__Inventory[item_name]
                        print(f"Предмет удалён: [{item_name}]")
                    else:
                        print(f"Предмет обновлён: [{item_name}]")
                else:
                    print("В вашем инвентаре мало места!""\n"f"Вам не хватает: [{Size-self.MaxInventoryWeightSize}]кг")
            except KeyError:
                Size = self.__AllInventoryWeightSize + item_amount * constants.ItemsWeights[item_name]
                if Size <= self.MaxInventoryWeightSize:
                    self.__Inventory[item_name] = {"Количество": item_amount, "Вес": item_amount * constants.ItemsWeights[item_name]}
                    self.__AllInventoryWeightSize = Size
                    print(f"Предмет добавлен: [{item_name}]")
                else:
                    print("В вашем инвентаре мало места!""\n"f"Вам не хватает: [{Size-self.MaxInventoryWeightSize}кг]")
        else:
            print(f"Такого предмета не существует в константах: [{item_name}]")

    def remove_item(self, item_name):
        if item_name in self.__Inventory.keys():
            self.__AllInventoryWeightSize -= self.__Inventory[item_name]["Вес"]
            del self.__Inventory[item_name]
            print(f"Предмет удалён: [{item_name}]")
        else:
            print("Warning: Вы пытаетесь удалить предмет, которого нету!")
        return self.__Inventory

    def get_inventory(self):
        print(self.__Inventory)

class Equipment():

    def __init__(self):
        self.__AllIEqipWeightSize = 0
        self.MaxEqipWeightSize = 12
        self.__Eqip = {}

    def add_item(self, item_name, item_amount):
        if item_name in constants.ItemsWeights.keys():
            try:
                Size = self.__AllIEqipWeightSize + item_amount * constants.ItemsWeights[item_name]
                if Size <= self.MaxEqipWeightSize:
                    self.__Eqip[item_name] = {"Количество": item_amount+self.__Eqip[item_name]["Количество"], "Вес": (item_amount+self.__Eqip[item_name]["Количество"]) * constants.ItemsWeights[item_name]}
                    self.__AllIEqipWeightSize = Size
                    if self.__Eqip[item_name]["Количество"] <= 0:
                        del self.__Eqip[item_name]
                        print(f"Предмет удалён: [{item_name}]")
                    else:
                        print(f"Предмет обновлён: [{item_name}]")
                else:
                    print("В вашем инвентаре мало места!""\n"f"Вам не хватает: [{Size-self.MaxEqipWeightSize}]кг")
            except KeyError:
                Size = self.__AllIEqipWeightSize + item_amount * constants.ItemsWeights[item_name]
                if Size <= self.MaxEqipWeightSize:
                    self.__Eqip[item_name] = {"Количество": item_amount, "Вес": item_amount * constants.ItemsWeights[item_name]}
                    self.__AllIEqipWeightSize = Size
                    print(f"Предмет добавлен: [{item_name}]")
                else:
                    print("В вашем инвентаре мало места!""\n"f"Вам не хватает: [{Size-self.MaxEqipWeightSize}кг]")
        else:
            print(f"Такого предмета не существует в константах: [{item_name}]")

    def remove_item(self, item_name):
        if item_name in self.__Eqip.keys():
            self.__AllIEqipWeightSize -= self.__Eqip[item_name]["Вес"]
            del self.__Eqip[item_name]
            print(f"Предмет удалён: [{item_name}]")
        else:
            print("Warning: Вы пытаетесь удалить предмет, которого нету!")

    def get_eqip(self):
        print(self.__Eqip)

class Player(Data):
    def __init__(self, name, race, clas, prof, spec):
        super().__init__(name, race, clas, prof, spec)
        #self.data = Data()
        self.characteristics = Characteristics()
        self.stats = {race: constants.Races[race], clas: constants.Class[clas], prof: constants.Profs[prof], spec: constants.Specs[spec]}
        self.skills = Skills()
        self.inventory = Inventory()
        self.equipment = Equipment()

    def get_player(self):
        print(self.__dict__)

player2 = Player("User-Test", "Человек", "Воин", "Паладин", "Авангард")





