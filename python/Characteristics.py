from FileWorker import db


class Characteristics:
    def __init__(self, health: int, mana: int, stamina: int, protection: int, damage: int):
        self.__max_health = health
        self.__max_mana = mana
        self.__max_stamina = stamina
        self.__max_protection = protection
        self.__max_damage = damage
        self.__current_health = health
        self.__current_mana = mana
        self.__current_stamina = stamina
        self.__current_protection = protection
        self.__current_damage = damage

    def set_health(self,health): self.__current_health = health
    def get_health(self): return self.__current_health
    def set_max_health(self,new_max_health): self.__max_health = new_max_health
    def get_max_health(self): return self.__max_health

    def set_mana(self,mana): self.__current_mana = mana
    def get_mana(self): return self.__current_mana
    def set_max_mana(self,new_max_mana): self.__max_mana = new_max_mana
    def get_max_mana(self): return self.__max_mana

    def set_stamina(self,stamina): self.__current_stamina = stamina
    def get_stamina(self): return self.__current_stamina
    def set_max_stamina(self,new_max_stamina): self.__max_stamina = new_max_stamina
    def get_max_stamina(self): return self.__max_stamina

    def set_protection(self,protection): self.__current_protection = protection
    def get_protection(self): return self.__current_protection
    def set_max_protection(self,new_max_protection): self.__max_stamina = new_max_protection
    def get_max_protection(self): return self.__max_protection

    def set_damage(self,damage): self.__current_damage = damage
    def get_damage(self): return self.__current_damage
    def set_max_damage(self,new_max_damage): self.__max_damage = new_max_damage
    def get_max_damage(self): return self.__max_damage

    def characteristics_status(self,prot: int = 0, dmg: int = 0):
        health = f"Health: {self.__current_health}/{self.__max_health}"
        mana = f"Mana: {self.__current_mana}/{self.__max_mana}"
        stamina = f"Stamina: {self.__current_stamina}/{self.__max_stamina}"
        protection = f"Protection: {self.__current_protection + prot}"
        damage = f"Damage: {self.__current_damage + dmg}"
        print(f"\n{health} | {mana} | {stamina} | {protection} | {damage}")

    def characteristic_recovery(self,percent: int = 15):
        hp_regen = int((self.max_health / 100) * percent)
        mp_regen = int((self.max_mana / 100) * percent)
        st_regen = int((self.max_stamina / 100) * percent)
        self.health = self.health + hp_regen if self.health + hp_regen <= self.max_health else self.max_health
        self.mana = self.mana + mp_regen if self.mana + mp_regen <= self.max_mana else self.max_mana
        self.stamina = self.stamina + st_regen if self.stamina + st_regen <= self.max_stamina else self.max_stamina
        if 15 <= percent <= 25:
            print("The snoring of your comrades did not let you sleep properly\n")
        elif 26 <= percent <= 50:
            print("You didn't sleep well\n")
        else:
            self.health = self.max_health
            self.mana = self.max_mana
            self.stamina = self.max_stamina
            print("You had a great rest\n")

    health = property(get_health,set_health)
    max_health = property(get_max_health,set_max_health)

    mana = property(get_mana,set_mana)
    max_mana = property(get_max_mana,set_max_mana)

    stamina = property(get_stamina,set_stamina)
    max_stamina = property(get_max_stamina,set_max_stamina)

    protection = property(get_protection,set_protection)
    max_protection = property(get_max_protection,set_max_protection)

    damage = property(get_damage,set_damage)
    max_damage = property(get_max_damage,set_max_damage)
