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
                    count+=1
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
        self.AllInventoryWeight = 0
        self.MaxInventoryWeight = 14
        self.Inventory = {}

    def add_item(self, item_name, item_amount):
        self.ItemName = item_name
        self.ItemAmount = item_amount
        try:
            self.AllInventoryWeight = self.AllInventoryWeight + item_amount * constants.ItemsWeights[item_name]
            if self.AllInventoryWeight <= self.MaxInventoryWeight:
                self.Inventory[item_name] = {"Количество": item_amount, "Вес": item_amount * constants.ItemsWeights[item_name]}
                print(f"Предмет добавлен: [{item_name}]")
            else:
                print("В вашем инвентаре мало места!")
                self.AllInventoryWeight = self.AllInventoryWeight - item_amount * constants.ItemsWeights[item_name]
        except KeyError:
            print ("Warning: Попытка добавить несуществующую вещь!")

    def set_item(self, item_name, item_amount):
        self.ItemName = item_name
        self.ItemAmount = item_amount
        try:
            self.AllInventoryWeight = self.AllInventoryWeight + item_amount * constants.ItemsWeights[item_name]
            if self.AllInventoryWeight <= self.MaxInventoryWeight:
                self.Inventory[item_name] = {"Количество": item_amount+self.Inventory[item_name]["Количество"], "Вес": (item_amount+self.Inventory[item_name]["Количество"]) * constants.ItemsWeights[item_name]}
                print(f"Предмет обновлён: [{item_name}]")
            else:
                print("В вашем инвенторе мало места!")
                self.AllInventoryWeight = self.AllInventoryWeight - item_amount * constants.ItemsWeights[item_name]
        except KeyError:
            print("Warning: Попытка добавить несуществующую вещь!")

    def remove_item(self, item_name):
        self.ItemName = item_name
        if item_name in self.Inventory.keys():
            self.AllInventoryWeight = self.AllInventoryWeight - self.Inventory[item_name]["Вес"]
            del self.Inventory[item_name]
            print (f"Предмет удалён: [{item_name}]")
        else:
            print("Warning: Вы пытаетесь удалить предмет, которого и так нету!")

    def data_inventory(self):
        print(self.Inventory)

class Equipment():

    def __init__(self):
        self.AllIEqipWeight = 0
        self.MaxEqipWeight = 12
        self.Eqip = {}

    def add_eqip(self, eqip_name, eqip_amount):
        self.EqipName = eqip_name
        self.EqipAmount = eqip_amount
        try:
            self.AllIEqipWeight = self.AllIEqipWeight + eqip_amount * constants.ItemsWeights[eqip_name]
            if self.AllIEqipWeight <= self.MaxEqipWeight:
                self.Eqip[eqip_name] = {"Количество": eqip_amount, "Вес": eqip_amount * constants.ItemsWeights[eqip_name]}
                print (f"Предмет добавлен: [{eqip_name}]")
            else:
                print("В вашем снаряжении мало места!")
                self.AllIEqipWeight = self.AllIEqipWeight - eqip_amount * constants.ItemsWeights[eqip_name]
        except KeyError:
            print("Warning: Попытка надеть несуществующую вещь!")

    def remove_eqip(self, eqip_name):
        self.EqipName = eqip_name
        if eqip_name in self.Eqip.keys():
            self.AllIEqipWeight = self.AllIEqipWeight - self.Eqip[eqip_name]["Вес"]
            del self.Eqip[eqip_name]
            print(f"Предмет удалён: [{eqip_name}]")
        else:
            print("Warning: Вы пытаетесь снять предмет, которого на вас нету!")

    def data_eqip(self):
        print(self.Eqip)

class Player(Data):
    def __init__(self, name, race, clas, prof, spec):
        super().__init__(name, race, clas, prof, spec)
        #self.data = Data()
        self.characteristics = Characteristics()
        self.stats = {race: constants.Races[race], clas: constants.Class[clas], prof: constants.Profs[prof], spec: constants.Specs[spec]}
        self.skills = Skills()
        self.inventory = Inventory()
        self.equipment = Equipment()

    def data_player(self):
        print(self.__dict__)
#player2 = Player("User-Test", "Человек", "Воин", "Паладин", "Авангард")
#player2.skills.set_skills()
#player2.skills.get_skills()







