from FileWorker import db
from Formulas import chance_calculation


class Enemy:
    def __init__(self,race: str, health: int, mana: int, protection: int, damage: int, skills: dict, abilities: dict, exp:int = 15):
        self._race = race
        self._max_health = health
        self._max_mana = mana
        self._health = health
        self._mana = mana
        self._protection = protection
        self._damage = damage
        self._skills = skills
        self._abilities = abilities
        self.__exp = exp
        self.life = True

    def attack(self,enemy=None):
        print(f"{self._race} Attack => {enemy}")
        return self._damage

    def defense(self,damage,hindrance=0):
        print(f"{self._race} Use Block")
        skill_bonus = db.get_object(obj_name="power", category="base", types="skills")["attributes"]["block_chance"]
        skill_lvl = 1 if "power" not in self._skills else self._skills["power"]
        match chance_calculation(skill_lvl=skill_lvl, skill_chance=1, skill_bonus=skill_bonus,hindrance=hindrance):
            case True: self._health += - damage + int((self._health * 1.5)) if damage >= int((self._health * 1.5)) else 0
            case _: self._health += - damage + int((self._protection / 1.5)) if damage >= int((self._protection * 1.5)) else 0
        self.life = False if self._health <= 0 else True
        print(f"[{self._race}] | Health: {self._health}/{self._max_health}") if self.life else print(f"{self._race} | Health: {self._health}/{self._max_health} is Dead!")

    def resurrect(self):
        self._health = self._max_health
        self.life = True

    def use_abilities(self,abilities_name):
        pass

    def status(self):
        skills = ""
        for key,value in self._skills.items():
            skills += f"{key}: {value} LvL | "
        skills = skills[:len(skills)-2]
        print(f"Enemy Race: {self._race}")
        print(f"Heath: {self._health} / {self._max_health} | Mana: {self._mana}  / {self._max_mana} | Protection: {self._protection} | Damage: {self._damage}")
        print(f"Skills: {skills}")

    def get_race(self): return self._race

    def get_exp(self): return self.__exp if db.get_setting(setting_name="use_sys_rpg") else 0


class Slime(Enemy):
    """Слизь"""
    def __init__(self,race,life,mana,protection,damage,skills,abilities,exp):
        Enemy.__init__(self,race,life,mana,protection,damage,skills,abilities,exp)


class Ogr(Enemy):
    """Огр"""
    def __init__(self,race,life,mana,protection,damage,skills,abilities,exp):
        Enemy.__init__(self,race,life,mana,protection,damage,skills,abilities,exp)


class Dragon(Enemy):
    """Дракон"""
    def __init__(self,race,life,mana,protection,damage,skills,abilities,exp):
        Enemy.__init__(self,race,life,mana,protection,damage,skills,abilities,exp)


class Hound(Enemy):
    """Гончая"""
    def __init__(self,race,life,mana,protection,damage,skills,abilities,exp):
        Enemy.__init__(self,race,life,mana,protection,damage,skills,abilities,exp)


class Plague(Enemy):
    """Чумная / Чума"""
    def __init__(self,race,life,mana,protection,damage,skills,abilities,exp):
        Enemy.__init__(self,race,life,mana,protection,damage,skills,abilities,exp)


class Demon(Enemy):
    """Демон"""
    def __init__(self,race,life,mana,protection,damage,skills,abilities,exp):
        Enemy.__init__(self,race,life,mana,protection,damage,skills,abilities,exp)


class Bandit(Enemy):
    """Бандит"""
    def __init__(self,race,life,mana,protection,damage,skills,abilities,exp):
        Enemy.__init__(self,race,life,mana,protection,damage,skills,abilities,exp)


slime = Slime("slime",86,42,4,8,{"absorption":5,"body":4,"dexterity":4,"power":3,"accuracy":3,"secrecy":3,"mastery":2,"adaptation":2,"wisdom":2,},dict(),exp=600)
ogr = Ogr("ogr",264,163,26,42,{"power":5,"body":4,"mastery":4,"adaptation":3,"strong stomach":3,"volition":3,"psyche":2,"wisdom":2,"dexterity":2,},dict(),exp=32)
dragon = Dragon("dragon",640,464,42,86,{"power":5,"body":4,"mastery":4,"adaptation":3,"dexterity":3,"absorption":3,"occultism":2,"justice":2,"volition":2,},dict(),exp=164)
hound = Hound("hound",200,80,16,35,{"accuracy":5,"dexterity":4,"strong stomach":4,"psyche":3,"volition":3,"absorption":3,"body":2,"power":2,"adaptation":2,},dict(),exp=56)
plague = Plague("plague",364,215,12,35,{"psyche":5,"strong stomach":4,"mastery":4,"absorption":3,"":3,"theft":3,"carefully":2,"accuracy":2,"adaptation":2,},dict(),exp=96)
demon = Demon("demon",200,164,29,56,{"scouting":5,"blessing":4,"volition":4,"deception":3,"resources":3,"mastery":3,"sociability":2,"absorption":2,"manipulation":2,},dict(),exp=86)
bandit = Bandit("bandit",163,163,26,42,{"hack":5,"body":4,"power":4,"theft":3,"trade":3,"sociability":3,"manipulation":2,"resources":2,"dexterity":2,},dict(),exp=42)
