from random import randint

class Weapon():
    def __init__(self,name:str, type_of_dice:int,melee:bool, ranged:bool,short_range=1, long_range=1, no_of_dice = 1):
        self.name= name
        self.type_of_dice = type_of_dice
        self.melee = melee
        self.ranged = ranged
        self.short_range = short_range
        self.long_range = long_range
        self.no_of_dice = no_of_dice

    def damage(self,critical=False):
        damage = 0
        for i in range(self.no_of_dice):
            damage+= randint(1,self.type_of_dice)
        if critical:
            for i in range(self.no_of_dice):
                damage += randint(1,self.type_of_dice)
        return damage

def create_weapon(name:str,type_of_dice:int,melee:bool,ranged:bool,short_range=0,long_range=0,no_of_dice=1):
    global weapons
    if name not in weapons:
        weapons[name] = Weapon(name,type_of_dice,melee,ranged,short_range,long_range,no_of_dice)
    return weapons[name]

def get_weapon(name:str): #weapon needs to be defined already
    global weapons
    return weapons[name] 


weapons = {'club':Weapon('club',4,True,False),
           'dagger':Weapon('dagger',4,True,True,4,12),
           'spear':Weapon('spear',6,True,True,4,12),
           'shortbow':Weapon('shortbow',6,False,True,20,80),
           'rapier':Weapon('rapier',4,True,False)
}

