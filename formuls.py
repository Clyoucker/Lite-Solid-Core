from random import *

def Chance(success):
    r"""Формула, проверяющая, что Success больше рандомного значения"""
    if success >= randrange(101):
        return True
    else:
        return False

def Sell(cost, money, amount, skill, bonus):
    r"""Формула, высчитывающая выручку при продаже"""
    if type(cost) is int and 0 <= cost <= 10000:
        revenue = cost + (cost * ((skill * bonus) / 100))*amount
        money = money + revenue
        return round(money)
    else:
        raise SyntaxError(f"{cost}: not be str|0<={cost}<=10000")

def Buy(cost, money, amount, skill, bonus):
    r"""Формула, высчитывающая остаток от покупки"""
    if type(cost) is int and cost >= 0:
        cost = (cost-(cost*((skill * bonus) / 100)))*amount
        money = money - cost
        return round(money)
    else:
        raise SyntaxError(f"{cost}: not be str|{cost} < 0")

def Сommon(constant, hindrance=0, skill_bonus_value=None):

    if skill_bonus_value is None:
        skill_bonus_value = 1

    success = Chance(int((constant * skill_bonus_value) - hindrance))
    print(int((constant * skill_bonus_value) - hindrance))
    return success

def Learn(base_skill_bonus, class_bonus, skill_bonus_value, class_name):

    if base_skill_bonus == 0:
        base_skill_bonus = 0.5
    if class_bonus == 0:
        class_bonus = 0.5
    if skill_bonus_value == 0:
        skill_bonus_value = 0.5

    if class_name == "Маг":
        success = Chance(int(base_skill_bonus + class_bonus +  base_skill_bonus * skill_bonus_value))

    elif class_name == "Никто":
        success = Chance(int(base_skill_bonus + class_bonus + base_skill_bonus * skill_bonus_value))

    else:
        success = Chance(int(base_skill_bonus + base_skill_bonus * skill_bonus_value))

    return success




def Calc_Hp(constant, body, prof, spec, race, clas, class_name):
    r"""Формула, расчитывающая Heal Point"""

    if constant == 0:
        constant = 0.5
    if body == 0:
        body = 0.5

    if class_name == "маг":
        Hp = int((constant + (body * ((prof * spec) + (race * clas)))) / 1.4)

    elif class_name == "воин":
        Hp = int((constant + (body * ((prof * spec) + (race * clas)))) * 1.4)

    elif class_name == "стрелок":
        Hp = int(1.4 * (constant + (body * ((prof * spec) + (race * clas)))) / 1.3)

    elif class_name == "никто":
        Hp = constant

    else:
        Hp = int(constant * randint(1,3))

    return Hp

def Calc_Mp(constant, wisdom, prof, spec, race, clas, class_name):
    r"""Формула, расчитывающая Mana Point"""

    if constant == 0:
        constant = 0.5
    if wisdom == 0:
        wisdom = 0.5

    if class_name == "маг":
        Mp = int(constant + (wisdom * ((prof * spec) + (race * clas))) * 1.3)

    elif class_name == "воин":
        Mp = int(constant + (wisdom * ((prof * spec) + (race * clas))) / 1.2)

    elif class_name == "стрелок":
        Mp = int(constant + (wisdom * ((prof * spec) + (race * clas))) * 1.2)

    elif class_name == "никто":
        Mp = constant

    else:
        Mp = int(constant * randint (1,3))

    return Mp

def Calc_Sm(constant, dexterity, prof, spec, race, clas, class_name):
    r"""Формула, расчитывающая Stamina Point"""

    if constant == 0:
        constant = 0.5
    if dexterity == 0:
        dexterity = 0.5

    if class_name == "маг":
        Sm = int(constant + (dexterity * ((prof * spec) + (race * clas))) / 1.3)

    elif class_name == "воин":
        Sm = int(constant + (dexterity * ((prof * spec) + (race * clas))) * 1.6)

    elif class_name == "стрелок":
        Sm = int(constant + (dexterity * ((prof * spec) + (race * clas))) * 1.2)

    elif class_name == "никто":
        Sm = constant

    else:
        Sm = int(constant * randint (1,3))

    return Sm

def Calc_Df(constant, body, clas, class_name):
    r"""Формула, расчитывающая Defend Point"""

    if constant == 0:
        constant = 0.5
    if body == 0:
        body = 0.5
    if clas == 0:
        clas = 0.5

    if class_name == "маг":
        defend = int((constant + body * clas) * 1.1)

    elif class_name == "воин":
        defend = int ((constant + body * clas) * 1.2)

    elif class_name == "стрелок":
        defend = int ((constant + body * clas) * 1.3)

    elif class_name == "никто":
        defend = int((constant + body * clas) * 1.4)

    else:
        defend = int(constant * randint (1,3))

    return defend

def Calc_Dmg(constant, master, power, wisdom, class_name):
    r"""Формула, расчитывающая Damage Point Hit"""

    if constant == 0:
        constant = 0.5
    if master == 0:
        master = 0.5
    if power == 0:
        power = 0.5
    if wisdom == 0:
        wisdom = 0.5

    if class_name == "маг":
        damage = int((constant + master * power * wisdom) * 1.4)

    elif class_name == "воин":
        damage = int(constant + master * power * wisdom)

    elif class_name == "стрелок":
        damage = int((constant + master * power * wisdom) * 1.3)

    elif class_name == "никто":
        damage = int((constant + master * power * wisdom) * 1.5)

    else:
        damage = int(constant * randint (1,3))

    return damage


def Calc_Minimal():
    hp = randint(100,256)
    df = randint(0,8)
    dmg = randint(16,32)
    print(f"HP:{hp} | DF:{df} | DMG:{dmg}")

def Calc_Medium():
    hp = randint(256,364)
    df = randint(8,24)
    dmg = randint(32,48)
    print(f"HP:{hp} | DF:{df} | DMG:{dmg}")

def Calc_Max():
    hp = randint(364,640)
    df = randint(24,46)
    dmg = randint(48,86)
    print(f"HP:{hp} | DF:{df} | DMG:{dmg}")
