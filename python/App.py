from FileWorker import db
from Corrector import *
from Player import Player
from Redactor import requests
import Formulas
import os
from os import listdir
from os.path import isfile, join

clear = lambda: os.system('cls')


class App:
    def __init__(self):
        self._items = db.get_all_objects(category="objects",types="items") | db.get_all_objects(category="objects",types="weapons") | db.get_all_objects(category="objects",types="equips")
        self._abilities = db.get_all_objects(category="base",types="abilities")
        self._wears = db.get_all_objects(category="objects",types="weapons") | db.get_all_objects(category="objects",types="equips")
        self._info = {"race":db.get_all_objects(category="base", types="races")} | \
                     {"class":db.get_all_objects(category="base", types="class")} | \
                     {"profession":db.get_all_objects(category="base", types="profs")} | \
                     {"specialization":db.get_all_objects(category="base", types="specs")} | \
                     {"religion":db.get_all_objects(category="base", types="religions")} | \
                     {"rank":db.get_all_objects(category="base", types="ranks")}
        self.player_load = False

    @staticmethod
    def version():
        clear()
        return db.get_setting("version")

    @staticmethod
    def redact():
        clear()
        while True:
            req = command(input("request: "))
            match req:
                case "back": break
                case _: requests(search=req)

    def create_player(self):
        clear()
        name = lowers(input("Player Name: "))
        temp_player = {"race": None, "class": None, "profession": None, "specialization": None, "religion": None}

        for key in [key for key in temp_player.keys()]:
            if temp_player[key] is None or temp_player[key] not in self._info[key]:
                temp_info = list(self._info[key].copy())
                temp_keys = dict()
                for i in range(len(temp_info)):
                    temp_keys[i] = temp_info[i]
                print(temp_keys)
                temp_player[key] = temp_keys[int(input(f"Player {key}: "))]
        temp_player["name"] = name

        accessible_skills = list(db.get_all_objects(category="base",types="skills").copy())
        temp_accessible_skills = dict()
        for i in range(len(accessible_skills)):
            temp_accessible_skills[i] = accessible_skills[i]
        temp_skills = dict()
        for i in range(1,db.get_setting(setting_name="max_skills")+1):
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

        # temp_player = {"name":"Clyoucker", "race": "human", "class": "nobody", "profession": "paladin", "specialization": "vanguard", "religion": "grottoism"}
        # temp_skills = {'body': 5, 'wisdom': 4, 'scouting': 4, 'accuracy': 3, 'sociability': 3, 'carefully': 3, 'charm': 2, 'strong stomach': 2, 'horse riding': 2}

        body = temp_skills["body"] if "body" in temp_skills else 0.5
        wisdom = temp_skills["wisdom"] if "wisdom" in temp_skills else 0.5
        master = temp_skills["master"] if "master" in temp_skills else 0.5
        power = temp_skills["power"] if "power" in temp_skills else 0.5
        dexterity = temp_skills["dexterity"] if "dexterity" in temp_skills else 0.5

        health = Formulas.calc_hp(body=body,prof=temp_player["profession"],spec=temp_player["specialization"],race=temp_player["race"],clas=temp_player["class"])
        mana = Formulas.calc_mp(wisdom=wisdom,prof=temp_player["profession"],spec=temp_player["specialization"],race=temp_player["race"],clas=temp_player["class"])
        stamina = Formulas.calc_sm(dexterity=dexterity,prof=temp_player["profession"],spec=temp_player["specialization"],race=temp_player["race"],clas=temp_player["class"])
        protection = Formulas.calc_df(body=body,clas=temp_player["class"])
        damage = Formulas.calc_dmg(power=power,master=master,wisdom=wisdom,clas=temp_player["class"])

        temp_characteristics = {"health":health, "mana":mana, "stamina":stamina, "protection":protection, "damage":damage}

        global player
        player = Player(information=temp_player, characteristics=temp_characteristics, skills=temp_skills)
        self.player_load = True
        print("Player was Created!\n")

    def load(self):
        clear()
        if "player" not in globals() and "player" != object:
            path = "../assets/saves/pickles"
            files = [f for f in listdir(path) if isfile(join(path, f))]
            selector = {i:files[i] for i in range(len(files))}
            print(selector)
            global player
            player = db.load_pickle(file_name=selector[int(input("Select Key Save: "))].split(".")[0])
            self.player_load = True
        else:
            print("the player is already loaded!\n")

    def save(self):
        clear()
        if self.player_load:
            file_name = f"{player.information['name']}"
            db.save_pickle(player=player,file_name=file_name)
        else:
            print("Trying to save a blank sheet!\n")


