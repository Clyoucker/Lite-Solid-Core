from Inventory import Inventory
from Equipment import Equipment


class Storage(Inventory, Equipment):
    def __init__(self):
        Inventory.__init__(self)
        Equipment.__init__(self)

    def add_item(self, item_name: str, item_amount: int, capacity: int = 0):
        capacity = 0 if self._equipment_bonus["capacity"] == 0 else self._equipment_bonus["capacity"]
        Inventory.add_item(self,item_name=item_name,item_amount=item_amount,capacity=capacity)

    def take_of_equipment(self, item_name, item_amount):
        if item_name in self._equipments:
            self.add_item(item_name,item_amount)
            self.del_equipments(item_name)
        else:
            print(f"Equipment: [{item_name}]")

    def inventory_status(self,capacity: int = 0):
        capacity = 0 if self._equipment_bonus["capacity"] == 0 else self._equipment_bonus["capacity"]
        Inventory.inventory_status(self,capacity=capacity)

    def wear_equipment(self, item_name: str, item_amount: int):
        res = Equipment.wear_equipment(self,item_name=item_name,item_amount=item_amount)
        if res["res"]:
            self.decrease_item(item_name=res["item_name"],item_amount=res["amount"])
