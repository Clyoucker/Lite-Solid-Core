import random
from Error import FoundError
from Storage import Storage
from Capability import Capability
from Formulas import sell,buy
from random import randint,choice
from Enemy import *
import os
clear = lambda: os.system('cls')


class Player(Storage,Capability):
    def __init__(self,information:dict, characteristics: dict, skills: dict):
        Capability.__init__(self,health=characteristics["health"],mana=characteristics["mana"],stamina=characteristics["stamina"],protection=characteristics["protection"],damage=characteristics["damage"],skills=skills)
        Storage.__init__(self)
        self.information = information
        self.level = 1
        self._level_up_exp = 0
        self._level_up_need_exp = db.get_setting(setting_name="level_up_need_xp")
        self.live = True
        self.__attack_use = False

    def __level_up(self):
        clear()
        if self.level != db.get_setting(setting_name="max_levels"):
            char_up = db.get_setting(setting_name="level_up")
            self.level += 1
            self._level_up_exp = 0
            self._level_up_need_exp += (self._level_up_need_exp / 100) * int(db.get_setting(setting_name="factor_level_up_exp").split("%")[0])
            self.max_health += char_up["health"]
            self.max_mana += char_up["mana"]
            self.max_stamina += char_up["stamina"]
            self.max_protection += char_up["protection"]
            self.max_damage += char_up["damage"]
            self.health = self.max_health
            self.mana = self.max_mana
            self.max_stamina = self.max_stamina
            self.damage = self.max_damage
            self.protection = self.max_protection
            self.characteristics_status()

    def set_exp(self,exp: int):
        clear()
        self._level_up_exp += exp
        self.__level_up() if self._level_up_exp >= self._level_up_need_exp else None

    def attack(self,monster_type: str):
        clear()
        damage = 0
        match monster_type:
            case "slime":
                damage = slime.attack(enemy="Player") if self.__attack_use else 0
                slime.defense(damage=self.damage + self._equipment_bonus["damage"], hindrance=25) if not self.__attack_use else None
                self._level_up_exp += slime.get_exp() if not slime.life else 0
                slime.resurrect() if not slime.life else None
            case "dragon":
                damage = dragon.attack(enemy="Player") if self.__attack_use else 0
                dragon.defense(damage=self.damage + self._equipment_bonus["damage"], hindrance=5) if not self.__attack_use else None
                self._level_up_exp += dragon.get_exp() if not dragon.life else 0
                dragon.resurrect() if not dragon.life else None
            case "ogr":
                damage = ogr.attack(enemy="Player") if self.__attack_use else 0
                ogr.defense(damage=self.damage + self._equipment_bonus["damage"], hindrance=10) if not self.__attack_use else None
                self._level_up_exp += ogr.get_exp() if not ogr.life else 0
                ogr.resurrect() if not ogr.life else None
            case "hound":
                damage = hound.attack(enemy="Player") if self.__attack_use else 0
                hound.defense(damage=self.damage + self._equipment_bonus["damage"], hindrance=15) if not self.__attack_use else None
                self._level_up_exp += hound.get_exp() if not hound.life else 0
                hound.resurrect() if not hound.life else None
            case "plague":
                damage = plague.attack(enemy="Player") if self.__attack_use else 0
                hound.defense(damage=self.damage + self._equipment_bonus["damage"], hindrance=15) if not self.__attack_use else None
                self._level_up_exp += plague.get_exp() if not plague.life else 0
                plague.resurrect() if not plague.life else None
            case "demon":
                damage = demon.attack(enemy="Player") if self.__attack_use else 0
                hound.defense(damage=self.damage + self._equipment_bonus["damage"], hindrance=15) if not self.__attack_use else None
                self._level_up_exp += demon.get_exp() if not demon.life else 0
                demon.resurrect() if not demon.life else None
            case "bandit":
                damage = bandit.attack(enemy="Player") if self.__attack_use else 0
                hound.defense(damage=self.damage + self._equipment_bonus["damage"], hindrance=15) if not self.__attack_use else None
                self._level_up_exp += bandit.get_exp() if not bandit.life else 0
                bandit.resurrect() if not bandit.life else None
            case _: pass
        self.__attack_use = not self.__attack_use
        if damage > 0:
            print("The enemy is attacking!")
            while True:
                cmd = input("Use Block [b] / Dodge [d]: ")
                if cmd == "b" or "B":
                    self.block_attack(damage=damage,hindrance=0)
                    break
                elif cmd == "d" or "D":
                    self.dodge_attack(hindrance=0)
                    break
        self.__level_up() if self._level_up_exp >= self._level_up_need_exp else None
        self.live = False if self.health <= 0 else True
        print(f"[{self.information['name']}] | Health: {self.health}/{self.max_health}\n") if self.live else print(f"{self.information['name']} | Health: {self.health}/{self.max_health} is Dead!\n")

    def use_abilities(self,abilities: str, monster_type: str = None):
        pass

    def use_item(self,item_name: str):
        clear()
        try:
            db_item = db.get_object(obj_name=item_name)
            if db_item["title"] in db.potions and db_item["title"] in self._inventory:
                if db_item["title"].startswith("health"):
                    heal = self.health + db_item["attributes"]["health"]
                    self.health = heal if heal <= self.max_health else self.max_health
                    self.decrease_item(item_name=db_item["title"],item_amount=1)
                elif db_item["title"].startswith("mana"):
                    mana = self.health + db_item["attributes"]["mana"]
                    self.mana = mana if mana <= self.max_mana else self.max_mana
                    self.decrease_item(item_name=db_item["title"],item_amount=1)
                elif db_item["title"].startswith("stamina"):
                    stamina = self.stamina + db_item["attributes"]["stamina"]
                    self.stamina = stamina if stamina <= self.max_stamina else self.max_stamina
                    self.decrease_item(item_name=db_item["title"],item_amount=1)
                elif db_item["title"].startswith("poison"):
                    heal = self.health + db_item["attributes"]["poison"]
                    self.health = heal if 1 <= heal <= self.health else 0
                    self.decrease_item(item_name=db_item["title"],item_amount=1)
                    if self.health == 0:
                        self.live = False
                        print("Death by poison\n")
                else:
                    print(f"It's impossible to use!: [{db_item['title']}]\n")
        except FoundError:
            print(f"Not Found Item: [{item_name}]\n")

    def sell_item(self, item_name: str, item_amount: int):
        clear()
        try:
            db_item = db.get_object(obj_name=item_name)
            if db_item["title"] in self._inventory:
                if 1 <= item_amount <= self._inventory[db_item["title"]]["amount"]:
                    skill_chance = db.get_object(obj_name="trade", category="base", types="skills")["attributes"]["chance"]
                    skill_bonus = db.get_object(obj_name="trade", category="base", types="skills")["attributes"]["bonus"]
                    skill_revenue_percentage = db.get_object(obj_name="trade", category="base", types="skills")["attributes"]["selling"]
                    skill_lvl = 1 if "trade" not in self._current_skills else self._current_skills["trade"]
                    money = sell(cost=db_item["attributes"]["cost"],amount=item_amount,skill_lvl=skill_lvl,skill_chance=skill_chance,skill_bonus=skill_bonus,skill_revenue_percentage=skill_revenue_percentage)
                    self.decrease_item(item_name=db_item["title"],item_amount=item_amount)
                    self.add_item(item_name="money",item_amount=money)
                else:
                    print("Quantity cannot be negative\n")
            else:
                print("There is no such item in the subsequent inventory!\n")
        except FoundError:
            print(f"Not Found Item: [{item_name}]\n")

    def buy_item(self,item_name: str, item_amount: int):
        clear()
        try:
            db_item = db.get_object(obj_name=item_name)
            skill_chance = db.get_object(obj_name="trade", category="base", types="skills")["attributes"]["chance"]
            skill_bonus = db.get_object(obj_name="trade", category="base", types="skills")["attributes"]["bonus"]
            skill_revenue_discounts = db.get_object(obj_name="trade", category="base", types="skills")["attributes"]["purchase"]
            skill_lvl = 1 if "trade" not in self._current_skills else self._current_skills["trade"]
            if "money" in self._inventory:
                money = buy(cost=db_item["attributes"]["cost"],money=self._inventory["money"]["amount"],skill_lvl=skill_lvl,skill_chance=skill_chance,skill_bonus=skill_bonus,amount=item_amount,skill_revenue_discounts=skill_revenue_discounts)
                if money >= 0:
                    self.decrease_item(item_name="money", item_amount=self._inventory["money"]["amount"]) if money != 0 else self.del_item(item_name="money")
                    self.add_item(item_name=db_item["title"],item_amount=item_amount)
                else:
                    print(self._inventory['money'])
                    print(f"Not enough money! \n You need money: [{db_item['attributes']['cost'] - self._inventory['money']['amount']}]\n")
            else:
                print("You don't have money!\n")
        except FoundError:
            print(f"Not Found Item: [{item_name}]\n")

    def steal_item(self,item_name: str, item_amount: int, hindrance: int = 0):
        clear()
        try:
            db_item = db.get_object(obj_name=item_name)
            if item_amount >= 1:
                skill_chance = db.get_object(obj_name="theft", category="base", types="skills")["attributes"]["chance"]
                skill_bonus = db.get_object(obj_name="theft", category="base", types="skills")["attributes"]["bonus"]
                skill_lvl = 1 if "theft" not in self._current_skills else self._current_skills["theft"]
                self.add_item(item_name=db_item["title"], item_amount=item_amount) if chance_calculation(skill_lvl=skill_lvl,skill_chance=skill_chance,skill_bonus=skill_bonus,hindrance=hindrance) else print("Failed\n")
            else:
                print("Quantity cannot be negative\n")
        except FoundError:
            print(f"Not Found Item: [{item_name}]\n")

    def hack_item(self,hindrance: int = 0):
        clear()
        skill_chance = db.get_object(obj_name="wisdom", category="base", types="skills")["attributes"]["chance"]
        skill_bonus = db.get_object(obj_name="wisdom", category="base", types="skills")["attributes"]["bonus"]
        skill_levels = {"wisdom":1 if "wisdom" not in self._current_skills else self._current_skills["wisdom"],"adaptation":1 if "adaptation" not in self._current_skills else self._current_skills["adaptation"]}
        skill_lvl = skill_levels["wisdom"] + 1 if skill_levels["wisdom"] > 1 and skill_levels["adaptation"] > 1 else skill_levels["wisdom"]
        print("Hack Success!\n") if chance_calculation(skill_lvl=skill_lvl,skill_chance=skill_chance,skill_bonus=skill_bonus,hindrance=hindrance) else print("Failed\n")

    def proof_person(self,hindrance: int = 0):
        clear()
        skill_chance = db.get_object(obj_name="sociability", category="base", types="skills")["attributes"]["chance"]
        skill_bonus = db.get_object(obj_name="sociability", category="base", types="skills")["attributes"]["bonus"]
        skill_levels = {"sociability":1 if "sociability" not in self._current_skills else self._current_skills["sociability"]}
        skill_lvl = 1 if "sociability" not in self._current_skills else self._current_skills["sociability"]
        print("Proof Success!\n") if chance_calculation(skill_lvl=skill_lvl,skill_chance=skill_chance,skill_bonus=skill_bonus,hindrance=hindrance) else print("Failed\n")

    def check(self,hindrance: int = 0):
        clear()
        skill_chance = db.get_object(obj_name="carefully", category="base", types="skills")["attributes"]["chance"]
        skill_bonus = db.get_object(obj_name="carefully", category="base", types="skills")["attributes"]["bonus"]
        skill_lvl = 1 if "carefully" not in self._current_skills else self._current_skills["carefully"]
        if chance_calculation(skill_lvl=skill_lvl, skill_chance=skill_chance, skill_bonus=skill_bonus,hindrance=hindrance):
            print("You suspect something\n")
        else:
            print("You failed to understand anything\n")

    def dodge_attack(self,hindrance: int = 0):
        clear()
        skill_chance = db.get_object(obj_name="dexterity", category="base", types="skills")["attributes"]["chance"]
        skill_bonus = db.get_object(obj_name="dexterity", category="base", types="skills")["attributes"]["bonus"]
        skill_lvl = 1 if "dexterity" not in self._current_skills else self._current_skills["dexterity"]
        if chance_calculation(skill_lvl=skill_lvl,skill_chance=skill_chance,skill_bonus=skill_bonus,hindrance=hindrance):
            print("You avoided damage\n")
        else:
            damage = int(input("Enemy Damage: "))
            self.health += - damage + ((self.protection + self._equipment_bonus["protect"]) / 2) if damage >= ((self.protection + self._equipment_bonus["protect"]) / 2) else 0
            if self.health <= 0:
                self.live = False
                print("You are Dead!\n")
        print(f"Health: {self.health}/{self.max_health}\n")

    def block_attack(self,damage:int, hindrance: int = 0):
        clear()
        skill_chance = 1
        skill_bonus = db.get_object(obj_name="power", category="base", types="skills")["attributes"]["block_chance"]
        skill_lvl = 1 if "power" not in self._current_skills else self._current_skills["power"]
        if chance_calculation(skill_lvl=skill_lvl, skill_chance=skill_chance, skill_bonus=skill_bonus,hindrance=hindrance):
            self.health -= damage + int(((self.protection + self._equipment_bonus["protect"]) * 1.5)) if damage >= int(((self.protection + self._equipment_bonus["protect"]) * 1.5)) else 0
        else:
            self.health -= damage + int(((self.protection + self._equipment_bonus["protect"]) / 1.5)) if damage >= int(((self.protection + self._equipment_bonus["protect"]) * 1.5)) else 0
        if self.health <= 0:
            self.live = False
            print("You are Dead!\n")
        print(f"Health: {self.health}/{self.max_health}\n")

    def craft_item(self,item_name: str, item_amount: int, hindrance: int = 0):
        clear()
        try:
            db_item = db.get_object(obj_name=item_name,item_amount=item_amount)
            skill_chance = db.get_object(obj_name="ingenuity", category="base", types="skills")["attributes"]["chance"]
            skill_bonus = db.get_object(obj_name="ingenuity", category="base", types="skills")["attributes"]["bonus"]
            skill_levels = {"wisdom":1 if "wisdom" not in self._current_skills else self._current_skills["wisdom"],"ingenuity":1 if "ingenuity" not in self._current_skills else self._current_skills["ingenuity"]}
            skill_lvl = skill_levels["ingenuity"] + 1 if skill_levels["ingenuity"] > 1 and skill_levels["wisdom"] > 1 else skill_levels["ingenuity"]
            if chance_calculation(skill_lvl=skill_lvl,skill_chance=skill_chance,skill_bonus=skill_bonus,hindrance=hindrance):
                print("Crafting Success!\n")
                self.add_item(item_name=db_item["title"],item_amount=item_amount)
            else:
                print("Crafting Failed!\n")
                self.add_item(item_name=choice(["scrap","wood","fragments"]), item_amount=randint(1,8))
        except FoundError:
            print(f"Not Found Item: [{item_name}]\n")

    def learn_abilities(self,abilities_name: str, hindrance: int = 0):
        clear()
        try:
            db_abilities = db.get_object(obj_name=abilities_name,category="base",types="abilities")
            chance_bonus = 25 if self.information["class"] == "nobody" else 5 if self.information["class"] == "mage" else 0
            skill_chance = db.get_object(obj_name="wisdom", category="base", types="skills")["attributes"]["chance"] + chance_bonus
            skill_bonus = db.get_object(obj_name="wisdom", category="base", types="skills")["attributes"]["bonus"]
            skill_lvl = 1 if "wisdom" not in self._current_skills else self._current_skills["wisdom"]
            if chance_calculation(skill_lvl=skill_lvl, skill_chance=skill_chance, skill_bonus=skill_bonus,hindrance=hindrance):
                self.add_abilities(abilities_name=db_abilities["title"])
            else:
                print(f"Research failure {db_abilities['title']}\n")
        except FoundError:
            print(f"Not Found Item: [{abilities_name}]\n")

    def characteristics_status(self,prot:int = 0, dmg: int = 0):
        prot = 0 if self._equipment_bonus["protect"] == 0 else self._equipment_bonus["protect"]
        dmg = 0 if self._equipment_bonus["damage"] == 0 else self._equipment_bonus["damage"]
        clear()
        Capability.characteristics_status(self,prot=prot,dmg=dmg)
        print(f"Current Player Exp: [{self._level_up_exp}/{self._level_up_need_exp}] | Player Level: [{self.level}]") if db.get_setting(setting_name="use_sys_rpg") else None
        print()

    def rest(self):
        clear()
        self.characteristic_recovery(random.randrange(15,101))
        self.characteristics_status()
        print()
