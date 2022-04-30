import constants
import formuls


"""пр 18 """
"""Задание 1 """
"""
def calc(znak):
    try:
        a = float(input("Первое число: "))
        b = float(input("Второк число: "))
        c = float(input("Третье число: "))
        if znak == "+":
            res = a + b + c
            return res
        elif znak == "-":
            res = a - b - c
            return res
        elif znak == "/":
            res = a / b / c
            return res
        elif znak == "*":
            res = a * b * c
            return res
        else:
            print("Unknown operation")
    except ZeroDivisionError:
        return 0
    except NameError:
        print("Error:Unknown number")
        return "Error"
    except ValueError:
        print("Error:Unknown number")
        return "Error"
    else:
        print("Except Errors is not definite")
        return "Error"
    finally:
        print("Вывод результата произведён")
while True:
    result = calc((input("znak ")))
    if result != "Error":
        break
"""

"""Задание 2 """
"""
def prof(cords):
    try:
        cords["x"] = float(cords["x"])
        cords["y"] = float(cords["y"])
    except ValueError:
        return print("Error: cords is not be str")
    if cords["x"] <= 0 and cords["y"] <= 0:
        print ("находится в 3-ей четверти.")
    else:
        print ("не находится в 3-ей четверти.")
while True:
    cords = dict ()
    x = input("x: ")
    y = input("y: ")
    cords["x"] = x
    cords["y"] = y
    prof(cords)
"""

"""Задание 3-4 """
""" 
def ss(number,cc):
    try:
        number = int(number)
        cc = int(cc)
    except ValueError:
        return print("Error: str in not be int")
    if cc == 2:
        res = bin(number)
        print(res[2:])
    elif cc == 8:
        res = oct(number)
        print(res[2:])
    elif cc == 16:
        res = hex(number)
        print(res[2:])
    else:
        print("Unknown Система считсления")
def Requests(searh):
    searh = searh.lower(); searh = searh.title(); searh = searh.strip()
    if searh == "/Esc":
        return "Break"
    elif searh == "/Ss":
        print(ss(input("Введите число: "),input("Введите систему счисления: ")))
    else:
        print("Error")
while True:
    print("[/Esc]-выход из программы")
    x = Requests(input())
    if x == "Break":
        break
"""

"""Задание 5 не готово"""
"""
lst = dict()
txt = "apple orange orange banana credits form searh list list list"
txt = txt.split()
"""

"""пр 23 """




"""
class TLogElement:
    def __init__(self):
        self.__in1=False
        self.__in2=False
        self._res=False

    def __setIn1(self, NewIn1):
        self.__in1=NewIn1
        self.calc()

    def __setIn2(self, NewIn2):
        self.__in1=NewIn2
        self.calc()

    In1=property(lambda x: x.__in1, __setIn1)
    In2=property(lambda x: x.__in2, __setIn2)
    Res=property(lambda x: x._res)

class TNot(TLogElement):
    def __init__(self):
        TLogElement.__init__(self)
    def calc(self):
        self._res=not self.In1

class TAnd(TLog2In):
    def __init__(self):
        TLog2In.__init__(self)
    def calc(self):
        self._res=self.In1 and self.In2
"""


"""
from animals import *

p = Dog("шарик", 5)
p.gettingOrder()
print(p.name + ":", p.age, "лет")
"""

class Player_Date:
    def __init__(self, name, race, clas):
        self.Name = name
        self.Race = race
        self.Clas = clas
        self.Rank = "X"
    def getPlayerStat(self):
        return self.__dict__

    def __setName(self,NewName):
        try:
            if NewName.isalpha():
                self.Name = NewName
        except AttributeError:
            print("Ваше имя не может состоять из цифр")
    def getName(self):
        return self.Name

    def __setRace(self,NewRace):
        if NewRace in constants.Races.keys():
            self.Race = NewRace
        else:
            print("Вы вписали несуществующую расу")
    def getRace(self):
        return self.Race

    def __setClas(self,NewClas):
        if NewClas in constants.Races.keys():
            self.Clas = NewClas
        else:
            print("Вы вписали несуществующий класс")
    def getClas(self):
        return self.Clas

    def __setRank(self,NewRank):
        if NewRank in constants.Ranks:
            self.Rank = NewRank
        else:
            print("Вы вписали несуществующий ранг")
    def getRank(self):
        return self.Rank

    name = property(getName, setName)
    race = property(getRace, setRace)
    clas = property(getClas, setClas)
    rank = property(getRank, setRank)
    info = property(getPlayerStat)

class User(Player_Date):
    def __init__(self,name, race, clas):
        self.InventoryWeight = 14
        self.EqipWeight = 12
        self.Skill = {}
        self.Inventory = {}
        self.Eqip = {}
        super().__init__(name, race, clas)

    def __addInventory(self,NewItem):
        if NewItem <= InventoryWeight:
            self.Inventory = NewItem
        else:
            print("pass")
    def getInventory(self):
        return self.Inventory

    invent = property(getInventory, __addInventory)


while True:


player = User (input ("Имя: "),input ("Раса: "),input ("Класс: "))

while True:
    if act == "/Add Item":
        name = input ("Название предмета: ")
        amount = int (input ("Кол-во: "))
        try:
            player.invent = {name:{"Количество":player.invent[name]["Количество"] + amount,"Вес":(player.invent[name]["Количество"] + amount) * constants.Weights[name]},"Общий вес":(player.invent[name]["Количество"] + amount) * constants.Weights[name]}
        except KeyError:
            print ("Warning: Попытка добавить несуществующую вещь!")
    else:
        pass







