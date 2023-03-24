from Error import FoundError
from tabulate import tabulate
from FileWorker import db
import os
clear = lambda: os.system('cls')


class Equipment:
    def __init__(self):
        self.__max_equipment_weight = db.get_setting(setting_name="max_equipment_weight")
        self.__max_eqip = db.get_setting(setting_name="max_eqip")
        self._current_equipment_weight = 0
        self._current_eqip = 0
        self._equipments = dict()
        self._equipment_price = 0
        self._equipment_bonus = {"protect": 0, "damage": 0, "capacity": 0}
        self._equipment_bonus_temp = {"protect": 0, "damage": 0, "capacity": 0}

    def __equipment_bonus_update(self):
        clear()
        if len(self._equipments) > 0:
            for key,value in self._equipments.items():
                attributes = db.get_object(obj_name=key,category="objects")["attributes"]

                for bonus in [item for item in self._equipment_bonus.keys()]:
                    if bonus in attributes:
                        self._equipment_bonus[bonus] = attributes[bonus] * value["amount"] if self._equipment_bonus_temp[bonus] != attributes[bonus] * value["amount"] else self._equipment_bonus[bonus]

                for bonus in [item for item in self._equipment_bonus_temp.keys()]:
                    if bonus in attributes:
                        self._equipment_bonus_temp[bonus] = self._equipment_bonus_temp[bonus] + attributes[bonus] * value["amount"] if self._equipment_bonus[bonus] != attributes[bonus] * value["amount"] else self._equipment_bonus_temp[bonus]

    def wear_equipment(self, item_name: str, item_amount: int):
        clear()
        try:
            db_item = db.get_object(obj_name=item_name, category="objects")
            if db_item["title"] in db._wears:
                if item_amount >= 1:
                    temp_weight = round(self._current_equipment_weight + item_amount * db_item["attributes"]["weight"],2)
                    equip = self._current_eqip + item_amount
                    price = self._equipment_price + db_item["attributes"]["cost"] * item_amount
                    if temp_weight <= self.__max_equipment_weight:
                        if equip <= self.__max_eqip:
                            # Обновляет уже существующий объект // Updating already exist obj
                            if db_item["title"] in self._equipments:
                                amount = self._equipments[db_item["title"]]["amount"] + item_amount
                                weight = round(amount * db_item["attributes"]["weight"], 2)
                                cost = db_item["attributes"]["cost"] * item_amount + self._equipments[db_item["title"]]["cost"]
                                self._equipments[db_item["title"]].update(amount=amount, weight=weight, cost=cost)
                                print(f"Update:{db_item['title']}")
                            # Добавляет новый объект // Adding new Obj
                            else:
                                weight = round(db_item["attributes"]["weight"] * item_amount, 2)
                                cost = db_item["attributes"]["cost"] * item_amount
                                self._equipments[db_item["title"]] = {"amount": item_amount, "weight": weight, "cost": cost}
                                print(f"{db_item['title']}: Was Wearing")
                            # Обновляет стоимость инвентаря, текущий вес и занятые ячейки снаряжения // Updates the cost of inventory, the weight of the capture of the equipment compartment
                            self._equipment_price = price
                            self._current_eqip = equip
                            self._current_equipment_weight = temp_weight
                            # Обновляет бонусные снаряжения // Updates bonus equipment
                            self.__equipment_bonus_update()
                            # Возвращает True для инвентаря, чтобы он убрал оттуда предмет, который будет одет. // Returns True for the inventory to remove the removed item to be equipped
                            return {"res":True,"item_name":db_item["title"],"amount":item_amount}
                        else:
                            print("Exceeding the limit of active equipments")
                    else:
                        print(f"Attempt to exceed the equipments limit! \n You need free weight [{temp_weight - self.__max_equipment_weight}]")
                else:
                    print("Quantity cannot be negative")
            else:
                print(f"This object is not considered a thing: [{item_name}]")
        except FoundError:
            print(f"Not Found Item: [{item_name}]")

    def del_equipments(self, item_name: str):
        clear()
        if item_name in self._equipments:
            db_item_attributes = db.get_object(obj_name=item_name,category="objects")["attributes"]
            item_attributes = self._equipments.__getitem__(item_name)
            self._current_eqip -= item_attributes["amount"]
            self._equipment_price -= item_attributes["cost"]
            self._current_equipment_weight -= item_attributes["weight"]
            for bonus in [item for item in self._equipment_bonus.keys()]:
                if bonus in db_item_attributes:
                    self._equipment_bonus[bonus] = self._equipment_bonus[bonus] - db_item_attributes[bonus] * item_attributes["amount"]
            del self._equipments[item_name]
        else:
            print("There is no such item in the subsequent inventory!")

    def equipment_status(self):
        clear()
        equipments = list()
        for item in self._equipments:
            equipments.append({"title":item,"weight":self._equipments[item]["weight"],"amount":self._equipments[item]["amount"],"cost":self._equipments[item]["cost"]})
        print(tabulate(equipments, headers="keys"),"\n") if len(equipments) > 0 else None
        print(f"Protect Bonus: {self._equipment_bonus['protect']} | Damage Bonus: {self._equipment_bonus['damage']} | Capacity Bonus: {self._equipment_bonus['capacity']}")
        print(f"Max Eqip Weight: {self.__max_equipment_weight} | Current Eqip Weight: {self._current_equipment_weight}\nMax Eqip: {self.__max_eqip} | Current Eqip: {self._current_eqip}\nEqip Cost: {self._equipment_price}\n")
