from random import *
from FileWorker import db


def form(stat: str, minimal: int, prof: str = None, spec: str = None, race: str = None, clas: str = None, body: int = None, wisdom: int = None, dexterity: int = None, master: int = None, power: int = None):
    # minimal - минимальное значение характеристик: Здоровья, Маны, Выносливости, Брони или Урона
    prof_bonus = db.get_object(obj_name=prof,category="base",types="profs")["attributes"]["bonus"] if prof is not None else 1
    spec_bonus = db.get_object(obj_name=spec, category="base", types="specs")["attributes"]["bonus"] if spec is not None else 1
    race_bonus = db.get_object(obj_name=race, category="base", types="races")["attributes"]["bonus"] if race is not None else 1
    class_bonus = db.get_object(obj_name=clas, category="base", types="class")["attributes"]["bonus"] if clas is not None else 1
    match stat:
        case "hp": return minimal + (body * ((prof_bonus * spec_bonus) + (race_bonus * class_bonus)))
        case "mp": return minimal + (wisdom * ((prof_bonus * spec_bonus) + (race_bonus * class_bonus)))
        case "sm": return minimal + (dexterity * ((prof_bonus * spec_bonus) + (race_bonus * class_bonus)))
        case "df": return minimal + (body * class_bonus)
        case "dmg": return minimal + (master * power * wisdom)
        case _: raise KeyError(f"{stat} unknown")


def sell(cost: int, amount: int, skill_lvl: int, skill_chance: int, skill_bonus: int, skill_revenue_percentage: int):
    current_chance = chance_calculation(skill_lvl=skill_lvl,skill_chance=skill_chance,skill_bonus=skill_bonus,hindrance=0)
    skill_revenue_percentage = skill_revenue_percentage if current_chance else 0
    return round((cost + (cost * ((skill_lvl * skill_revenue_percentage)/100) * amount)) - ((cost / 100) * 16))


def buy(cost: int, money: int, amount: int, skill_lvl: int, skill_chance: int, skill_bonus: int, skill_revenue_discounts: int):
    current_chance = chance_calculation(skill_lvl=skill_lvl,skill_chance=skill_chance,skill_bonus=skill_bonus,hindrance=0)
    skill_revenue_discounts = skill_revenue_discounts if current_chance else 0
    return round(money - (cost * amount - (((cost / 100) * (skill_lvl * skill_revenue_discounts)) * amount)))


def chance_calculation(skill_lvl: int, skill_chance: int, skill_bonus: int, hindrance:int = 0):
    current_chance = skill_chance + (skill_lvl * skill_bonus) if skill_lvl > 1 else skill_chance
    return True if int(current_chance - hindrance) >= randrange(101) else False


def calc_hp(body: int, prof: str, spec: str, race: str, clas: str):
    min_hp = db.get_object(obj_name="health",category="base",types="characteristics")["attributes"]["min"]
    match clas:
        case "mage": hp = int(form("hp", min_hp, prof=prof, spec=spec, race=race,clas=clas, body=body) / 1.4)
        case "warrior": hp = int(form("hp",min_hp,prof=prof,spec=spec,race=race,clas=clas,body=body) * 1.4)
        case "archer": hp = int(1.4 * form("hp",min_hp,prof=prof,spec=spec,race=race,clas=clas,body=body) / 1.3)
        case "nobody": hp = min_hp
        case _: hp = int(64 * randint(1, 3))
    return hp


def calc_mp(wisdom: int, prof: str, spec: str, race: str, clas: str):
    min_mp = db.get_object(obj_name="mana", category="base", types="characteristics")["attributes"]["min"]
    match clas:
        case "mage": mp = int(form("mp",min_mp,prof=prof,spec=spec,race=race,clas=clas,wisdom=wisdom) * 1.3)
        case "warrior": mp = int(form("mp",min_mp,prof=prof,spec=spec,race=race,clas=clas,wisdom=wisdom) * 1.4)
        case "archer": mp = int(1.4 * form("mp",min_mp,prof=prof,spec=spec,race=race,clas=clas,wisdom=wisdom) / 1.3)
        case "nobody": mp = min_mp
        case _: mp = int(64 * randint(1, 3))
    return mp


def calc_sm(dexterity: int, prof: str, spec: str, race: str, clas: str):
    min_sm = db.get_object(obj_name="stamina", category="base", types="characteristics")["attributes"]["min"]
    match clas:
        case "mage": sm = int(form("sm",min_sm,prof=prof,spec=spec,race=race,clas=clas,dexterity=dexterity) / 1.3)
        case "warrior": sm = int(form("sm",min_sm,prof=prof,spec=spec,race=race,clas=clas,dexterity=dexterity) * 1.6)
        case "archer": sm = int(1.4 * form("sm",min_sm,prof=prof,spec=spec,race=race,clas=clas,dexterity=dexterity) * 1.2)
        case "nobody": sm = min_sm
        case _: sm = int(64 * randint(1, 3))
    return sm


def calc_df(body: int, clas: str):
    min_df = db.get_object(obj_name="protection", category="base", types="characteristics")["attributes"]["min"]
    match clas:
        case "mage": df = int(form("df",min_df,body=body,clas=clas) * 1.1)
        case "warrior": df = int(form("df",min_df,body=body,clas=clas) * 1.2)
        case "archer": df = int(1.4 * form("df",min_df,body=body,clas=clas) * 1.3)
        case "nobody": df = int(form("df",min_df,body=body,clas=clas) * 1.4)
        case _: df = int(64 * randint(1, 3))
    return df


def calc_dmg(clas: str, master: int, power: int, wisdom: int):
    min_dmg = db.get_object(obj_name="damage", category="base", types="characteristics")["attributes"]["min"]
    match clas:
        case "mage": dmg = int(form("dmg",min_dmg,master=master,power=power,wisdom=wisdom) * 1.1)
        case "warrior": dmg = int(form("dmg",min_dmg,master=master,power=power,wisdom=wisdom))
        case "archer": dmg = int(1.4 * form("dmg",min_dmg,master=master,power=power,wisdom=wisdom) * 1.3)
        case "nobody": dmg = int(form("dmg",min_dmg,master=master,power=power,wisdom=wisdom) * 1.5)
        case _: dmg = int(64 * randint(1, 3))
    return dmg


def roll(rolling):
    rolling = [int(item) for item in rolling.split("d")]
    res = 0
    roll_numbers = set()
    for i in range(rolling[0]):
        num = randint(1,rolling[1])
        res += num
        roll_numbers.add(num)
    print(f"Rolls: {roll_numbers}")
    print(f"Roll Result: {res}")