def main():
    db.start()
    if db.datas_status is True:
        app = App()
        try:
            while True:
                if db.get_setting("lang") == "Eng":
                    print("Launched Request: Func processing of basic requests")
                    print("Read Documentation.md for information about app commands")
                    request = (command(input("Request: ")))
                    match request:
                        case "app.version" | "version": print(app.version(),"\n")
                        case "app.redactor" | "redactor": app.redact()
                        case "create.player" | "create": app.create_player()
                        case "load.player" | "load": app.load()
                        case "save.player" | "save": app.save()
                        case "player.actions" | "actions":
                            if "player" in globals() and isinstance(player,Player):
                                clear()
                                while True and player.live:
                                    print("Actions Request: Func processing of basic requests")
                                    action = (command(input("Action: ")))
                                    try:
                                        match action:
                                            # Action Funcs
                                            case "attack" | "a": player.attack(monster_type=input("Enemy: "))
                                            case "block" | "b": player.block_attack(damage=int(input("Enemy Damage: ")),hindrance=int(input("Hindrance [0-100]: ")))
                                            case "dodge" | "d": player.dodge_attack(hindrance=int(input("Hindrance [0-100]: ")))
                                            case "craft" | "ct": player.craft_item(item_name=input("Item Name: "),item_amount=int(input("Item Amount: ")),hindrance=int(input("Hindrance [0-100]: ")))
                                            case "hack" | "h": player.hack_item(hindrance=int(input("Hindrance [0-100]: ")))
                                            case "steal" | "s": player.steal_item(item_name=input("Item Name: "),item_amount=int(input("Item Amount: ")),hindrance=int(input("Hindrance [0-100]: ")))
                                            case "check" | "c": player.check(hindrance=int(input("Hindrance [0-100]: ")))
                                            case "use.potion" | "u": player.use_item(item_name=input("Item Name: "))

                                            # Inventory + Equipments Funcs
                                            case "add.item" | "add": player.add_item(item_name=input("Item Name: "),item_amount=int(input("Item Amount: ")))
                                            case "buy.item" | "buy": player.buy_item(item_name=input("Item Name: "),item_amount=int(input("Item Amount: ")))
                                            case "sell.item" | "sell": player.sell_item(item_name=input("Item Name: "),item_amount=int(input("Item Amount: ")))
                                            case "decrease.item" | "sub.item": player.decrease_item(item_name=input("Del Item Name: "),item_amount=int(input("Item Amount: ")))
                                            case "del.item": player.del_item(item_name=input("Del Item Name: "))
                                            case "reset.inventory": player.reset_inventory()
                                            case "inventory.status" | "i":player.inventory_status()

                                            case "wear.equip" | "wear": player.wear_equipment(item_name=input("Item Name: "),item_amount=int(input("Item Amount: ")))
                                            case "take.of.equip" | "take.of": player.take_of_equipment(item_name=input("Item Name: "),item_amount=int(input("Item Amount: ")))
                                            case "del.equip": player.del_equipments(item_name=input("Del Item: "))
                                            case "equip.status" | "e": player.equipment_status()

                                            # Skills + Abilities Funcs
                                            case "skills.status" | "ss": player.skills_status()
                                            case "learn.abilities" | "la": print("Not Working!\n")

                                            # Different Funcs
                                            case "rest": player.rest()
                                            case "player.status" | "p": player.characteristics_status()
                                            case "use.roll" | "roll":
                                                clear()
                                                if db.get_setting(setting_name="use_roll"):
                                                    Formulas.roll(input("Roll: "))
                                                else:
                                                    print("This feature is disabled in settings.\n")
                                            case "back": break
                                    except ValueError:
                                        clear()
                                        print("Wrong type entered Quantity / Hindrance\n")
                                if not player.live:
                                    clear()
                                    res = input("Resurrect a character? [Y/n]\n")
                                    if res == "Y" or "y":
                                        player.live = True
                                        player.health = int((player.max_health / 100) * 50)
                                        print(f"{player.information['name']} was Resurrect\n")
                            else: print("player not found!\nIt may not have been loaded or created.\n")
                        case "use.roll" | "roll":
                            clear()
                            if db.get_setting(setting_name="use_roll"): Formulas.roll(input("Roll: "))
                            else: print("This feature is disabled in settings.\n")
                        case "exit":
                            clear()
                            app.save() if db.get_setting("auto_save") else None
                            break
                        case _:
                            clear()
                            print(f"Unknown Command: [{request}]\n")
                elif db.get_setting("lang") == "Rus":
                    print("Запущен процесс базовых запросов")
                    print("Для подробного ознакомления с командами прочтите Documentation.md")
                    request = command(input("Запрос: "))
                    match request:
                        case "версия": print(app.version(), "\n")
                        case "редактор": app.redact()
                        case "создание.игрока": app.create_player()
                        case "загрузка" | "load": app.load()
                        case "сохранение": app.save()
                        case "действия":
                            if "player" in globals() and isinstance(player, Player):
                                clear()
                                while True and player.live:
                                    print("Запущен процесс действий персонажа")
                                    print("Для подробного ознакомления с командами прочтите Documentation.md")
                                    action = (command(input("Действие: ")))
                                    try:
                                        match action:
                                            # Action Funcs
                                            case "атака":
                                                player.attack(monster_type=input("Enemy: "))
                                            case "блок":
                                                player.block_attack(
                                                    damage=int(input("Вражеский Урон: ")),
                                                    hindrance=int(input("Сложность Блокирования [0-100]: "))
                                                )
                                            case "уворот":
                                                player.dodge_attack(hindrance=int(input("Сложность Уворота [0-100]: ")))
                                            case "крафт":
                                                player.craft_item(
                                                    item_name=input("Название создаваемого предмета: "),
                                                    item_amount=int(input("Кол-во создаваемого предмета: ")),
                                                    hindrance=int(input("Сложность создания [0-100]: "))
                                                )
                                            case "взлом":
                                                player.hack_item(hindrance=int(input("Сложность взлома [0-100]: ")))
                                            case "кража":
                                                player.steal_item(
                                                    item_name=input("Название предмета: "),
                                                    item_amount=int(input("Кол-во предмета: ")),
                                                    hindrance=int(input("Сложность кражи [0-100]: "))
                                                )
                                            case "проверка":
                                                player.check(hindrance=int(input("Сложность проверки [0-100]: ")))
                                            case "использовать.зелье" | "использовать":
                                                player.use_item(item_name=input("Название расходника: "))

                                            # Inventory + Equipments Funcs
                                            case "добавить.предмет" | "добавить":
                                                player.add_item(
                                                    item_name=input("Добавит предмета: "),
                                                    item_amount=int(input("Кол-во предмета: "))
                                                )
                                            case "купить.предмет" | "купить":
                                                player.buy_item(
                                                    item_name=input("Купить предмета: "),
                                                    item_amount=int(input("Кол-во предмета: "))
                                                )
                                            case "продать.предмет" | "продать":
                                                player.sell_item(
                                                    item_name=input("Продать предмета: "),
                                                    item_amount=int(input("Кол-во предмета: "))
                                                )
                                            case "выкинуть.предмет" | "выкинуть":
                                                player.decrease_item(
                                                    item_name=input("Выкинуть предмета: "),
                                                    item_amount=int(input("Кол-во предмета: "))
                                                )
                                            case "удалить.предмет":
                                                player.del_item(item_name=input("Удалить предмета: "))
                                            case "обнулить.инвентарь": player.reset_inventory()
                                            case "статус.инвентаря" | "i": player.inventory_status()

                                            case "надеть.снаряжение" | "надеть":
                                                player.wear_equipment(
                                                    item_name=input("Надеть снаряжение: "),
                                                    item_amount=int(input("Кол-во предмета: "))
                                                )
                                            case "снять.снаряжение" | "снять":
                                                player.take_of_equipment(
                                                    item_name=input("Снять снаряжение: "),
                                                    item_amount=int(input("Кол-во предмета: "))
                                                )
                                            case "удалить.снаряжение": player.del_equipments(item_name=input("Удалить предмет: "))
                                            case "статус.снаряжения": player.equipment_status()

                                            # Skills + Abilities Funcs
                                            case "статус.навыков" | "навыки": player.skills_status()
                                            case "изучить.способность" | "изучить": print("Not Working!\n")

                                            # Different Funcs
                                            case "отдых": player.rest()
                                            case "статус.игрока" | "игрок": player.characteristics_status()
                                            case "кубик":
                                                clear()
                                                if db.get_setting(setting_name="use_roll"): Formulas.roll(input("Roll: "))
                                                else: print("Эту функция отключена в настройках.\n")
                                            case "back": break
                                    except ValueError:
                                        clear()
                                        print("Введён неправильный тип Количество / Усложнения\n")
                                if not player.live:
                                    clear()
                                    res = input("Resurrect a character? [Y/n]\n")
                                    if res == "Y" or "y":
                                        player.live = True
                                        player.health = int((player.max_health / 100) * 50)
                                        print(f"{player.information['name']} был воскрешён\n")
                            else: print("Игрок не найден!\nВозможно он не загружен или не создан.\n")
                        case "кубик":
                            clear()
                            if db.get_setting(setting_name="use_roll"): Formulas.roll(input("Roll: "))
                            else: print("Эту функция отключена в настройках!.\n")
                        case "exit":
                            clear()
                            app.save() if db.get_setting("auto_save") else None
                            break
                        case _:
                            clear()
                            print(f"Неизвестная команда: [{request}]\n")
                else: print("Wrong Lang!")
        except KeyboardInterrupt:
            clear()
            app.save() if db.get_setting("auto_save") else None
            db.shut_down()


if __name__ == "__main__":
    clear()
    main()
    db.shut_down()
