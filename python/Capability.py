from Abilities import Abilities
from Characteristics import Characteristics
from Skills import Skills


class Capability(Abilities,Characteristics,Skills):
    def __init__(self,health: int,mana: int,stamina: int,protection: int,damage: int,skills: dict):
        Abilities.__init__(self)
        Characteristics.__init__(self,health=health,mana=mana,stamina=stamina,protection=protection,damage=damage)
        Skills.__init__(self,skills=skills)
