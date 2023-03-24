from Error import FoundError
from tabulate import tabulate
from FileWorker import db
import os
clear = lambda: os.system('cls')


class Inventory:
    def __init__(self):
        self.__max_inventory_weight = db.get_setting(setting_name="max_inventory_weight")
        self._current_inventory_weight = 0
        self._inventory_price = 0
        self._inventory = dict()

    def add_item(self, item_name: str, item_amount: int, capacity: int = 0):
        clear()
        try:
            db_item = db.get_object(obj_name=item_name, category="objects")
            if item_amount >= 1:
                temp_weight = round(self._current_inventory_weight + item_amount * db_item["attributes"]["weight"],2)
                if temp_weight <= self.__max_inventory_weight + capacity:
                    # Обновляет уже существующий объект // Updating already exist obj
                    if db_item["title"] in self._inventory:
                        amount = self._inventory[db_item["title"]]["amount"] + item_amount
                        weight = round((self._inventory[db_item["title"]]["amount"] + item_amount) * db_item["attributes"]["weight"],2)
                        cost = db_item["attributes"]["cost"] * item_amount + self._inventory[db_item["title"]]["cost"]
                        self._inventory[db_item["title"]].update(amount=amount, weight=weight, cost=cost)
                        print(f"Update: {db_item['title']}")
                    # Добавляет новый объект // Adding new Obj
                    else:
                        weight = round(db_item["attributes"]["weight"] * item_amount, 2)
                        cost = db_item["attributes"]["cost"] * item_amount
                        self._inventory[db_item["title"]] = {"amount": item_amount, "weight": weight, "cost": cost}
                        print(f"New: {db_item['title']}")
                    # Обновляет стоимость инвентаря // Updating inventory price
                    self._current_inventory_weight = temp_weight
                    self._inventory_price += db_item["attributes"]["cost"] * item_amount
                else:
                    print(f"Attempt to exceed the inventory limit! \n You need free weight [{temp_weight - self.__max_inventory_weight}]")
            else:
                print("Quantity cannot be negative")
        except FoundError:
            print(f"Not Found Item: [{item_name}]")

    def decrease_item(self,item_name:str, item_amount: int):
        clear()
        try:
            temp_weight = self._current_inventory_weight
            temp_price = self._inventory_price
            db_item = db.get_object(obj_name=item_name, category="objects")
            if 1 <= item_amount <= self._inventory[db_item["title"]]["amount"]:
                # Обновляет уже существующий объект // Updating already exist obj
                if db_item["title"] in self._inventory:
                    weight = round(self._inventory[db_item["title"]]["amount"] * db_item["attributes"]["weight"] - db_item["attributes"]["weight"] * item_amount,2)
                    cost = self._inventory[db_item["title"]]["cost"] - db_item["attributes"]["cost"] * item_amount
                    amount = self._inventory[db_item["title"]]["amount"] - item_amount
                    if amount == 0:
                        self.del_item(item_name=item_name)
                    else:
                        self._inventory[db_item["title"]].update(amount=amount, weight=weight, cost=cost)
                        print(f"Update: {db_item['title']}")
                    self._current_inventory_weight = temp_weight - db_item["attributes"]["weight"] * item_amount
                    self._inventory_price = temp_price - db_item["attributes"]["cost"] * item_amount
                else:
                    print("There is no such item in the subsequent inventory!")
            else:
                print("You don't have enough item to remove it.")
        except FoundError:
            print(f"Not Found Item: [{item_name}]")

    def del_item(self, item_name: str):
        clear()
        if item_name in self._inventory:
            item_attributes = self._inventory.__getitem__(item_name)
            self._inventory_price -= item_attributes["cost"]
            self._current_inventory_weight -= item_attributes["weight"]
            del self._inventory[item_name]
            print(f"Del: {item_name}")
        else:
            print("There is no such item in the subsequent inventory!")

    def reset_inventory(self):
        clear()
        self._inventory = dict()
        self._inventory_price = 0
        self._current_inventory_weight = 0
        print("Reset Inventory Completed!")

    def inventory_status(self,capacity: int = 0):
        clear()
        items = list()
        for item in self._inventory:
            items.append({"title":item,"weight":self._inventory[item]["weight"],"amount":self._inventory[item]["amount"],"cost":self._inventory[item]["cost"]})
        print(tabulate(items, headers="keys"),"\n") if len(items) > 0 else None
        print(f"Max Inventory Weight: {self.__max_inventory_weight + capacity} | Current Inventory Weight: {self._current_inventory_weight} | Inventory Cost: {self._inventory_price}\n")
