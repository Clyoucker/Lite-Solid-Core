
class Weapon_Stats():

    def __init__(self):
        self.Damage = 5
        self.Weight = 1
        self.Cost = 128

class Sword(Weapon_Stats):
    def __init__(self):
        super().__init__()
    def ttt(self):
        print(self.__dict__)

s = Sword(2)
s.ttt()