import json
from file_worker import *
from query_corrector import *

os.chdir(sys.path[0])
clears = lambda: os.system("cls")

class Redactor(CheckFiles, JsonFilesObjects, JsonFilesConstants, LiteSolidCoreConfig):
    r"""
    Redactor - дочерний класс, наследующий все свойства и методы супер классов: CheckFiles, JsonFilesObjects, JsonFilesConstants и LiteSolidCoreConfig
    [Optional] - Необязательное поле для заполнения.

    Основные команды дочернего класса:

    #Objects_config.json
    Object Name: [items, potions, artifacts, materials, equips, weapons] - Категория предметов
    Item Name - Название предмета
    Item Bonus Name - Название предметного бонуса
    Bonus Value - Числовое значение бонуса

    Read.Objects -> <[Optional]Object Name> | <[Optional]Item Name> -> Выводит информацию об объектах и/или объекте
    Add.Item -> <Object Name> | <Item Name> | <Item Bonus Name> | <Bonus Value> -> Добавляет объект в файл.
    Add.Item.Bonus -> <Item Name> | <New Item Bonus Name> | <Bonus Value> -> Добавляет существующему объекту дополнительные бонусы
    Change.Item -> <Item Name> | <Old Item Bonus Name> | <New Bonus Value> -> Изменяет бонусное значение существующего объекта
    Del.Item -> <Item Name> | <[Optional]Item Bonus Name> -> Удаляет либо сам объект, либо конкретный бонус объекта

    --------------------------------------------------------------------------------------------------------------------

    #Constants_config.json
    Constant Name: [characteristics, races, class, class_bonus, profs, specs, religions, ranks, skills, skills_bonus, abilities]
    -> Категория констант (условно константы, так как мы всё равно можете их изменить)
    Element Name - Название объекта в категории констант
    Element Bonus Name - Название предметного бонуса
    Bonus Value - Числовое значение бонуса

    Read.Constants -> <[Optional]Constant Name> | <[Optional]Element Name> -> Выводит информацию об объектах и/или объекте
    Add.Constant -> <Constant Name> | <Element Name> | <Element Bonus Name> | <Bonus Value> -> Добавляет объект в файл.
    Add.Constant.Bonus -> <Constant Name> | <Element Name> | <New Element Bonus Name> | <Bonus Value> -> Добавляет существующему объекту дополнительные бонусы
    Change.Constant -> <Constant Name> | <Element Name> | <Old Element Bonus Name> | <New Bonus Value> Изменяет бонусное значение существующего объекта
    Del.Constant -> <Constant Name> | <Element Name> | <[Optional]Element Bonus Name> -> Удаляет либо сам объект, либо конкретный бонус объекта

    --------------------------------------------------------------------------------------------------------------------

    #LSC_Config.json
    Read.Config
    Config Name - [inventory_size, equipment_size, max_skills, max_abilities, max_eqip, lang, version]

    Read.Config -> <[Optional]Config Name> -> Выводит информацию об конфигурациях и/или конфигурационном объекте


    Ecs - Выход из редактора
    """

    def __init__(self):
        CheckFiles.__init__(self)
        JsonFilesObjects.__init__(self)
        JsonFilesConstants.__init__(self)
        LiteSolidCoreConfig.__init__(self)

redact = Redactor()


def Requests(searh):
    print(searh)
    clears()

    #Objects_config.json
    if searh == "Read.Objects":
        redact.read_objects(lowers(lowers(input("[Optional]Object Name: "))), lowers(input("[Optional]Item Name: ")))
    elif searh == "Add.Item":
        redact.add_object_element(lowers(input("Object Name: ")), lowers(input("Item Name: ")), lowers(input("Item Bonus Name: ")), float(input("Bonus Value: ")))
    elif searh == "Add.Item.Bonus":
        redact.add_object_bonus(lowers(input("Item Name: ")), lowers(input("New Item Bonus Name: ")), float(input("Bonus Value: ")))
    elif searh == "Change.Item":
        redact.change_object_element(lowers(input("Item Name: ")), lowers(input("Old Item Bonus Name: ")), float(input("New Bonus Value: ")))
    elif searh == "Del.Item":
        redact.del_objects(lowers(input("Item Name: ")), lowers(input("[Optional]Item Bonus Name: ")))


    #Constants_config.json
    elif searh == "Read.Constants":
        redact.read_constant(lowers(input("[Optional]Constant Name: ")), lowers(input("[Optional]Element Name: ")))
    elif searh == "Add.Constant":
        redact.add_constant_element(lowers(input("Constant Name: ")), lowers(input("Element Name: ")), lowers(input("Element Bonus Name: ")), float(input("Bonus Value: ")))
    elif searh == "Add.Constant.Bonus":
        redact.add_constant_bonus(lowers(input("Constant Name: ")), lowers(input("Element Name: ")), lowers(input ("Element Bonus Name: ")), float (input ("Bonus Value: ")))
    elif searh == "Change.Constant":
        redact.change_constant_element(lowers(input("Constant Name: ")), lowers(input("Element Name: ")), lowers(input ("Element Bonus Name: ")), float (input ("New Bonus Value: ")))
    elif searh == "Del.Constant":
        redact.del_constant(lowers(input("Constant Name: ")), lowers(input("Element Name: ")), lowers(input("[Optional]Element Bonus Name: ")))


    #LSC_Config.json
    elif searh == "Read.Config":
        redact.read_constant(lowers(input("[Optional]Config Name: ")))


    elif searh == "Doc.Redactor":
        print(Redactor.__doc__)

    elif searh == "Ecs":
        return searh


def run():
    clears()
    print("Справка по редактору [Doc.Redactor]")
    while True:
        res = Requests(command(input("Действие: ")))
        if res == "Ecs":
            break
